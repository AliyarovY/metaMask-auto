from utils import *
from config import METAMASK_EXTENSION_PATH


def airdrop_connect(Worker):
    worker = Worker
    worker.driver.get('https://app.airdrop-hunter.site/')
    worker.big_sleep()

    # metamask connect
    xpath = "//div[text()='MetaMask']"
    worker.driver.find_element(By.XPATH, xpath).click()
    worker.small_sleep()
