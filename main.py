from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

service = Service(r"C:\Users\hen gabay\Desktop\chromedriver.exe")
driver = webdriver.Chrome(service=service)

TCB_USERNAME = ""
TCB_PASSWORD = ""

class LoginToTcb:
    def login_step_1(self):
        driver.get("https://login.tcb.ac.il/nidp/saml2/sso?id=tcbloa2&sid=1&option=credential&sid=1")
        time.sleep(5)
        username = driver.find_element(By.ID,"Ecom_User_ID")
        username.send_keys(TCB_USERNAME)
        username.send_keys(Keys.ENTER)
        time.sleep(5)


    def login_step_2(self):
        time.sleep(2)
        link = driver.find_element(By.ID,"ldapPasswordCardClick")
        link.click()


    def login_step_3(self):
        time.sleep(5)
        password = driver.find_element(By.ID, "ldapPassword")
        password.send_keys(TCB_PASSWORD)
        password.send_keys(Keys.ENTER)
        time.sleep(5)


class LinkedInJobs:
    def login_linkedin(self):
        driver.get("https://www.linkedin.com/checkpoint/rm/sign-in-another-account")
        time.sleep(5)
        username = driver.find_element(By.ID, "username")
        password = driver.find_element(By.ID,"password")

        username.send_keys("")
        password.send_keys("")
        password.send_keys(Keys.ENTER)

        time.sleep(3)

        driver.get("")

        time.sleep(10)


# tcb = LoginToTcb()
# tcb.login_step_1()
# tcb.login_step_2()
# tcb.login_step_3()


linked = LinkedInJobs()
linked.login_linkedin()
