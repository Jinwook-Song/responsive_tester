import time
import math

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
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
    driver.execute_script("window.scrollTo(0, 0)")
    time.sleep(1.5)
    # return JS -> Python
    scroll_size = driver.execute_script("return document.body.scrollHeight")
    total_sections = math.ceil(scroll_size / height)
    for section in range(total_sections + 1):
        driver.execute_script(f"window.scrollTo(0, {(section) * height})")
        driver.save_screenshot(f"screenshots/{size}_{section}.png")
        time.sleep(0.5)
