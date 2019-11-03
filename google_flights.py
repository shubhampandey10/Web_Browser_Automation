import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

CHROME_DRIVER_PATH = 'C:\\Users\\reach\\Desktop\\chromedriver.exe'


def get_data(origin, destination, depart_date, return_date):
    """Function to get data from google flights

    Arguments:
        origin {string}: origin place
        destination {string}: destination place
        depart_date {string}: departure date
        return_date {string}: return date
    """
    driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
    driver.maximize_window()

    driver.get("https://www.google.com/flights?hl=en")

    driver.find_element_by_xpath(
        "//div[@class='flt-input gws-flights-form__input-container "
        "gws-flights__flex-box "
        "gws-flights-form__airport-input "
        "gws-flights-form__swapper-right']").click()
    driver.find_element_by_xpath("//input[@placeholder='Where from?']").clear()
    time.sleep(1)
    driver.find_element_by_xpath(
        "//input[@placeholder='Where from?']").send_keys(origin)
    time.sleep(1)
    driver.find_element_by_xpath(
        "//input[@placeholder='Where from?']").send_keys(Keys.ENTER)
    time.sleep(1)
    driver.find_element_by_xpath(
        "//div[@class='flt-input gws-flights-form__input-container "
        "gws-flights__flex-box gws-flights-form__airport-input "
        "gws-flights-form__empty gws-flights-form__swapper-left']").click()
    time.sleep(1)
    driver.find_element_by_xpath(
        "//input[@placeholder='Where to?']").send_keys(destination)
    time.sleep(1)
    driver.find_element_by_xpath(
        "//input[@placeholder='Where to?']").send_keys(Keys.ENTER)
    time.sleep(1)
    driver.find_element_by_xpath(
        "//div[@class='flt-input gws-flights__flex-box gws-flights__flex-filler"
        " gws-flights-form__departure-input gws-flights-form__round-trip']"
        "//div[@class='gws-flights__flex-filler "
        "gws-flights__ellipsize gws-flights-form__input-target']").click()
    time.sleep(1)
    driver.find_element_by_xpath(
        "//input[@placeholder='Departure date']").send_keys(depart_date)
    time.sleep(1)
    driver.find_element_by_xpath(
        "//input[@placeholder='Return date']").click()
    time.sleep(1)
    driver.find_element_by_xpath(
        "//input[@placeholder='Return date']").send_keys(return_date)
    time.sleep(1)
    driver.find_element_by_xpath(
        "//div[@class='eE8hUfzg9Na__overlay']").click()
    time.sleep(60)


if __name__ == "__main__":
    orig = input("Enter the source city: ").strip()
    dest = input("Enter the destination city: ").strip()
    dep = input("Enter the departure date (DD/MM/YYY): ").strip()
    ret = input("Enter the return date (DD/MM/YYY): ").strip()

    get_data(orig, dest, dep, ret)
