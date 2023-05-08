import time

from utils import MetaMaskWorker, airdrop_connect


def main():
    worker = MetaMaskWorker()

    worker.extension_add()

    worker.driver.close()
    windows = worker.driver.window_handles
    worker.driver.switch_to.window(windows[-1])

    worker.extension_connect()

    worker.load_url()
    worker.con_met_ext()

    worker.change_network()
    worker.change_currency()
    worker.change_account()

    airdrop_connect(worker)

    worker.con_met_ext(exstantion_only=True)


if __name__ == '__main__':
    main()
    input()
