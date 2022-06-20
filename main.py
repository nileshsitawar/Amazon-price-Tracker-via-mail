import requests
from smtplib import SMTP
from bs4 import BeautifulSoup as BS
url ="https://www.amazon.in/Dell-Monitor-S2421HN-Switching-Flicker-Free-Ultrathin/dp/B08GGF4L1K/ref=asc_df_B08GGF4L1K/?tag=googleshopdes-21&linkCode=df0&hvadid=396985551000&hvpos=&hvnetw=g&hvrand=10219357059414500253&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1007787&hvtargid=pla-1039877425613&ext_vrnc=hi&th=1"
def extract_price():
    page =requests.get(url,headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36"})
    soup = BS(page.content,"html.parser")
    b = soup.find( id ="corePrice_feature_div").text
    c = b[2:9].replace(",","")
    price= float(c.replace("₹",""))
    return price

def notify_():
    smtp_server ="smtp.gmail.com"
    port = 587
    email_id ="sitawarnilesh@gmail.com"
    password = "qxrulcdekwaxrktm"
    server = SMTP(smtp_server,port)
    server.starttls()
    server.login(email_id,password)
    subject ="BUY NOW"
    body ="Price has fallen ..! Go buy Now"  + url
    msg = f"subject:{subject}\n\n{body}"
    server.sendmail(email_id,email_id,msg)
    server.quit()

Affordabl_price =13804
if extract_price()<=Affordabl_price:
    notify_()
    