import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

def main():

    suffix = "https://www.amazon.com/s?k=gaming+laptops&page="
    prefix = "pf_rd_i=23508887011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=434db2ed-6d53-4c59-b173-e8cd550a2e4f&pf_rd_r=D2PPPQAC9Z2H0FPJ8M9A&pf_rd_s=merchandised-search-5&pf_rd_t=101&qid=1705773238&ref=sr_pg_"
    
    # Adding Options to fool the anti-scraping method in Amazon 
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    options.add_argument(f"--user-agent={user_agent}")

    driver = webdriver.Chrome(options=options)

    laptop_links = []

    for i in range(20):
        page_no = i+1
        url = suffix + str(page_no) + prefix + str(page_no)
        driver.get(url=url)
        print(f"From Page:{page_no}============================================>>>>>>>>")
        # print(url)

        laptop_link_elements = driver.find_elements(by=By.XPATH, value="//a[@class='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal']")
        # print(laptop_link_elements)
        
        laptop_links.extend([element.get_attribute("href") for element in laptop_link_elements])
        # print(laptop_links)

        df  = pd.DataFrame(data=laptop_links, columns = ["urls"])
        df.to_csv("./csv_files/laptop_links.csv", index=False)

        time.sleep(3)

    driver.close()
    
if "__name__ == main":
    main()