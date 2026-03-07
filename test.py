from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep
o = ChromeOptions()
o.add_experimental_option(name="detach", value=True)
driver = Chrome(options=o)
driver.maximize_window()
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


# Question 1
#
# driver.get("https://www.amazon.in/")
# sleep(4)
# a = driver.find_elements("class name", "nav-sprite")
# for item in a:
#     print(item.text)

#--------------------------------------------------------------------------------
#Question 2 Print top 10 movie names from IMDB Top 250

# driver.get("https://www.imdb.com/chart/top/")
# driver.maximize_window()
# sleep(3)
#
# movies = driver.find_elements(By.XPATH, "//h3[@class='ipc-title__text']")
#
# for i in range(1,11):
#     print(movies[i].text)
#--------------------------------------------------------------------------------
## Question 3 count all images on amazon

# driver.get("https://www.amazon.in")
# sleep(5)
#
# images = driver.find_elements(By.TAG_NAME, "img")
#
# print("Total images:", len(images))
#--------------------------------------------------------------------------------
## Question 4

# driver.get("https://demoqa.com/select-menu")
# sleep(3)
#
#
# driver.find_element(By.ID, "withOptGroup").click()
# sleep(2)
#
#
# driver.find_element(By.XPATH, "//div[text()='Group 1, option 1']").click()
#
# sleep(2)
#--------------------------------------------------------------------------------
# Question 5
# driver.get("https://www.amazon.in/")
# sleep(3)
#
# links = driver.find_elements(By.TAG_NAME,"a")
#
# for link in links:
#     print(link.text)


#--------------------------------------------------------------------------------
# Question 6
# driver.get("https://www.google.com")
#
# search = driver.find_element(By.NAME,"q")
# search.send_keys("football")
# sleep(3)
#
# a = driver.find_elements(By.XPATH,"//li[@role='presentation']")
#
# for i in a:
#     print(i.text)

#-------------------------------------------------------------------------------------
# Question 7
# driver.get("https://www.amazon.com")
# sleep(3)
#
# a = driver.find_element(By.ID, "nav-link-accountList")
#
# o= ActionChains(driver)
# o.move_to_element(a).perform()
#
# sleep(2)
#
# driver.find_element(By.LINK_TEXT, "Create a List").click()

#-------------------------------------------------------------------------------------
# Question 8

# driver.get("https://www.w3schools.com/html/tryit.asp?filename=tryhtml_iframe")
# sleep(3)
## driver.switch_to.frame("iframeResult")

# driver.switch_to.frame(0)
# a = driver.find_element(By.TAG_NAME, "h1").text
#
# print("Heading:", a)

#-------------------------------------------------------------------------------------
# Question 9

# driver.get("https://www.amazon.com")
# sleep(3)
#
#
# search = driver.find_element(By.ID, "twotabsearchtextbox")
# search.send_keys("Laptop", Keys.ENTER)
#
# sleep(5)
#
#
# a= driver.find_elements(By.XPATH, "//h2//span")
#
# for i in a:
#     print(i.text)