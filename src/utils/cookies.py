import json

from utils import *


class CookiesMixin:
    cookies_path = None
    driver = None

    def dump_cookies(self):
        cookies = self.driver.get_cookies()
        with open(self.cookies_path, 'w') as file:
            json.dump(cookies, file)

    def add_cookies(self):
        with open(self.cookies_path, 'r') as file:
            cookies = json.load(file)
            for cookie in cookies:
                self.driver.add_cookie(cookie)
            self.driver.refresh()
