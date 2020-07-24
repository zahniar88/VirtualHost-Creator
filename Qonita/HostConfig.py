class HostConfig:
    # host Configurasi
    def Host(self, Command):
        self.Command = Command
        
    # Aktifkan host
    def EnableHost(self):
        self.HostInputFileName()
        self.Command.App.Main.OS.system(
            "sudo a2ensite " + self.FILENAME + 
            " && sudo systemctl restart apache2 && sudo systemctl reload apache2")
        self.Command.App.Main.OS.system("sudo nano /etc/hosts")
        self.Command.App.AppContinue()
    
    # Nonaktifkan host
    def DisableHost(self):
        self.HostInputFileName()
        self.Command.App.Main.OS.system(
            "sudo a2dissite " + self.FILENAME + 
            " && sudo systemctl restart apache2 && sudo systemctl reload apache2")
        self.Command.App.Main.OS.system("sudo nano /etc/hosts")
        self.Command.App.AppContinue()
    
    # Menghapus host
    def DeleteHost(self):
        self.HostInputFileName()
        self.HostConfirmBeforeDelete()
        
    # konfirmasi sebelum menghapus file
    def HostConfirmBeforeDelete(self):
        self.Command.App.Main.OS.system("clear")
        CONFIRM = input("Apakah anda yakin akan menghapus " + self.FILENAME + ".conf?\nKetik (y/n) >>> ")
        if CONFIRM not in ("Y", "y", "n", "N"):
            self.HostConfirmBeforeDelete()
        elif CONFIRM in ("n", "N"):
            self.Command.App.AppContinue()
        else:
            self.Command.App.Main.OS.remove(
                self.Command.App.Main.DEFAULT_DIR +
                self.FILENAME + ".conf"
            )
            self.Command.App.AppContinue()
    
    # memasukkan nama file
    def HostInputFileName(self):
        self.Command.App.Main.OS.system("clear")
        self.FILENAME = input("Masukkan nama file host (tanpa .conf) >>> ")
