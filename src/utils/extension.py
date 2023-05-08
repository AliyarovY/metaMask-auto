from utils import *
from config import METAMASK_EXTENSION_PATH

from selenium import webdriver


class ExtensionMixin(Base):
    extension_paths = [METAMASK_EXTENSION_PATH]

    def extension_add(self):
        for extension_path in self.extension_paths:
            options = self.driver.create_options()
            options.add_extension(extension_path)

            self.driver = webdriver.Chrome(options=options, service=self.driver.service)
            self.big_sleep()
