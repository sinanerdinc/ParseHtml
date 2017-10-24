import requests
from bs4 import BeautifulSoup

r = requests.get("https://goo.gl/pXM4u1",allow_redirects=True,headers={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"})
soup = BeautifulSoup(r.content,"lxml")

games = soup.find_all("div",attrs={"class":"tab_row"})
print("{} games listed.".format(len(games)))
print("#"*20)
for game in games:
    try:
        print("Game: [{}] -> Discount: [{}] -> Price: [{}] -> Url: [{}]".format(
        game.h4.text,
        game.find("div",attrs={"class":"tab_discount discount_pct"}).string.strip(),
        game.find("span",attrs={"class":"price"}).string.strip(),
        game.find("div",attrs={"class":"tab_overlay"}).a.get("href")
        ))
    except Exception as e:
        pass
