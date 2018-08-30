""" Abre o navegador Firefox utilizando selenium e realiza uma lista de buscas
    no google em uma série de contas do gmail e salva os resultados destas buscas
    em um banco de dados """
#!/usr/bin/env python3
# -*- coding: utf-8 -*

import os
import sys
import json
import time
import datetime
from random import shuffle
import requests
import actors_list
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
sys.path.insert(0, sys.path[0] + "/html_scanner")
from html_scanner import extract_info

def google_search(driver, query):
    """ Navega driver para a página com resultado da pesquisa no google do termo query """
	
    base_link = "https://www.google.com/search?q="
    driver.get("https://www.google.com")
    driver.get(base_link + query)

    return driver.page_source

def gmail_sign_in(driver, profile):
    """ Navega driver para a página do gmail e realiza o login na conta especificada por profile """

    driver.get("http://mail.google.com")

    email_id = driver.find_element_by_id("identifierId")
    email_id.send_keys(profile["login"])

    nxt = driver.find_element_by_id("identifierNext")
    nxt.click()

    time.sleep(5)

    passw = driver.find_element_by_name("password")
    passw.send_keys(profile["password"])

    nxt = driver.find_element_by_id("passwordNext")
    nxt.click()

    time.sleep(5)

def main():
    """ Abre o navegador Firefox utilizando selenium e realiza uma lista de buscas
     no google em uma série de contas do gmail """

    fireforx_profile = webdriver.FirefoxProfile()
    fireforx_profile.set_preference(
        "general.useragent.override",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64)" +
        " AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.85 Safari/537.36")

    options = Options()
    options.set_headless(headless=False)
    
    profile_list = []

    with open("profiles.json") as profiles_file:
        profiles = json.load(profiles_file)
        for profile in profiles:
            profile_list.append(profile)

    shuffle(profile_list)

    for profile in profile_list:
        driver = webdriver.Firefox(fireforx_profile, firefox_options=options)
        
        if profile["login"] != "":
            gmail_sign_in(driver, profile)
        buscas = actors_list.retrieve_actors()
        for busca in buscas:
            google_html = google_search(driver, busca)
            json_data = extract_info(google_html)
            json_data["data"] = str(datetime.date.today())
            json_data["ator"] = busca
            json_data["perfil"] = profile["login"]
            requests.post(os.environ["POST_URL"], json=json_data)
        driver.close()

if __name__ == "__main__":
    main()
