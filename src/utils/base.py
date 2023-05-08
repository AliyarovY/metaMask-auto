from random import randint
from time import sleep

from utils import *
from functools import cached_property


class Base:
    headless = True

    def big_sleep(self):
        sleep_seconds = randint(4, 7)
        sleep(sleep_seconds)

    def small_sleep(self):
        sleep_seconds = randint(1, 3)
        sleep(sleep_seconds)


    @cached_property
    def driver(self):
        options = webdriver.ChromeOptions()
        if self.headless:
            options.add_argument("--headless")
        options.add_argument("start-maximized")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)

        service = Service(r'chromedriver.exe')
        driver = webdriver.Chrome(options=options, service=service)

        stealth(driver,
                languages=["en-US", "en"],
                vendor="Google Inc.",
                platform="Win32",
                webgl_vendor="Intel Inc.",
                renderer="Intel Iris OpenGL Engine",
                fix_hairline=True,
                )
        return driver
