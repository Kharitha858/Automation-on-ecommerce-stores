from selenium.webdriver.common.by import By

class Loginpage:
    textbox_useremail_id="CustomerEmail"
    textbox_password_id="CustomerPassword"
    button_login_xpath='//div//button[@id="customer-login-submit"]'

    def __init__(self,driver):
        self.driver = driver

    def setuseremail(self,useremail):
        self.driver.find_element(By.ID, self.textbox_useremail_id).clear()
        self.driver.find_element(By.ID,self.textbox_useremail_id).send_keys(useremail)

    def setpassword(self,password):
        self.driver.find_element(By.ID,self.textbox_password_id).clear()
        self.driver.find_element(By.ID,self.textbox_password_id).send_keys(password)

    def clicklogin(self):
        self.driver.find_element(By.XPATH,self.button_login_xpath).click()

