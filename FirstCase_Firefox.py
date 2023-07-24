from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

options = Options()
options.binary_location = r"D:\Ananth\Udemy\geckodriver.exe"
driver = Firefox(options=options, executable_path=r"D:\Ananth\Udemy\geckodriver.exe")

#path = "D:\\Ananth\\Udemy\\geckodriver.exe"
#driver = Firefox(executable_path = path)

driver.get("https://thetestingworld.com/index.php?option=com_formmaker&view=formmaker&id=2&Itemid=657")

# maximize_browser
driver.maximize_window()

# Enter data to text box

driver.find_element(By.XPATH, "//input[@id='wdform_1_element_first2']").send_keys("Ananth")
driver.find_element(By.XPATH, "//input[@id='wdform_1_element_last2']").send_keys("Kamaraj")
driver.find_element(By.XPATH, "//input[@id='wdform_2_element2']").send_keys("ananthsct@gmail.com")
driver.find_element(By.XPATH, "//input[@id='wdform_1_element_first2']").clear()
driver.find_element(By.XPATH, "//input[@id='wdform_1_element_first2']").send_keys("Ananth2")
driver.find_element(By.XPATH, "//button[contains(text(),'Reset')]").click()

obj = Select(driver.find_element(By.XPATH, "//select[@id='wdform_5_element2']"))
obj.select_by_value("Selenium ")

time.sleep(2)
