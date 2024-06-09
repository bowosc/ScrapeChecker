from selenium import webdriver

driver = webdriver.Firefox()

driver.get("https://example.com/")

html = driver.execute_script("return document.documentElement.innerHTML;")

print(html)       

f = open("htmlstorage.txt", "w")
f.write(html)
f.close()

driver.close()