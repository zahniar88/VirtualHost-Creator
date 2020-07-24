class HttpsConfig:
    # menjalankan konfigurasi HttpsConfig secara umum
    def HttpsRunning(self, Command):
        self.Command = Command
        self.HttpsRun()
        
    # menjalankan program utama HttpsConfig
    def HttpsRun(self):
        self.Command.App.Main.OS.system("clear")
        self.Command.CommandInputOnlyHttp()
        self.Command.CommandInputRequireIfHttps()
        self.HttpsConfirmBeforeCreate()
    
    # mengambil contoh data Https
    def HttpsGetFileText(self):
        f = open(self.Command.App.Main.CURRENT_DIR + "Txt/Https.txt", "r")
        self.FILE_HTTPS = f.read()
        f.close()
        
    # mengubah isi contoh data menjadi data yang telah di input
    def HttpsChangeFileText(self):
        self.HttpsGetFileText()
        C1 = self.FILE_HTTPS.replace("#DIR#", self.Command.DIR)
        C2 = C1.replace("#DOMAIN#", self.Command.DOMAIN)
        C3 = C2.replace("#ROOT#", self.Command.ROOT)
        C4 = C3.replace(
            "#SSLFILE#", 
            self.Command.App.Main.DEFAULT_SSL_LOCATION + 
            self.Command.SSL_FILE
            )
        self.HTTPS_HAS_CHANGE = C4.replace(
            "#SSLKEY#", 
            self.Command.App.Main.DEFAULT_SSL_LOCATION +
            self.Command.SSL_KEY
            )
        
    # konfirmasi data sebelum di buat
    def HttpsConfirmBeforeCreate(self):
        self.Command.App.Main.OS.system("clear")
        self.HttpsChangeFileText()
        self.CONFIRM = input(
            self.HTTPS_HAS_CHANGE + 
            "\n\nApakah data sudah benar?\nKetik (y/n) >>> "
            )
        self.HttpsGetUserCofirmation()
    
    # pengguna melakukan konfirmasi data
    def HttpsGetUserCofirmation(self):
        if self.CONFIRM not in ("y", "Y", "n", "N"):
            self.HttpsConfirmBeforeCreate()
        elif self.CONFIRM in ("y", "Y"):
            self.HttpsCreateFile()
        else:
            self.HttpsRun()
    
    # melakukan pembuatan file pada folder yang ditentukan
    def HttpsCreateFile(self):
        f = open(
            self.Command.App.Main.DEFAULT_DIR + 
            self.Command.FILENAME + 
            ".conf", "w+"
            )
        f.write(self.HTTPS_HAS_CHANGE)
        f.close()
        self.Command.App.AppContinue()
