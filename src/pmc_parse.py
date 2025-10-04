from bs4 import BeautifulSoup
from selenium import webdriver # Using Selenium because Cloudflare blocks get requests
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from os import path # For path.devnull

def scrape_texturepack(URL: str) -> dict:
    """
    Takes a Texturepack url from Planet Minecraft, grab the creators
    username, pack description and pics
    :param URL: Planet Minecraft URL
    :returns: dict with `username` `description` and `pictures`
    """

    # We must use Selenium because javascript loads the images, cloudscraper didnt work...
    service = Service(log_path=path.devnull)

    driver = webdriver.Firefox(service=service)
    driver.get(URL)
    
    wait = WebDriverWait(driver, 20)

    # Hover over the slides to show the button
    element_to_hover = wait.until(EC.presence_of_element_located((By.ID, "lg-inner-1")))
    hover = ActionChains(driver).move_to_element(element_to_hover)
    hover.perform()

    # Get amount of slides from counter at the top left
    slide_count_element = wait.until(EC.presence_of_element_located((By.ID, "lg-counter-all-1")))
    slide_count = int(slide_count_element.text.strip())

    imgs = []

    for i in range(slide_count):
        # Get img src that is nested inside lg-current
        img_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".lg-current img")))
        imgs.append(img_element.get_attribute("src"))

        if i < slide_count - 1:
            button = wait.until(EC.element_to_be_clickable((By.ID, "lg-next-1")))
            button.click()
            time.sleep(0.5)

    # Get webpage html for lazy way of getting username and description ( Maybe in the future I will change for pure selenium )
    html_str = driver.page_source
    
    driver.close()

    soup = BeautifulSoup(html_str, 'html.parser')
    username = soup.find(class_="pusername").get_text()
    description = soup.find(id="r-text-block").get_text()


    return {"username":username, "description":description, "pictures":imgs}