from dataclasses import dataclass
from time import sleep

from utils import *
from config import SECOND_METAMASK_ID, METAMASK_SECRET_WORD, METAMASK_PASSWORD


class UrlLoader(Base):
    url = 'https://portfolio.metamask.io/'

    def load_url(self):
        self.driver.get(self.url)
        self.big_sleep()

    def con_met_ext(self, exstantion_only=False):
        if not exstantion_only:
            xpath = '//span[text()="Connect MetaMask"]'
            self.driver.find_element(By.XPATH, xpath).click()
            self.small_sleep()

        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])
        self.small_sleep()

        xpath = '//div[@class="permissions-connect-choose-account__bottom-buttons"]/button[@class="button btn--rounded btn-primary"]'
        self.driver.find_element(By.XPATH, xpath).click()
        self.small_sleep()

        xpath = '//button[@data-testid="page-container-footer-next"]'
        self.driver.find_element(By.XPATH, xpath).click()
        self.small_sleep()

        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[0])
        self.small_sleep()

        self.big_sleep()


class Loginner(Base):
    def login(self, acc_id=SECOND_METAMASK_ID):
        # enter acc id
        css = '[placeholder="Wallet address or ENS name"]'
        self.driver.find_element(By.CSS_SELECTOR, css).send_keys(acc_id)
        self.small_sleep()
        # click "import" button
        xpath = "//span[text()='Import']"
        self.driver.find_element(By.XPATH, xpath).click()

        self.big_sleep()

    def change_account(self, changed_acc_id=SECOND_METAMASK_ID):
        # click on button for show account
        xpath = "//div[@id='accounts-multi-dropdown']//span[@id='account-multi-name']"
        self.driver.find_element(By.XPATH, xpath).click()
        self.small_sleep()

        # "Add another account" button click
        xpath = "//div[text()='Add another account']"
        self.driver.find_element(By.XPATH, xpath).click()
        self.small_sleep()

        self.login(changed_acc_id)


@dataclass
class NotworkChanger(Base):
    network_name: str = 'Polygon'

    def change_network(self):
        # click on button for show networks
        xpath = "//div[@id='networks-multi-dropdown']/div[1]/button"
        self.driver.find_element(By.XPATH, xpath).click()
        self.small_sleep()
        # choose network
        xpath = f"//span[text()='{self.network_name}']"
        self.driver.find_element(By.XPATH, xpath).click()

        self.small_sleep()


class CurrencyChanger(Base):
    def change_currency(self, currency_name: str = 'EUR'):
        currency_name = currency_name.strip().upper()

        # click on button for show currencies
        xpath = "//div[@class='sm:flex hidden']/div[@class='relative']/button"
        self.driver.find_element(By.XPATH, xpath).click()
        self.small_sleep()
        # choose currency
        xpath = f"//span[text()='{currency_name}']"
        self.driver.find_element(By.XPATH, xpath).click()

        self.small_sleep()


class MetaMaskExtension(ExtensionMixin):
    def extension_connect(self):
        # for metamask connect button
        xpath = '//button[@data-testid="onboarding-import-wallet"]'
        self.driver.find_element(By.XPATH, xpath).click()

        # agree button
        xpath = '//button[@data-testid="metametrics-i-agree"]'
        self.driver.find_element(By.XPATH, xpath).click()

        self.small_sleep()

        # secret word send
        for i, word in enumerate(METAMASK_SECRET_WORD.split()):
            xpath = f'//input[@id="import-srp__srp-word-{i}"]'
            self.driver.find_element(By.XPATH, xpath).send_keys(word)
            self.small_sleep()

        # confirm
        xpath = '//button[@data-testid="import-srp-confirm"]'
        self.driver.find_element(By.XPATH, xpath).click()

        self.small_sleep()

        # set password
        # firs pass
        xpath = '//input[@data-testid="create-password-new"]'
        self.driver.find_element(By.XPATH, xpath).send_keys(METAMASK_PASSWORD)
        self.small_sleep()
        # second pass
        xpath = '//input[@data-testid="create-password-confirm"]'
        self.driver.find_element(By.XPATH, xpath).send_keys(METAMASK_PASSWORD)
        self.small_sleep()
        # agree
        xpath = '//input[@data-testid="create-password-terms"]'
        self.driver.find_element(By.XPATH, xpath).click()
        self.small_sleep()
        # confirm
        xpath = '//button[@data-testid="create-password-import"]'
        self.driver.find_element(By.XPATH, xpath).click()
        self.small_sleep()

        # complete buttons
        xpath = '//button[@data-testid="onboarding-complete-done"]'
        self.driver.find_element(By.XPATH, xpath).click()
        self.small_sleep()
        xpath = '//button[@data-testid="pin-extension-next"]'
        self.driver.find_element(By.XPATH, xpath).click()
        self.small_sleep()
        xpath = '//button[@data-testid="pin-extension-done"]'
        self.driver.find_element(By.XPATH, xpath).click()
        self.small_sleep()

        # fin
        xpath = '//button[text()="Enable security alerts"]'
        self.driver.find_element(By.XPATH, xpath).click()

        self.small_sleep()


class MetaMaskWorker(
    UrlLoader,
    Loginner,
    NotworkChanger,
    CurrencyChanger,
    MetaMaskExtension
):
    headless = False
