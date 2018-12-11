# Retrieve images from a google search
# GET: ?q=search+terms
# &tbm=isch <- Images Search
# &source=lnms
# &sa=X

import os, time

from urllib import request as req

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def init_selenium():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox') # needed if running as root user to avoid no-sandbox errors
    chrome_options.add_argument("--window-size=1920x1080")

    chrome_driver = webdriver.Chrome(options=chrome_options, service_args=['--verbose', '--log-path=/tmp/chromedriver.log'])

    return chrome_driver


def image_download(source, path):
    if not os.path.isfile(path):
        req.urlretrieve(source, path)

def image_search(search_terms, return_amount, dir):
    terms = search_terms.replace(" ", "+")
    url = 'https://www.google.dk/search?tbm=isch&sa=X&source=lnms&q=' + terms

    driver = init_selenium()
    wait = WebDriverWait(driver, 7)

    driver.get(url)
    wait.until(EC.element_to_be_clickable((By.ID, 'search')))

    for i in range(5):
        time.sleep(2)
        driver.execute_script('return arguments[0].scrollIntoView();',
                                     driver.find_element_by_tag_name("body"))

    image_holder = driver.find_element_by_id('search')
    images = image_holder.find_elements_by_tag_name("img")

    images_found = len(images)

    i = 0

    print("Downloading images to " + dir + " ...")

    for image in images:
        i += 1
        source = image.get_property('src')
        path = dir + str(i) + ".jpg"

        try:
            image_download(source, path)

        except:
            continue

        if i >= return_amount or i == images_found:
            break


