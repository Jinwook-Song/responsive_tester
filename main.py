import time
import math

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

# Check Lists
sizes = [480, 960, 1440]

# Device screen height 790
height = driver.get_window_size()["height"]

for size in sizes:
    driver.set_window_size(size, height)
    time.sleep(1.5)
    # return JS -> Python
    scroll_size = driver.execute_script("return document.body.scrollHeight")
    total_sections = math.ceil(scroll_size / height)
    for section in range(total_sections):
        driver.execute_script(f"window.scrollTo(0, {(section + 1) * height})")
        time.sleep(1)
