import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Workflow to simulate searching for a product, adding it to cart, and registering a account


username = "user"
email = "user@example.com"
password = "1234567890"

with webdriver.Chrome() as driver:
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("http://127.0.0.1:8000")

        # Assumes the search bar has id="search-bar"
        search_box = wait.until(EC.presence_of_element_located((By.ID, "search-bar")))
        search_box.send_keys("Product 1")
        search_box.send_keys(Keys.RETURN)

        # Assumes search result renders elements with class="product-card" inside "product-grid"
        product = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".product-grid .product-card")
        ))
        product.click()

        # Assumes the "Add to Cart" button has class and type defined as below
        add_to_cart = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'button.btn.btn-secondary[type="submit"]')
        ))
        add_to_cart.click()

        # Assumes /register/ route exists and is linked with an <a href="/register/"> 
        register_link = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'a[href="/register/"]')
        ))
        register_link.click()

        # Registration fields
        wait.until(EC.presence_of_element_located((By.NAME, "email")))
        driver.find_element(By.NAME, "email").send_keys(email)
        driver.find_element(By.NAME, "username").send_keys(username)
        driver.find_element(By.NAME, "password").send_keys(password)

        driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

        time.sleep(5)

    except Exception as e:
        print("Error:", e)
        time.sleep(5)  