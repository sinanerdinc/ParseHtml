import requests
from bs4 import BeautifulSoup

url = "https://boxofficeturkiye.com/hafta/?yil=2018&hafta=7"
headers_param = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36"}
r = requests.get(url,headers = headers_param)
soup = BeautifulSoup(r.content,"lxml")

# class değeri ustcizgi olan table altındaki 2. tr nin altındaki td nin altındaki 3. table ın altındaki tr yi çektik.
filmTablosu = soup.find("table",attrs={"class":"ustcizgi"}).select("tr:nth-of-type(2) > td > table:nth-of-type(3) > tr")

for i in range(1,21):
    filmAdi = filmTablosu[i].find("a",attrs={"class":"film"}).get("title")
    toplamSeyirci = filmTablosu[i].select("td:nth-of-type(10) > font")[0].text
    hasilat = filmTablosu[i].select("td:nth-of-type(9) > font")[0].text
    print("Film Adı: {} \nHasılat: {} \nToplam Seyirci: {}".format(filmAdi,hasilat,toplamSeyirci))
    print("-"*30)
