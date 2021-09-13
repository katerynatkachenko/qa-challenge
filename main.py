from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import unittest
import warnings


class TestStringMethods(unittest.TestCase):

    def setUp(self):
        option = webdriver.ChromeOptions()
        option.add_argument('--disable-blink-features=AutomationControlled')

        self.driver = webdriver.Chrome(options=option)
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get("http://localhost:8080/")

    def tearDown(self):
        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)
        self.driver.close()

    def test_adding_new_customer(self):

        # Create a new customer:
        company_name = "Test"
        about_text = "test test test"

        # usually finding By.XPATH not a good a example to use, but since the elements have no id's
        # and the class names are dynamically generated, I've used the xpath approach

        add_customer_btn = self.driver.find_element(By.XPATH, "//*[@id=\"react-node\"]/div/div[1]/div[2]/div[2]")
        add_customer_btn.click()

        company = self.driver.find_element(By.XPATH, "//*[@id=\"react-node\"]/div/div[2]/div[1]/input")
        company.click()
        company.send_keys(company_name)

        industry = self.driver.find_element(By.XPATH, "//*[@id=\"react-node\"]/div/div[2]/div[2]/select")
        industry.click()
        industry.value_of_css_property("finance")

        active = self.driver.find_element(By.XPATH, "//*[@id=\"react-node\"]/div/div[2]/div[3]/input")
        active.click()

        about = self.driver.find_element(By.XPATH, "//*[@id=\"react-node\"]/div/div[2]/div[4]/textarea")
        about.click()
        about.send_keys(about_text)


        add = self.driver.find_element(By.XPATH, "//*[@id=\"react-node\"]/div/div[2]/div[6]/div")
        self.assertEqual(add.text, 'ADD')
        add.click()

if __name__ == '__main__':
    unittest.main()
