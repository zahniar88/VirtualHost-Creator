class App:
    # Menjalankan aplikasi
    def AppRunnning(self, Main):
        self.Main = Main
        self.AppRun()
    
    # menjalankan aplikasi secara umum
    def AppRun(self):
        self.CheckingFileEnv()
    
    # melakukan pengecekan file env
    def CheckingFileEnv(self):
        if self.Main.ENV_FILE:
            self.Main.RunningCommand(self)
        else:
            self.Main.RunningConfigure(self)

    # konfirmasi sebelum keluar aplikasi
    def AppConfirmBeforeExit(self):
        self.Main.OS.system("clear")
        CONFIRM = input("Apakah anda yakin akan keluar>\nKetik (y/n) >>> ")
        
        if CONFIRM not in ("Y", "y", "N", "n"):
            self.AppConfirmBeforeExit()
        elif CONFIRM in ("Y", "y"):
            self.Main.OS.system("clear")
        else:
            self.AppRun()
    
    # Melanjutkan aplikasi
    def AppContinue(self):
        self.Main.OS.system("clear")
        CONFIRM = input("Apakah anda ingin melanjutkan program?>\nKetik (y/n) >>> ")

        if CONFIRM not in ("Y", "y", "N", "n"):
            self.AppContinue()
        elif CONFIRM in ("Y", "y"):
            self.AppRun()
        else:
            self.Main.OS.system("clear")
