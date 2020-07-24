class Configure:
    # menjalankan konfigurasi
    def RunningConfigure(self, App):
        self.App = App
        self.EnvRunCreate()
        
    # Menjalankan program
    def EnvRunCreate(self):
        self.InputDataConfigure()
        self.ChangeDataEnv()
        self.ConfirmBeforeCreateEnv()
        
    # menu input data konfigurasi
    def InputDataConfigure(self):
        self.App.Main.OS.system("clear")
        self.DIR      = input("Masukkan lokasi direktori vhost >>> ")
        self.USER     = input("Masukkan username bawaan (default root) >>> ")
        self.SSL      = input("Masukkan lokasi ssl vhost >>> ")
        self.DEF_USER = "root"
        if self.USER != "" : self.DEF_USER = self.USER

    # melakukan pengambilan data contoh dari file .env.example
    def GetEnvFile(self):
        f = open(".env.example", "r")
        self.ENV_TEXT = f.read()
        f.close()
        
    # melakukan pengubahan data
    def ChangeDataEnv(self):
        self.GetEnvFile()
        C1 = self.ENV_TEXT.replace("<DIR>", self.DIR)
        C2 = C1.replace("<USER>", self.DEF_USER)
        self.ENV_HAS_CHANGE = C2.replace("<SSL>", self.SSL)
    
    # konfirmasi sebelum file .env dibuat
    def ConfirmBeforeCreateEnv(self):
        self.App.Main.OS.system("clear")
        CONFIRM_CREATE = input(self.ENV_HAS_CHANGE + "\n\nApakah data yang anda masukkan sudah benar?\nKetik (y/n) >>> ")
        if CONFIRM_CREATE not in ("Y", "y", "n", "N"):
            self.ConfirmBeforeCreateEnv()
        elif CONFIRM_CREATE in ("Y", "y"):
            self.CreateEnvFile()
        else:
            self.EnvRunCreate()
        
    # membuat file .env
    def CreateEnvFile(self):
        f = open(".env", "w+")
        f.write(self.ENV_HAS_CHANGE)
        f.close()
        self.App.Main.OS.system("clear")
        print("File .env berhasil dibuat!")
