import os, time
from urllib import request as req

# import necessary Selinium methods and classes for automatic web browsing
from selenium import webdriver   # To launch browser
from selenium.webdriver.common.by import By # Search by specific parameters
from selenium.webdriver.support.ui import WebDriverWait # Allows waiting
from selenium.webdriver.support import expected_conditions as EC # Specify what to look for to determine load is done


    
    

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

def imageScrape(term, directory, amount):
   
    
    url = 'https://www.google.dk/search?tbm=isch&sa=X&source=lnms&q=' + term
    print('searching for pictures of : ' + term)

    driver = init_selenium() # driver init
    wait = WebDriverWait(driver, 7)  #  OBS new addition!

    driver.get(url)
    wait.until(EC.element_to_be_clickable((By.ID, 'search'))) # OBS new addition!

    for i in range(5):
        time.sleep(2)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    image_holder = driver.find_element_by_id('search')
    images = image_holder.find_elements_by_tag_name("img")

    images_found = len(images)
    print('Found ' + images_found)

    i = 0

    directory = "testdir"
    print("Downloading images to " + directory + " ...")

    for image in images: 
        i += 1
        source = image.get_property('src')
        path = directory + str(i)

        try:
            image_download(source, path)

        except:
            i -= 1
            continue

        if i >= amount or i == images_found:
            break

    return "Done"



if __name__ == "__main__":


 imageScrape('necrosis','standardDirectory',amount=10)     #necrosis , directory , amount = 10