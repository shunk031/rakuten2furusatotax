import os

from rakuten2furusatotax.cli import create_driver, login_furusato_tax, login_rakuten


def test_login_rakuten():
    driver = create_driver(disable_headless=True)
    login_rakuten(
        driver=driver,
        login_id=os.environ["RAKUTEN_LOGIN_ID"],
        password=os.environ["RAKUTEN_PASSWORD"],
    )


def test_login_furusato_tax():
    driver = create_driver(disable_headless=True)
    login_furusato_tax(
        driver=driver,
        login_id=os.environ["FURUSATO_TAX_LOGIN_ID"],
        password=os.environ["FURUSATO_TAX_PASSWORD"],
    )
