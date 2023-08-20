"""
Module parse data from myfin 
"""
import requests
from bs4 import BeautifulSoup as BS

from string import digits


URL ="https://myfin.by/currency/usd"

class Parser:

    def get_html_page(self) -> str:
        """
        Parse html page from site
        """
        with requests.get(URL) as responce:
            html = responce.text
            return html

    def parse_html(self) -> list[tuple[str, float, float]]:
        """
        Find in html data these write in DB
        """
        data_list = []
        html = self.get_html_page()
        soup = BS(html, "lxml")

        # processe parsing
        div = soup.find("tbody", class_="sort_body")
        div_with_table = div.find_all("tr", class_="currencies-courses__row-main")
        for item in div_with_table:
            name, surrender, buy = item.find_all("td")[:3]

            data = self.serializer_data(name=name.text, surrunder_currency=surrender.text, buy_currency=buy.text)
            data_list.append(data)

        return data_list 

    def serializer_data(self, name: str, surrunder_currency: str, buy_currency: str) -> tuple[str, float, float]:
        """
        Serilizer data before it goes to the DB
        """
        name = name.strip()
        if set(surrunder_currency).intersection(set(digits)) != set():
            surrunder_currency = float(surrunder_currency.strip())
        else:
            surrunder_currency = None
        if set(buy_currency).intersection(set(digits)) != set():
            buy_currency = float(buy_currency.strip())
        else:
            buy_currency = None

        return (name, surrunder_currency, buy_currency)
        

