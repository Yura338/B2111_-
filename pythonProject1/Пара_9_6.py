from bs4 import BeautifulSoup
import requests

response = requests.get("https://bank.gov.ua/ua/markets/exchangerates")
if response.status_code == 200:
    soup = BeautifulSoup(response.text, features="html.parser")
    soup_list = soup.find_all("td",{"data-label": "Офіційний курс"})
    print(soup_list)
    res = soup_list[7]
    print(res.text)

many = int(input("Enter sum:"))
dol = many/float(res.text.replace(',', '.'))
print(dol)