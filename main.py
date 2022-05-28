import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


# option to be kept open
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()), options=chrome_options
)
driver.get("https://nomadcoders.co")
driver.maximize_window()

sizes = [320, 480, 720, 1024, 1440]

height = driver.get_window_size()["height"]  # 790

for size in sizes:
    driver.set_window_size(size, height)
    time.sleep(1.5)
