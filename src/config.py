import os

from dotenv import load_dotenv


env_path = 'D:\Pycharm\pythonProject\WebAuto\.env'
load_dotenv(dotenv_path=env_path)

METAMASK_EXTENSION_PATH = os.getenv('METAMASK_EXTENSION_PATH')
SECOND_METAMASK_ID = os.getenv('SECOND_METAMASK_ID')
METAMASK_SECRET_WORD = os.getenv('METAMASK_SECRET_WORD')
METAMASK_PASSWORD = os.getenv('METAMASK_PASSWORD')
