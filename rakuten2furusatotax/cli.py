import logging

import click
from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s", level=logging.INFO
)

logger = logging.getLogger(__name__)


def create_driver(disable_headless: bool) -> WebDriver:
    options = webdriver.ChromeOptions()
    if not disable_headless:
        options.add_argument("--headless")

    executable_path = ChromeDriverManager().install()
    logger.info(f"Executable path: {executable_path}")

    chrome_service = service.Service(executable_path=executable_path)
    driver = webdriver.Chrome(service=chrome_service, options=options)

    return driver


def login_rakuten(
    driver: WebDriver,
    login_id: str,
    password: str,
) -> WebDriver:
    # ログインページへアクセス
    driver.get("https://grp02.id.rakuten.co.jp/rms/nid/login")

    # 日本語にする
    driver.execute_script('document.formLang1.lang.value = "ja"')
    driver.execute_script("document.formLang1.submit();")

    driver.find_element(By.ID, "loginInner_u").send_keys(login_id)
    driver.find_element(By.ID, "loginInner_p").send_keys(password)
    driver.find_element(By.CLASS_NAME, "loginButton").click()

    driver.find_element(By.CLASS_NAME, "submit").find_element(
        By.TAG_NAME, "input"
    ).click()
    driver.find_element(By.CLASS_NAME, "submit").find_element(
        By.TAG_NAME, "input"
    ).click()

    return driver


def login_furusato_tax(driver: WebDriver, login_id: str, password: str) -> WebDriver:
    driver.get("https://www.furusato-tax.jp/login")
    driver.find_element(By.CLASS_NAME, "frm-input").send_keys(login_id)
    driver.find_element(By.CLASS_NAME, "frm-pass__input").send_keys(password)
    driver.find_element(By.CLASS_NAME, "btn-positive").click()
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
    driver = create_driver()

    # driver = login_rakuten(
    #     driver=driver,
    #     login_id=rakuten_login_id,
    #     password=rakuten_password,
    # )

    # driver = login_furusato_tax(
    #     driver=driver,
    #     login_id=furusato_tax_login_id,
    #     password=furusato_tax_password,
    # )

    breakpoint()
