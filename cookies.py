from selenium import webdriver

CHROME_DRIVER_PATH = 'C:\\Users\\reach\\Desktop\\chromedriver.exe'


def get_cookies(url):
    """This function returns all the cookies in the given url.

    Arguments:
        url {string}: URL to save cookies from.
    """
    driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
    driver.get(url)
    return driver.get_cookies()


def load_cookies(url, cookies):
    """This function sets all the given cookies in the given url.

    Arguments:
        url {string}: URL to save cookies from.
        cookies {list}: cookies to set.
    """
    driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
    driver.get(url)
    print('Before setting: ', driver.get_cookies())
    for cookie in cookies:
        driver.add_cookie({'name' : cookie['name'], 'value' : cookie['value']})
    print('\nAfter setting: ', driver.get_cookies())


if __name__ == "__main__":
    url = input("Enter URL to get cookies from: ").strip()
    # First get cookies for the given url
    cookies = get_cookies(url)
    print('Cookies got:', cookies)
    url = input("Enter URL to set cookies on: ").strip()
    # Load the cookies
    load_cookies(url, cookies)