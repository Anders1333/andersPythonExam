# Retrieve images from a google search
# GET: ?q=search+terms
# &tbm=isch <- Images Search
# &source=lnms
# &sa=X

import os, time
from urllib import request as req

# import necessary Selinium methods and classes for automatic web browsing
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def init_selenium():
    '''
    Initialize the Selinium webdriver as a  Chrome based headless browser
    :return: Returns the webdriver
    '''
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox') # needed if running as root user to avoid no-sandbox errors
    chrome_options.add_argument("--window-size=1920x1080")

    chrome_driver = webdriver.Chrome(options=chrome_options, service_args=['--verbose', '--log-path=/tmp/chromedriver.log'])

    return chrome_driver


def image_download(source, path):
    if not os.path.isfile(path):
        req.urlretrieve(source, path)

def image_search(search_terms, dir, return_amount=100):
    '''
    :param search_terms:
    :param dir: Download Directory - where the images are stored
    :param return_amount: Max amount of images to return/download - defaults to 100
    :return: Returns True when complete
    '''
    terms = search_terms.replace(" ", "+")
    # URL for Google image-search - "tbm=isch" sets method as ImagesSearCH
    url = 'https://www.google.dk/search?tbm=isch&sa=X&source=lnms&q=' + terms

    driver = init_selenium() # initialize headless webbrowser
    wait = WebDriverWait(driver, 7) # Allows the webdriver to wait for 7 seconds before continueing

    driver.get(url)
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'y yf'))) # <div ... class="y yf" ...> Holds found images

    for i in range(5):
        time.sleep(2)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)") # Scroll to bottom of page

    image_holder = driver.find_element_by_id('search')
    images = image_holder.find_elements_by_tag_name("img")

    images_found = len(images)

    i = 0

    print("Downloading images to " + dir + " ...")

    for image in images: # Download all images found but a maximum of 'return_amount'
        i += 1
        source = image.get_property('src')
        path = dir + str(i) + ".jpg" # All images are forcebly downloaded as JPEG

        try:
            image_download(source, path)

        except:
            i -= 1
            continue

        if i >= return_amount or i == images_found:
            break

    return True

# Search parameters & testdata folders

testdata_params = {
    'necrotic': ['necrotic wound human skin', "testdata/necrosis/"],
    'fibrin': ['sår med fibrin', "testdata/fibrin/"],
    'superficial': ['overfladiske sår hud', "testdata/superficial/"]
}