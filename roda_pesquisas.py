from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import sys
sys.path.insert(0, sys.path[0] + "/html_scanner")
from html_scanner import extract_info
import json
import time
import datetime
import requests
import os

def google_search(driver, query):
    baseLink = "https://www.google.com/search?q="

    driver.get(baseLink + query)

    return driver.page_source

def gmail_sign_in(driver, profile):
    driver.get("http://mail.google.com")

    emailid = driver.find_element_by_id("identifierId")
    emailid.send_keys(profile["login"])

    nxt = driver.find_element_by_id("identifierNext")
    nxt.click()

    time.sleep(5)

    passw = driver.find_element_by_name("password")
    passw.send_keys(profile["password"])

    nxt = driver.find_element_by_id("passwordNext")
    nxt.click()

    time.sleep(5)

if __name__ == "__main__":
    firefoxProfile = webdriver.FirefoxProfile()
    firefoxProfile.set_preference("general.useragent.override", "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.85 Safari/537.36")    
    
    options = Options()
    options.set_headless(headless=True)

    with open("profiles.json") as profilesFile: 
        profiles = json.load(profilesFile)

        for profile in profiles:
            driver = webdriver.Firefox(firefoxProfile, firefox_options=options)
            
            if profile["login"] != "":
                gmail_sign_in(driver, profile)

            with open("actors/actors.json") as actors:
                buscas = json.load(actors)
                for busca in buscas["atores"]:
                    googleHtml = google_search(driver, busca)
                    jsonData = extract_info(googleHtml)
                    jsonData["data"] = str(datetime.date.today())
                    jsonData["ator"] = busca
                    jsonData["perfil"] = profile["login"]
                    requests.post(os.environ["POST_URL"], json=jsonData)
            driver.close()
