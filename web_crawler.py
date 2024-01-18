import requests as req
from bs4 import BeautifulSoup as bs
import pandas as pd
import re

titleList = []
priceList = []

for i in range(1,2):
  res = req.get("https://emart.ssg.com/disp/theme/category.ssg?dispCtgId=6000224045&page="+str(i))
  soup = bs(res.text, "lxml")

  title = soup.select("span.mnemitem_goods_tit")
  price = soup.select("em.ssg_price")

  pattern = r'[\[\(][^)\]]*[\]\)]' 

  for t in title:
    text = re.sub(pattern=pattern, repl='', string=t.text)
    titleList.append(text);

  for p in price:
    text = re.sub(r',', '', p.text)
    priceList.append(p.text);

# df = pd.DataFrame({'Column1': titleList, 'Column2': priceList})
df = pd.DataFrame({"상품": titleList})
df.to_csv("data.csv", encoding="utf-8", index=False)
