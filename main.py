
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# From the 500 Items and Services List table we only want the first column (CODE)
# to print them in this format: ('code1','code2',...'codeN')
url = "https://www.cms.gov/healthplan-price-transparency/resources/500-items-services"
output = ""

options = Options()
options.add_argument("--headless")

driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
driver.get(url)

table = driver.find_element(By.TAG_NAME, "tbody")
rows = table.find_elements(By.TAG_NAME, "tr")
print(f"Scraping {len(rows)} codes...")

print("(",end="")
for row in rows:       
    col = row.find_elements(By.TAG_NAME, "td")[0]
    output += "'"+col.text.strip()+"',"

print(output[:-1]+")")
driver.quit()
