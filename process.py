from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Set up the web driver (e.g., for Chrome)
options = webdriver.ChromeOptions() 
options.add_argument("user-data-dir=C:\\\\Users\\Robin\\AppData\\Local\\Google\\Chrome\\User Data")
driver = webdriver.Chrome(executable_path="D:\\\\Documenti2\\temp\\chromedriver.exe", chrome_options=options)
#driver = webdriver.Chrome('/path/to/chromedriver')

# Load the form URL
driver.get('https://animebracket.com/me/process/epic-seven-best-waifu-contest-2023/nominations/')
time.sleep(2)

try:
    for i in range(201):
        try:
            time.sleep(1)
            
            button1 = driver.find_element(By.XPATH, '/HTML[1]/BODY[1]/DIV[1]/DIV[1]/DIV[1]/DIV[1]/FORM[1]/DIV[1]/BUTTON[1]')
            button1.click()
            time.sleep(1)

            try:
                button2 = driver.find_element(By.XPATH, '/HTML[1]/BODY[1]/DIV[1]/DIV[1]/DIV[2]/DIV[1]/DIV[2]/DIV[1]/BUTTON[1]')
                button2.click()
                time.sleep(1)
            except:
                button2 = driver.find_element(By.XPATH, '/HTML[1]/BODY[1]/DIV[1]/DIV[1]/DIV[3]/DIV[1]/DIV[2]/DIV[1]/BUTTON[1]')
                button2.click()
                time.sleep(1)

            button3 = driver.find_element(By.XPATH, '/HTML[1]/BODY[1]/DIV[1]/DIV[1]/DIV[1]/DIV[1]/FORM[1]/DIV[2]/DIV[4]/BUTTON[1]')
            button3.click()
            time.sleep(1)
        
        except:
            print("Error")
except:
    print("Exiting")
    
    
# Close the browser after completing the iterations
driver.quit()
