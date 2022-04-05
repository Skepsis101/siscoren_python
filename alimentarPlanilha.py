import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import json

url = "https://www.portalcoren-rs.gov.br/novoadmin/index.php?pagina=agendamentos"

option = Options()
option.headless = True
driver = webdriver.Firefox()

driver.find_element_by_class_name(
    "//table[@class='table table-striped table-hover table-bordered']//tbody/tr/td")

driver.get(url)
time.sleep(10)


driver.quit()
