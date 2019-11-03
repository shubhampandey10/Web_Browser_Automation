import time
from selenium import webdriver

CHROME_DRIVER_PATH = "C:\\Users\\reach\\Desktop\\chromedriver.exe"


def click_first_show():
    """Click first show on sonyliv"""
    driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
    driver.maximize_window()
    driver.get("https://sonyliv.com")

    try:
        driver.find_element_by_xpath("//button[@id='wzrk-cancel']").click()
    except:
        pass

    time.sleep(2)
    driver.find_element_by_xpath(
        "//div[@class='navbar-left menuDesktop']//span[@class='menu-text "
        "ng-binding'][contains(text(),'Shows')]").click()
    time.sleep(2)
    driver.find_element_by_xpath(
        "//div[@class='navbar-left menuDesktop']//span[@class='menu-text "
        "ng-binding'][contains(text(),'SONY TV SHOWS')]").click()
    time.sleep(2)
    driver.find_element_by_xpath(
        "//li[1]//tile-vid-01[1]//div[1]//a[1]").click()
    time.sleep(60)


if __name__ == "__main__":
    click_first_show()
