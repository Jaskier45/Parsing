from email import header
import time
from matplotlib.pyplot import text
import requests
import os
from bs4 import BeautifulSoup


def  get_all_pages():
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36"
    }

    # r = requests.get(url="https://watch.ua/gucci-uk.html", headers=headers)
    
    # if not os.path.exists("data"):
    #     os.mkdir("data")

    # with open("data/page_1.html", "w", encoding="utf-8") as file:
    #     file.write(r.text)

    with open ("data/page_1.html", encoding="utf-8") as file:
        src = file.read()
    
    soup = BeautifulSoup(src, "lxml")
    page_count = int(soup.find("div", class_="ty-pagination__items").find_all("a")[-1].text)
    
    for i in range(1, page_count + 1):
        url = f"https://watch.ua/gucci-uk-page-{i}.html"
    
        r = requests.get(url=url, headers= headers)

        with open (f"data/page_{i}.html", "w", encoding= "utf-8") as file:
            file.write(r.text)
        
        time.sleep(2)

    return page_count + 1


def collect_data(pages_count):

    for page in range(1,pages_count):
        with open(f"data/page_{page}.html", encoding= "utf-8") as file:
            src = file.read()

        soup = BeautifulSoup(src, "lxml")
        item_cards = soup.find_all("a", class_ = "product-title")
        item_price = soup.find("span", class_ = "ty-price-num")
        # print(item_price)

        for item in item_cards:
            item_title = item.text
            item_link = item.get("href")
            
            for item in item_price:
                item_cost = item.text
            # item_pricee = item.find("span", class_ = "ty-price-num")
            print(f"{item_title}: {item_cost} :{item_link}")
            # print(item_name, item_link)


        # for item in item_cards:
        #     item_title = item.text
        #     item_link = item.get("href")
        #     # item_pricee = item.find("span", class_ = "ty-price-num")
        #     print(f"{item_title}: {item_pricee} :{item_link}")
        #     # print(item_name, item_link)

def main():
    pages_count = get_all_pages()
    collect_data(pages_count=pages_count)


if __name__ == '__main__':
    main()
    