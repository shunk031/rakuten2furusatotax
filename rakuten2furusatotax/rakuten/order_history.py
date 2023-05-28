from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
import datetime
from selenium.webdriver.support.select import Select
from rakuten2furusatotax.furusato_tax_info import FurusatoTaxInfo
from typing import List
import logging

logger = logging.getLogger(__name__)


def get_furusato_tax_info_list(driver: WebDriver) -> List[FurusatoTaxInfo]:
    driver.get("https://order.my.rakuten.co.jp/?l-id=pc_header_func_ph")
    current_year = datetime.date.today().year
    select_year_dropdown = driver.find_element(By.ID, "selectPeriodYear")
    select = Select(select_year_dropdown)

    # select.select_by_value(str(current_year))
    # select.select_by_value("2022")

    order_list_wrap_div = driver.find_element(By.ID, "oDrListWrap")
    order_list_items = order_list_wrap_div.find_elements(By.CLASS_NAME, "oDrListItem")

    furusato_tax_info_list = []
    for order_list_item in order_list_items:
        item_name_tag = order_list_item.find_element(By.CLASS_NAME, "itemName")

        if item_name_tag.text.startswith("【ふるさと納税】"):
            purchase_date_tag = order_list_item.find_element(
                By.CLASS_NAME, "purchaseDate"
            )
            purchase_date = datetime.datetime.strptime(
                purchase_date_tag.text, "%Y年%m月%d日"
            )

            shop_name_tag = order_list_item.find_element(By.CLASS_NAME, "shopName")
            shop_name = shop_name_tag.text

            price_tag = order_list_item.find_element(By.CLASS_NAME, "price")
            price = int(price_tag.text.replace(",", ""))

            furusato_tax_info = FurusatoTaxInfo(
                application_date=purchase_date,
                municipality_name=shop_name,
                donation_price=price,
            )
            logger.info(furusato_tax_info)
            furusato_tax_info_list.append(furusato_tax_info)

    return furusato_tax_info_list
