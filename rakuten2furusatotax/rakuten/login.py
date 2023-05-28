from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


def _set_language(driver: WebDriver) -> WebDriver:
    # 日本語にする
    driver.execute_script('document.formLang1.lang.value = "ja"')
    driver.execute_script("document.formLang1.submit();")
    return driver


def _login_rakuten(driver: WebDriver, login_id: str, password: str) -> WebDriver:
    driver.find_element(By.ID, "loginInner_u").send_keys(login_id)
    driver.find_element(By.ID, "loginInner_p").send_keys(password)
    driver.find_element(By.CLASS_NAME, "loginButton").click()
    return driver


def confirm_registered_contact_information(driver: WebDriver) -> WebDriver:
    next_button_tag = driver.find_element(By.CLASS_NAME, "submit")
    next_button_tag.find_element(By.TAG_NAME, "input").click()
    return driver


def confirm_registered_credit_card(driver: WebDriver) -> WebDriver:
    next_button_tag = driver.find_element(By.CLASS_NAME, "submit")
    next_button_tag.find_element(By.TAG_NAME, "input").click()
    return driver


def login_rakuten(
    driver: WebDriver,
    login_id: str,
    password: str,
) -> WebDriver:
    # ログインページへアクセス
    driver.get("https://grp02.id.rakuten.co.jp/rms/nid/login")

    driver = _set_language(driver=driver)

    driver = _login_rakuten(
        driver=driver,
        login_id=login_id,
        password=password,
    )

    driver = confirm_registered_contact_information(driver=driver)
    driver = confirm_registered_credit_card(driver=driver)

    return driver
