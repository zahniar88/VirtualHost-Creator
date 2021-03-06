import os
from dotenv import load_dotenv
from Qonita.App import App
from Qonita.Configure import Configure
from Qonita.Command import Command
from Qonita.HttpConfig import HttpConfig
from Qonita.HttpsConfig import HttpsConfig
from Qonita.HostConfig import HostConfig
load_dotenv()

# mendifinisikan Class Main
class Main(App, Configure, Command, HttpConfig, HttpsConfig, HostConfig):
    def __init__(self):
        self.OS = os
        # .env configure
        self.CURRENT_DIR = os.path.dirname(os.path.realpath(__file__)) + "/"
        self.ENV_FILE = os.path.exists(self.CURRENT_DIR + ".env")
        
        if self.ENV_FILE:
            self.DEFAULT_DIR = os.getenv("DEFAULT_DIR") + "/"
            self.DEFAULT_USER = os.getenv("DEFAULT_USER")
            self.DEFAULT_SSL_LOCATION = os.getenv("DEFAULT_SSL_LOCATION") + "/"
        
        self.AppRunnning(self)
        
# inisialisasi class main
Main()
