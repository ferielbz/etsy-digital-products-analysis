import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import csv

# Step 1: Open browser
driver = uc.Chrome()
driver.get("https://www.etsy.com")

# Step 2: Wait for you to solve CAPTCHA manually
print("Please solve the CAPTCHA in the browser... then press ENTER here.")
input()  # Waits for you to press Enter

# Step 3: Perform search
search_box = driver.find_element(By.NAME, "search_query")
search_box.send_keys("digital planner")
search_box.send_keys(Keys.ENTER)
time.sleep(5)

# Step 4: Extract product data
products = driver.find_elements(By.CSS_SELECTOR, 'li.wt-list-unstyled')
data = []

for item in products:
    try:
        title = item.find_element(By.CSS_SELECTOR, 'h3').text.strip()
        price = item.find_element(By.CSS_SELECTOR, 'span.currency-value').text.strip()
        url = item.find_element(By.TAG_NAME, 'a').get_attribute("href").split("?")[0]
        data.append({"title": title, "price": price, "url": url})
    except:
        continue

# Step 5: Save to CSV
with open("etsy_data.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["title", "price", "url"])
    writer.writeheader()
    writer.writerows(data)

driver.quit()
print(f"✅ Saved {len(data)} products to etsy_data.csv")
