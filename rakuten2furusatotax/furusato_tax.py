from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


def login_furusato_tax(driver: WebDriver, login_id: str, password: str) -> WebDriver:
    driver.get("https://www.furusato-tax.jp/login")
    driver.find_element(By.CLASS_NAME, "frm-input").send_keys(login_id)
    driver.find_element(By.CLASS_NAME, "frm-pass__input").send_keys(password)
    driver.find_element(By.CLASS_NAME, "btn-positive").click()
    return driver
