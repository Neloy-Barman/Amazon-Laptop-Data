import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

columns = ["brand", "model_name", "screen_size", "color", "cpu_model", "ram", "os", "special_feature", "graphics_card_type", "graphics_coprocessor", "price", "average_ratings"]

laptop_details = []

def main():

    
    url = "https://www.amazon.com/ASUS-Display-GeForce-Windows-FA707NU-DS74/dp/B0BWH9XCHC/ref=sr_1_6?keywords=gaming%2Blaptops&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=434db2ed-6d53-4c59-b173-e8cd550a2e4f&pf_rd_r=D2PPPQAC9Z2H0FPJ8M9A&pf_rd_s=merchandised-search-5&pf_rd_t=101&qid=1705809677&sr=8-6&th=1"

    # Adding Options to fool the anti-scraping method in Amazon 
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    options.add_argument(f"--user-agent={user_agent}")

    driver = webdriver.Chrome(options=options)

    urls = pd.read_csv("./csv_files/laptop_links.csv")['urls'].to_list()

    for url in urls:

        driver.get(url=url)
        
        time.sleep(3)

        try:
            see_more_button = driver.find_element(by=By.XPATH, value="//div[@id='poToggleButton']/a/i")
            see_more_button.click()
        except:
            pass
        
        try:
            brand = driver.find_element(by=By.XPATH, value="//tr[@class='a-spacing-small po-brand']/td[2]/span").text
        except:
            brand = None
        
        try:
            model_name = driver.find_element(by=By.XPATH, value="//tr[@class='a-spacing-small po-model_name']/td[2]/span").text
        except:
            model_name = None
        
        try:
            screen_size = driver.find_element(by=By.XPATH, value="//tr[@class='a-spacing-small po-display.size']/td[2]/span").text
        except:
            screen_size = None

        try:
            color = driver.find_element(by=By.XPATH, value="//tr[@class='a-spacing-small po-color']/td[2]/span").text
        except:
            color = None

        try:
            cpu_model = driver.find_element(by=By.XPATH, value="//tr[@class='a-spacing-small po-cpu_model.family']/td[2]/span").text
        except:
            cpu_model = None

        try:
            ram = driver.find_element(by=By.XPATH, value="//tr[@class='a-spacing-small po-ram_memory.installed_size']/td[2]/span").text
        except:
            ram = None

        try:
            os = driver.find_element(by=By.XPATH, value="//tr[@class='a-spacing-small po-operating_system']/td[2]/span").text
        except:
            os = None

        try:
            special_feature = driver.find_element(by=By.XPATH, value="//tr[@class='a-spacing-small po-special_feature']/td[2]/span").text
        except:
            special_feature = None
        
        try:
            graphics_card_type = driver.find_element(by=By.XPATH, value="//tr[@class='a-spacing-small po-graphics_description']/td[2]/span").text
        except:
            graphics_card_type = None
        
        try:
            graphics_coprocessor = driver.find_element(by=By.XPATH, value="//tr[@class='a-spacing-small po-graphics_coprocessor']/td[2]/span").text
        except:
            graphics_coprocessor = None
        
        try:
            price = driver.find_element(by=By.XPATH, value="//span[@class='a-price-whole']").text
        except:
            price = None

        try:
            average_ratings = driver.find_element(by=By.XPATH, value="//span[@id='acrPopover']/span/a/span").text
        except:
            average_ratings = None

        details = {
            "brand": brand,
            "model_name": model_name,
            "screen_size": screen_size,
            "color": color,
            "cpu_model": cpu_model,
            "ram": ram,
            "os": os,
            "special_feature": special_feature,
            "graphics_card_type": graphics_card_type,
            "graphics_coprocessor": graphics_coprocessor,
            "price": price,
            "average_ratings": average_ratings
        }

        print(f"{details}\n")

        laptop_details.append(details)

        df = pd.DataFrame(data = laptop_details, columns = columns)
        # df.to_csv("./csv_files/laptop_details.csv", index=False)

        df.to_csv("laptop_details.csv", index=False)

    
    driver.close()

if "__name__ == main":
    main()