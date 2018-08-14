#!/usr/bin/env python3
# -*- coding: utf-8 -*

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

def main():
    """ Abre o navegador Firefox utilizando selenium e
    navega para a página de login do gmail """

    fireforx_profile = webdriver.FirefoxProfile()
    fireforx_profile.set_preference(
        "general.useragent.override",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64)" +
        " AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.85 Safari/537.36")

    options = Options()
    options.set_headless(headless=False)

    driver = webdriver.Firefox(fireforx_profile, firefox_options=options)
    
    driver.get("http://mail.google.com")

if __name__ == "__main__":
    main()
