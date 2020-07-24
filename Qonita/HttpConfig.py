class HttpConfig:
    # menjalankan konfigurasi HttpConfig secara umum
    def HttpRunning(self, Command):
        self.Command = Command
        self.HttpRun()
        
    # menjalankan program utama HttpConfig
    def HttpRun(self):
        self.Command.App.Main.OS.system("clear")
        self.Command.CommandInputOnlyHttp()
        self.HttpConfirmBeforeCreate()
    
    # mengambil contoh data Http
    def HttpGetFileText(self):
        f = open("Txt/Http.txt", "r")
        self.FILE_HTTP = f.read()
        f.close()
        
    # mengubah isi contoh data menjadi data yang telah di input
    def HttpChangeFileText(self):
        self.HttpGetFileText()
        C1 = self.FILE_HTTP.replace("#DIR#", self.Command.DIR)
        C2 = C1.replace("#DOMAIN#", self.Command.DOMAIN)
        self.HTTP_HAS_CHANGE = C2.replace("#ROOT#", self.Command.ROOT)
        
    # konfirmasi data sebelum di buat
    def HttpConfirmBeforeCreate(self):
        self.Command.App.Main.OS.system("clear")
        self.HttpChangeFileText()
        self.CONFIRM = input(
            self.HTTP_HAS_CHANGE + 
            "\n\nApakah data sudah benar?\nKetik (y/n) >>> "
            )
        self.HttpGetUserCofirmation()
    
    # pengguna melakukan konfirmasi data
    def HttpGetUserCofirmation(self):
        if self.CONFIRM not in ("y", "Y", "n", "N"):
            self.HttpConfirmBeforeCreate()
        elif self.CONFIRM in ("y", "Y"):
            self.HttpCreateFile()
        else:
            self.HttpRun()
    
    # melakukan pembuatan file pada folder yang ditentukan
    def HttpCreateFile(self):
        f = open(
            self.Command.App.Main.DEFAULT_DIR + 
            self.Command.FILENAME + 
            ".conf", "w+"
            )
        f.write(self.HTTP_HAS_CHANGE)
        f.close()
        self.Command.App.AppContinue()
