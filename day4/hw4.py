from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By

class Test_SauceHW:
    def __init__(self):
        self.driver=webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
        sleep(5)
        self.userName=self.driver.find_element(By.ID,"user-name")
        self.password=self.driver.find_element(By.ID,"password")  
        sleep(2)
        self.loginBtn=self.driver.find_element(By.ID,"login-button")
        sleep(2)
    def kullaniciAdıSifreBos(self):         
        self.userName.send_keys("")
        self.password.send_keys("") 
        sleep(2)        
        self.loginBtn.click()
        errorMessage=self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult=errorMessage.text=="Epic sadface: Username is required"
        print(f"TEST SONUCU: {testResult}")
        sleep(60)


    def SifreBos(self):
        self.userName.send_keys("abc")
        self.password.send_keys("") 
        sleep(2)
        self.loginBtn.click()
        errorMessage=self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult=errorMessage.text=="Epic sadface: Password is required"
        print(f"TEST SONUCU: {testResult}")
        sleep(60)
    
    def LockedAccount(self):
        self.userName.send_keys("locked_out_user")
        self.password.send_keys("secret_sauce") 
        sleep(2)
        self.loginBtn.click()
        errorMessage=self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult=errorMessage.text=="Epic sadface: Sorry, this user has been locked out."
        print(f"TEST SONUCU: {testResult}")
        sleep(60)

    def StandardAccount(self):
        self.userName.send_keys("standard_user")
        self.password.send_keys("secret_sauce") 
        sleep(2)
        self.loginBtn.click()
        self.driver.get("https://www.saucedemo.com/inventory.html")        
        sleep(60)    


myTestClass=Test_SauceHW()
#myTestClass.kullaniciAdıSifreBos()
#myTestClass.SifreBos()
#myTestClass.LockedAccount()
#myTestClass.StandardAccount()
while True:
    continue
        



