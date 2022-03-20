from bs4 import BeautifulSoup
import requests
import lxml
import smtplib

FROM_EMAIL = "harryformus@gmail.com"
MY_EMAIL = "pythonproject862@gmail.com"
MY_PASSWORD = "goober1!"

HEADERS = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko)"
                  " Chrome/96.0.4664.110 Safari/537.36",
}

response = requests.get(url="https://www.amazon.com/Instant-Zest-Rice-Cooker-Pot/dp/B07TZL8Y3C/ref=sr_1_3?"
                        "crid=211KSQ8GI3YWB&keywords=instant+pot+rice+cooker&qid=1643281224&s="
                        "home-garden&sprefix=instant+pot+rice+cooker%2Cgarden%2C64&sr=1-3", headers=HEADERS)

product_text = response.text

soup = BeautifulSoup(product_text, "lxml")

price = soup.find("span", class_="a-offscreen").get_text()
price_no_dollar_sign = price.split("$")[1]
price_as_float = float(price_no_dollar_sign)

if price_as_float < 40.00:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=FROM_EMAIL,
                            msg=f"The price of the item you've been watching has dropped below"
                                f" $40.00!")

