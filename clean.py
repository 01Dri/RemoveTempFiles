import os
from colorama import init, Fore, Style


class TempDelFiles:

    def __init__(self) -> None:
        init()
        self.TEMP = None
        self.PLUSTEMP = None
        self.PREFETCH = None

        self.nick = None

        self.quantity_files_temp = 0
        self.quantity_files_temp_permision_error = 0

        self.quantity_files_tempwin = 0
        self.quantity_files_tempwin_permision_error = 0

        self.quantity_files_prefetch = 0
        self.quantity_files_prefetch_permision_error = 0

    def addValueInPathFolders(self):
        self.TEMP = os.environ.get('TEMP_DEFAULT')
        if self.TEMP == None:
            os.environ['TEMP_DEFAULT'] = 'C:\\Windows\\Temp'
            self.TEMP = os.environ.get('TEMP_DEFAULT')

        self.nick = os.getlogin()
        if self.PLUSTEMP == None:
            os.environ['PLUSTEMP'] = f'C:\\Users\\{self.nick}\\AppData\\Local\\Temp'
            self.PLUSTEMP = os.environ.get('PLUSTEMP')


        self.PREFETCH = os.environ.get('PREFETCH')
        if self.PREFETCH == None:
            os.environ['PREFETCH'] = 'C:\\Windows\\Prefetch'
            self.PREFETCH = os.environ.get("PREFETCH")


    def removeAllFilesTempPath(self):
        for file in os.listdir(self.TEMP):
            path_file = os.path.join(self.TEMP, file)
            try:
                os.remove(path_file)
                self.quantity_files_temp += 1
            except PermissionError:
                self.quantity_files_temp_permision_error += 1

    def removeAllFilesTempWinPath(self):
        for file in os.listdir(self.PLUSTEMP):
            path_file = os.path.join(self.PLUSTEMP, file)
            try:
                os.remove(path_file)
                self.quantity_files_tempwin += 1
            except PermissionError:
                self.quantity_files_tempwin_permision_error += 1

    def removeAllFilesPrefetchPath(self):
        for file in os.listdir(self.PREFETCH):
            path_file = os.path.join(self.PREFETCH, file)
            try:
                os.remove(path_file)
                self.quantity_files_prefetch += 1
            except PermissionError:
                self.quantity_files_prefetch_permision_error += 1


    def showInformationForUser(self):
        os.system('cls')
        print(Fore.WHITE + f">>>> DRI LIXEIRO PASSANDO <<<<" + Style.RESET_ALL)
        self.logInformation("TEMP", self.quantity_files_temp, self.quantity_files_temp_permision_error)
        self.logInformation("[%TEMP%]", self.quantity_files_tempwin, self.quantity_files_tempwin_permision_error)
        self.logInformation("PREFETCH", self.quantity_files_prefetch, self.quantity_files_prefetch_permision_error)

        
    def logInformation(self, path_name, quantity_files_removed, quantity_errors_permission):
        print("")
        if quantity_files_removed == 0 and quantity_errors_permission > 0:
            print(f"ALGUNS ARQUIVOS NA PASTA {path_name} NÃO FORAM APAGADOS, QUANTIDADE: " + Fore.RED + f'{quantity_errors_permission}' + Style.RESET_ALL)
        elif quantity_files_removed == 0 and quantity_errors_permission == 0:
            print(Fore.BLUE + f"A PASTA {path_name} ESTAVA VAZIA!!!"  + Style.RESET_ALL)
        elif quantity_files_removed > 0 and quantity_errors_permission == 0:
            print(f"ARQUIVOS APAGADOS EM {path_name}: " + Fore.GREEN + f'{quantity_files_removed}' + Style.RESET_ALL)

init_class = TempDelFiles()
init_class.addValueInPathFolders()
init_class.removeAllFilesTempPath()
init_class.removeAllFilesTempWinPath()
init_class.removeAllFilesPrefetchPath()
init_class.showInformationForUser()