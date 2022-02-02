from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/explicit_wait2.html"
browser.get(link)
# говорим Selenium проверять в течение 12 секунд, пока цена не станет $100
WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
# нажимаем на кнопку book
browser.find_element(By.ID, "book").click()
# вычисляем функцию, печатаем х (для себя)
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
print(x)
# вычисляем y и вставляем значение в поле
y = calc(x)
browser.find_element(By.CSS_SELECTOR, "input#answer.form-control").send_keys(y)
# нажимаем на кнопку
browser.find_element(By.ID, "solve").click()
# печатаем число из модального окна в консоль
print(browser.switch_to.alert.text)
# закрываем браузер после всех манипуляций
browser.quit()
