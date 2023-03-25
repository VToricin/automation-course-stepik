from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

driver = webdriver.Chrome()
link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"

def form_check(self, link):
    driver.get(link)

    first_element = driver.find_element(By.XPATH, "//div[@class = 'first_block']//input[@class = 'form-control first']")
    first_element.send_keys("Махмуд")

    second_element = driver.find_element(By.XPATH, "//div[@class = 'first_block']//input[@class = 'form-control second']")
    second_element.send_keys("Семенов")

    third_element = driver.find_element(
        By.XPATH, "//div[@class = 'first_block']//input[@class = 'form-control third']")
    third_element.send_keys("Uzbekistan")

    # Отправляем заполненную форму
    button = driver.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = driver.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text
    text_to_check = "Congratulations! You have successfully registered!"
    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    self.assertEqual(text_to_check, welcome_text, "Не прошло чего-то")

class LessonUTest(unittest.TestCase):
    def test_first_form(self):
        form_check(self, link1)
        
    def test_second_form(self):
        form_check(self, link2)    
        
             

if __name__ == "__main__":
    unittest.main()
