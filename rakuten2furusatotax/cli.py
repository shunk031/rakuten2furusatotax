import logging
import datetime
import click

from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select

from rakuten2furusatotax.rakuten import login_rakuten
from rakuten2furusatotax.furusato_tax import login_furusato_tax
from rakuten2furusatotax.furusato_tax_info import FurusatoTaxInfo
import time

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s", level=logging.INFO
)

logger = logging.getLogger(__name__)


def create_driver(disable_headless: bool) -> WebDriver:
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-dev-shm-usage")

    if not disable_headless:
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")

    executable_path = ChromeDriverManager().install()
    logger.info(f"Executable path: {executable_path}")

    chrome_service = service.Service(executable_path=executable_path)
    driver = webdriver.Chrome(service=chrome_service, options=options)

    return driver


@click.command()
@click.option("--rakuten-login-id", type=str, required=True)
@click.option("--rakuten-password", type=str, required=True)
@click.option("--furusato-tax-login-id", type=str, required=True)
@click.option("--furusato-tax-password", type=str, required=True)
@click.option("--disable-headless", is_flag=True, default=False)
def run(
    rakuten_login_id: str,
    rakuten_password: str,
    furusato_tax_login_id: str,
    furusato_tax_password: str,
    disable_headless: bool,
):
    driver = create_driver(
        disable_headless=disable_headless,
    )
    driver = login_rakuten(
        driver=driver,
        login_id=rakuten_login_id,
        password=rakuten_password,
    )

    driver = get_furusato_tax_info_list(driver)

    driver = login_furusato_tax(
        driver=driver,
        login_id=furusato_tax_login_id,
        password=furusato_tax_password,
    )

    for furusato_tax_info in furusato_tax_info_list:
        driver.get("https://www.furusato-tax.jp/mypage/contribution/history/list")
        driver.find_element(By.LINK_TEXT, "寄付履歴を手動追加").click()

        select_year_dropdown = driver.find_element(
            By.XPATH, "//select[@class='form_entry _year']"
        )
        select = Select(select_year_dropdown)
        select.select_by_value(str(furusato_tax_info.application_date.year))

        select_month_dropdown = driver.find_element(
            By.XPATH, "//select[@class='form_entry _month']"
        )
        select = Select(select_month_dropdown)
        select.select_by_value(str(furusato_tax_info.application_date.month))

        select_day_dropdown = driver.find_element(
            By.XPATH, "//select[@class='form_entry _day']"
        )
        select = Select(select_day_dropdown)
        select.select_by_value(str(furusato_tax_info.application_date.day))

        select_prefecture_dropdown = driver.find_element(By.ID, "prefecture_id")
        select = Select(select_prefecture_dropdown)
        select.select_by_visible_text(furusato_tax_info.prefecture)
        time.sleep(1)

        select_city_dropdown = driver.find_element(By.ID, "cities")
        select = Select(select_city_dropdown)
        select.select_by_visible_text(furusato_tax_info.municipalities)

        driver.find_element(
            By.XPATH, "//input[@name='donation_amount_comma']"
        ).send_keys(str(furusato_tax_info.donation_price))

        # 確定ボタンを押す
        driver.find_element(By.CLASS_NAME, "btn-positive__text").click()

        # 寄付履歴へ戻る
        driver.find_element(By.LINK_TEXT, "寄付履歴へ").click()
