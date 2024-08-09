from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

site = "https://www.cardkingdom.com/mtg/fifth-dawn/avarice-totem"
element = "/html/body/div[1]/div[2]/div[2]/div[2]/div/div[3]/div[1]/ul[2]/li[1]/form/div[1]"

chroptions = Options()
chroptions.add_argument("--headless=new")
driver = webdriver.Chrome(options = chroptions)

def checkit(siteaddr, elementxpath):
    driver.get(siteaddr)

    element = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, elementxpath))
            )

    substance = element.get_attribute('innerHTML')
    storage = open("storage.txt", "r+")
    if substance != storage.read():
        print("scrapechecker > Difference noted!")
        print("scrapechecker > Previous: {}".format(storage.read()))
        storage.write(substance)
        storage.close()
        storage = open("storage.txt", "r")
        print("scrapechecker > Updated: {}".format(storage.read()))
        storage.close()
    else:
        print("No changes detected.")

    driver.close()

    


if __name__ == "__main__":
    checkit(site, element)



'''html = driver.execute_script("return document.documentElement.innerHTML;")

print(html)       

f = open("htmlstorage.txt", "w")
f.write(html)
f.close()

driver.close()'''