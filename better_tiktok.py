import undetected_chromedriver.v2 as uc
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pyfiglet
from time import sleep
from os import system
vidUrl = input("Video Link: ")
def loop1():
    global i
    sleep(30)
    try:
        driver.find_element_by_xpath("//*[@id=\"main\"]/div/div[4]/div/button").click()
    except:
        print("You didn't solve the captcha yet. Need to refresh to avoid endless loop.")
        driver.maximize_window()
        driver.refresh()
        loop1()
    try:
        driver.minimize_window()
        sleep(2)
        driver.find_element_by_xpath("//*[@id=\"sid4\"]/div/div/div/form/div/input").send_keys(vidUrl)
        sleep(1)
        driver.find_element_by_xpath("//*[@id=\"sid4\"]/div/div/div/form/div/div/button").click()
        sleep(2)
        driver.find_element_by_xpath("//*[@id=\"c2VuZC9mb2xsb3dlcnNfdGlrdG9V\"]/div[1]/div/form/button").click()
        sleep(10)
        driver.refresh()
        i += 1
        total = i * 1000
        system("cls")
        print("Views success delivered! Total", total,"views")
        sleep(30)
        loop1()
    except:
        
        driver.refresh()
        sleep(20)
        loop1()

def loop2():
    sleep(10)
    try:
        driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[3]/div/div[2]/div/button").click()
    except:
        print("You didn't solve the captcha yet. Need to refresh to avoid endless loop.")
        driver.maximize_window()
        driver.refresh()
        loop2()
    try:
        driver.minimize_window()
        sleep(2)
        driver.find_element_by_xpath("/html/body/div[4]/div[3]/div/div/div/form/div/input").send_keys(vidUrl)
        sleep(1)
        driver.find_element_by_xpath("/html/body/div[4]/div[3]/div/div/div/form/div/div/button").click()
        sleep(10)
        driver.find_element_by_xpath("/html/body/div[4]/div[3]/div/div/div/div/div[1]/div/form/button").click()
        sleep(10)
        hearts = driver.find_element_by_xpath('//*[@id="c2VuZE9nb2xsb3dlcnNfdGlrdG9r"]/span').text
        sleep(55)
        print(hearts," Success delivered! Thank me with a $ 1 donation on GitHub")
        sleep(100)
        driver.refresh()
        sleep(200)
        loop2()
    except:
        print("A generic error occurred. Now will retry again")
        driver.refresh()
        sleep(355)
        loop2()

def loop3():
    sleep(10)
    try:
        driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[3]/div/div[3]/div/button").click()
    except:
        print("You didn't solve the captcha yet. Need to refresh to avoid endless loop.")
        driver.maximize_window()
        driver.refresh()
        loop2()
    try:
        driver.minimize_window()
        sleep(2)
        driver.find_element_by_xpath("/html/body/div[4]/div[4]/div/div/div/form/div/input").send_keys(vidUrl)
        sleep(1)
        driver.find_element_by_xpath("/html/body/div[4]/div[4]/div/div/div/form/div/div/button").click()
        sleep(5)
        driver.find_element_by_xpath("/html/body/div[4]/div[4]/div/div/div/div/div[1]/div/form/button").click()
        sleep(5)
        driver.find_element_by_xpath("/html/body/div[4]/div[4]/div/div/div/div/form/ul/li/div/button").click()
        sleep(47)
        driver.refresh()
        print("Success delivered! Thank me with a $ 1 donation on GitHub")
        loop3()
    except:
        print("A generic error occurred. Now will retry again")
        driver.refresh()
        sleep(50)
        loop3()

def loop4():
    sleep(20)
    wait_time = 660 #11 minutes
    try:
        driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[3]/div/div[1]/div/button").click() #Followers
    except:
        print("You didn't solve the captcha yet. Need to refresh to avoid endless loop.")
        driver.maximize_window()
        driver.refresh()
        
        
        loop4()
    try:
        driver.minimize_window()
        sleep(20)
        driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div/div/form/div/input").send_keys(vidUrl) #Write
        sleep(2)
        driver.find_element_by_xpath("//*[@id=\"sid\"]/div/div/div/form/div/div/button").click() #Search
        sleep(20)
        driver.find_element_by_xpath("//*[@id=\"c2VuZF9mb2xsb3dlcnNfdGlrdG9r\"]/div[1]/div/form/button").click() #AddFollowers
        sleep(wait_time/3)
        print("Success delivered!")
        sleep(wait_time/3)
        driver.refresh()
        sleep(wait_time/3)
        loop4()
    except:
        print("A generic error occurred. Now will retry again")
        driver.refresh()
        sleep(wait_time)
        loop4()

def loop5():
    sleep(20)
    try:
        driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[3]/div/div[5]/div/button").click()
    except:
        print("You didn't solve the captcha yet. Need to refresh to avoid endless loop.")
        driver.maximize_window()
        driver.refresh()
        loop5()
    try:
        driver.minimize_window()
        sleep(20)
        driver.find_element_by_xpath("/html/body/div[4]/div[6]/div/div/div/form/div/input").send_keys(vidUrl) # Write
        sleep(2)
        driver.find_element_by_xpath("/html/body/div[4]/div[6]/div/div/div/form/div/div/button").click() # Search
        sleep(20)
        driver.find_element_by_xpath("/html/body/div[4]/div[6]/div/div/div/div/div[1]/div/form/button").click() # AddShares
        sleep(60)
        print("Shares sent! ")
        sleep(1700)
    except:
        print("A generic error occurred. Now will retry again")
        driver.refresh()
        sleep(300)
        loop5()

def loop6():
    sleep(1000)
    driver.refresh()
    print("Reload")
    loop5()





bot = int(input("What do you want to do?\n1 - Auto views(1000)\n2 - Auto hearts\n3 - Auto (FIRST) comments heart\n4 - Auto followers\n5 - [NEW]Auto Share\n6 - Simple reload\n"))
i = 0

chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = uc.Chrome(chrome_options=chrome_options)

driver.get("https://vipto.de/")

if bot == 1:
    loop1()
elif bot == 2:
    loop2()
elif bot == 3:
    loop3()
elif bot == 4:
    loop4()
elif bot == 5:
    loop5()
elif bot == 6:
    loop5()
else:
    print("You can insert just 1, 2, 3, 4, 5 or 6")