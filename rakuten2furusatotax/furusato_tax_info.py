from dataclasses import dataclass
import datetime
from typing import Optional
import re


@dataclass
class FurusatoTaxInfo(object):
    application_date: datetime.datetime
    municipality_name: str
    donation_price: int
    prefecture: Optional[str] = None
    municipalities: Optional[str] = None

    def __post_init__(self) -> None:
        matches = re.match(r"(.+?[都道府県])(.+?[市区町村])", self.municipality_name)
        if matches:
            groups = matches.groups()
            assert (
                len(groups) == 2
            ), f"{self.municipality_name} という入力から正しく自治体情報を抽出することができませんでした。(抽出結果: {groups})"

            self.prefecture = groups[0]
            self.municipalities = groups[1]
        else:
            raise ValueError(
                f'"{self.municipality_name}" という入力から正しく自治体情報を抽出することができませんでした。'
            )
