from abc import ABC, abstractmethod
import pymongo
import pyfiglet
import time
from colorama import Fore, Style

class Database(ABC):
    @abstractmethod
    def checkConnection(self) -> None:
        pass

    @abstractmethod
    def displayTerminal(self) -> None:
        pass

    @abstractmethod
    def Choices(self, inputan) -> None:
        pass

class MongoDBDatabase(Database):
    def __init__(self, connection: str, dbname: str) -> None:
        self.client: pymongo.MongoClient = pymongo.MongoClient(connection)
        self.db_name = dbname

    def checkConnection(self) -> None:
        db_list = self.client.list_database_names()
        if self.db_name in db_list:
            print(f'{Fore.GREEN}Database {self.db_name} Already Connected{Style.RESET_ALL}')
            print()
        else:
            print(f'{Fore.RED}Database {self.db_name} Belum Ada !{Style.RESET_ALL}')
            print(f"Membuat Database ..")
            time.sleep(2)
            db = self.client[self.db_name]
            db.create_collection('Person')
            print(f"{Fore.GREEN}Berhasil Membuat Database..{Style.RESET_ALL}")
            print()

    def displayTerminal(self) -> None:
        banner = pyfiglet.figlet_format('LOGIN REGISTER', font='small')
        print(banner)
        print('Sudah Punya Akun ?')
        print('1. Sudah')
        print('2. Belum')
        try:
            input_user = int(input('Choices (1/2): '))
            self.Choices(input_user)
        except ValueError as e:
            print(f'{Fore.RED}Kamu memasukkan input yang salah..{Style.RESET_ALL}')
            print(e) 

    def Choices(self, inputan) -> None:
        db = self.client[self.db_name]
        if inputan == 2:
            print()
            print('- Form Register -')
            username_reg = input('Username: ').strip()
            password_reg = input('Password: ').strip()
            
            if username_reg == '' or password_reg == '':
                print(f'{Fore.RED}Username Dan Password Tidak Boleh Kosong !{Style.RESET_ALL}')
                return

            db['Person'].insert_one({
                'username': username_reg, 'password': password_reg
            })
            time.sleep(2)
            print(f"{Fore.GREEN}Berhasil Register Akun, Silahkan Login Untuk Menikmati Fitur ~ {Style.RESET_ALL}")
            time.sleep(3)
        

        elif inputan == 1:
            db = self.client[self.db_name]
            collection = db['Person']
            print()
            print('- Silahkan Masukkan Akun Untuk Login -')
            username_log = input('Username: ').strip()
            password_log = input('Password: ').strip()

            if username_log == '' or password_log == '':
                print(f'{Fore.RED}Username Dan Password Tidak Boleh Kosong !{Style.RESET_ALL}')
                return

            user = collection.find_one({'username': username_log})

            if not user:
                time.sleep(1)
                print('Username Atau Password Salah !')

            elif user and user['password'] == password_log:
                time.sleep(1)
                print(f'Login Sukses ~')
                print(f'{Fore.GREEN}Selamat Datang {username_log} {Style.RESET_ALL}')

        else:
            print('Inputan Tidak Sesuai')


if __name__ == "__main__":
    database = MongoDBDatabase('mongodb://root:2121@localhost:27017/', 'latihan')
    database.checkConnection()
    database.displayTerminal()
