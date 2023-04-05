
import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


# Problem #1: From the 500 Items and Services List table we only want the first column values (Code)
# to print them in this format: ('code1','code2',...'codeN')

# Problem #2: From the 500 Items and Services List table we want to store all column values (Code, Description
# Plain Language Description) into a data structure, and then generate a csv file from there.

class item:
    def __init__(self, code, description, plainDescription):
        self.code = code
        self.description = description
        self.plainDescription = plainDescription

items = []

url = "https://www.cms.gov/healthplan-price-transparency/resources/500-items-services"
outputSol1 = ""

options = Options()
options.add_argument("--headless")

driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
driver.get(url)

table = driver.find_element(By.TAG_NAME, "tbody")
rows = table.find_elements(By.TAG_NAME, "tr")
print(f"Scraping {len(rows)} codes...")
     
#Problem 1 solution
print("(",end="")
for row in rows:       
    code = row.find_elements(By.TAG_NAME, "td")[0].text.strip()
    description = row.find_elements(By.TAG_NAME, "td")[1].text.strip().replace(",","").replace("\n","")
    plainDescription = row.find_elements(By.TAG_NAME, "td")[2].text.strip().replace(",","")
    outputSol1 += "'"+code+"',"
    items.append(item(code, description, plainDescription))
print(outputSol1[:-1]+")")

#Problem 2 solution
with open('500items.csv', 'w', newline='') as file:
     writer = csv.writer(file)
     writer.writerow(["Code", "Description", "Plain Language Description"])
     for record in items:
        writer.writerow([record.code, record.description, record.plainDescription])
file.close
driver.quit()
