class Command:
    # menjalankan command dari app
    def RunningCommand(self, App):
        self.App = App
        self.CommandRun()
        
    # menjalankan program utama
    def CommandRun(self):
        self.App.Main.OS.system("clear")
        self.CommandDisplayMenu()
    
    # mengambil data menu
    def CommandGetMenu(self):
        f = open("./Txt/Menu.txt", "r")
        self.COMMAND_MENU = f.read()
        f.close()

    # menampilkan menu pilihan kepada user
    def CommandDisplayMenu(self):
        self.CommandGetMenu()
        MENU = input(self.COMMAND_MENU)
        self.MENU = int(MENU)
        self.CommandGetUserSelectMenu()
        
    # melakukan pengecekan menu yang dipilih pengguna
    def CommandGetUserSelectMenu(self):
        if self.MENU not in (1, 2, 3, 4, 5, 6, 0):
            self.CommandRun()
        elif self.MENU == 1:
            self.App.Main.HttpRunning(self)
        elif self.MENU == 2:
            self.App.Main.HttpsRunning(self)
        elif self.MENU == 3:
            self.App.Main.Host(self)
            self.App.Main.EnableHost()
        elif self.MENU == 4:
            self.App.Main.Host(self)
            self.App.Main.DisableHost()
        elif self.MENU == 5:
            self.App.Main.Host(self)
            self.App.Main.DeleteHost()
        elif self.MENU == 6:
            self.App.Main.OS.remove('.env')
            self.App.Main.ENV_FILE = False
            self.App.AppRun()
        else:
            self.App.AppConfirmBeforeExit()
        
    # input data http only
    def CommandInputOnlyHttp(self):
        self.FILENAME = input("Masukkan nama file host baru (tanpa .conf) >>> ")
        self.DIR = input("Masukkan direktori vhost >>> ")
        self.DOMAIN = input("Masukkan nama domain untuk vhost >>> ")
        self.ROOT = input("Masukkan lokasi dokumen root vhost >>> ")

    # input dibutuhkan jika https
    def CommandInputRequireIfHttps(self):
        self.SSL_FILE = input("Masukkan nama file ssl >>> ")
        self.SSL_KEY  = input("Masukkan nama file ssl key >>> ")
