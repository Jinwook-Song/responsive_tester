import time
import math

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


class ResponsiveTester:
    def __init__(self, urls):
        self.chrome_options = Options()
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
        )
        self.driver.maximize_window()

        self.urls = urls
        # Check Lists
        self.sizes = [480, 960, 1440]
        # Device screen height 790
        self.height = self.driver.get_window_size()["height"]

    def screenshots(self, url):
        self.driver.get(url)
        for size in self.sizes:
            self.driver.set_window_size(size, self.height)
            self.driver.execute_script("window.scrollTo(0, 0)")
            time.sleep(1.5)
            # return JS -> Python
            scroll_size = self.driver.execute_script(
                "return document.body.scrollHeight"
            )
            total_sections = math.ceil(scroll_size / self.height)
            for section in range(total_sections + 1):
                self.driver.execute_script(
                    f"window.scrollTo(0, {(section) * self.height})"
                )
                self.driver.save_screenshot(f"screenshots/{size}_{section}.png")
                time.sleep(0.5)

    def start(self):
        for url in self.urls:
            self.screenshots(url)

        self.driver.quit()


tester = ResponsiveTester(["https://nomadcoders.co"])
tester.start()
