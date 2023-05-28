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


def login_rakuten(
    driver: WebDriver,
    rakuten_login_id: str,
    rakuten_password: str,
) -> WebDriver:
    # ログインページへアクセス
    driver.get("https://grp02.id.rakuten.co.jp/rms/nid/login")

    # 日本語にする
    driver.execute_script('document.formLang1.lang.value = "ja"')
    driver.execute_script("document.formLang1.submit();")

    driver.find_element(By.ID, "loginInner_u").send_keys(rakuten_login_id)
    driver.find_element(By.ID, "loginInner_p").send_keys(rakuten_password)
    driver.find_element(By.CLASS_NAME, "loginButton").click()

    driver.find_element(By.CLASS_NAME, "submit").find_element(
        By.TAG_NAME, "input"
    ).click()
    driver.find_element(By.CLASS_NAME, "submit").find_element(
        By.TAG_NAME, "input"
    ).click()

    return driver


@click.command()
@click.option("--rakuten-login-id", type=str, required=True)
@click.option("--rakuten-password", type=str, required=True)
@click.option("--disable-headless", is_flag=True, default=False)
def run(
    rakuten_login_id: str,
    rakuten_password: str,
    disable_headless: bool,
):
    options = webdriver.ChromeOptions()
    if not disable_headless:
        options.add_argument("--headless")

    executable_path = ChromeDriverManager().install()
    logger.info(f"Executable path: {executable_path}")

    chrome_service = service.Service(executable_path=executable_path)
    driver = webdriver.Chrome(service=chrome_service, options=options)

    driver = login_rakuten(
        driver=driver,
        rakuten_login_id=rakuten_login_id,
        rakuten_password=rakuten_password,
    )

    breakpoint()
