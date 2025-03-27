import re
import smtplib
from os import getenv
from dotenv import load_dotenv
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

### NOTE: Currently only Amazon returns prices ###
load_dotenv()

URLS = {
    "Amazon": "https://www.amazon.de",
    "Idealo": "https://www.idealo.de/",
    "Alternate": "https://www.alternate.de/",
    "Geizhals": "https://geizhals.de/",
    "Mindfactory": "https://www.mindfactory.de/"
}

TARGET_PRICE = 700  

EMAIL_SENDER = getenv("GMAIL")
EMAIL_PASSWORD = getenv("PASSWORD")  
EMAIL_RECEIVER = getenv("GMAIL")

def send_email(retailer, price):
    subject = f"Price Alert! AMD 9070 XT at €{price} on {retailer}, here: {URLS[retailer]}"
    body = f"Price Alert! AMD 9070 XT at €{price} on {retailer}, here: {URLS[retailer]}"
    msg = f"Subject: {subject}\n\n{body}"

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, msg)
        server.quit()
        print(f"Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")

def get_price(driver, url, keyword="9070xt"):
    driver.get(url)
    print(f"[{datetime.now()}] Checking price for {url}...")

    try:
        if "amazon" in url.lower():
            search_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "#twotabsearchtextbox"))
            )
        elif "idealo" in url.lower():
            search_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '#i-search-input'))
            )
        elif "alternate" in url.lower():
            search_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '#search-input-m'))
            )
        elif "geizhals" in url.lower():
            search_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '#gh-ac-input'))
            )
        elif "mindfactory" in url.lower():
            search_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '#search_query'))
            )

        search_input.clear()  
        search_input.send_keys(f"{keyword}")  
        search_input.send_keys(Keys.RETURN)  

        if "amazon" in url.lower():
            price_elements = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".a-price-whole"))
            )
        elif "idealo" in url.lower():
            price_elements = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".sr-detailedPriceInfo__price_sYVmx"))
            )
        elif "alternate" in url.lower():
            price_elements = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".price"))
            )
        elif "geizhals" in url.lower():
            price_elements = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, ".listview__price"))
            )
        elif "mindfactory" in url.lower():
            price_elements = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".pprice"))
            )

        prices = []
        for price_element in price_elements:
            price = price_element.text.strip() 
            prices.append(price)

        print(prices)

        lowest_price = float('inf')
        for price in prices:
            price_value = float(re.sub(r'[^\d.]', '', price))  
            if price_value <= TARGET_PRICE and price_value < lowest_price:
                lowest_price = price_value
                print(f"Found lower price: {lowest_price}")
                send_email(url, lowest_price)

        return lowest_price

    except Exception as e:
        print(f"An error occurred while getting the price: {e}")
        return float('inf')

def run():
    options = Options()
    options.add_argument("--headless")  
    driver = webdriver.Chrome(options=options)
    
    lowest_price = float('inf')
    retailer_name = None

    for retailer, url in URLS.items():
        price = get_price(driver, url)
        if price < lowest_price:
            lowest_price = price
            retailer_name = retailer

    driver.quit()

    if lowest_price <= TARGET_PRICE:
        print(f"Lowest price found: €{lowest_price} at {retailer_name}! Sending alert...")
        send_email(retailer_name, lowest_price)
    else:
        print(f"Lowest price is €{lowest_price} at {retailer_name}. No alert sent.")

run()
