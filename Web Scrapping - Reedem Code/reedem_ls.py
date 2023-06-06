from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyfiglet
from colorama import Fore,Style

display = pyfiglet.figlet_format('BOT REEDEM')
print(display)
print(f"""
{Fore.RED}AUTHOR: {Fore.GREEN}@CAESARR_ID
{Fore.RED}FUNGSI: {Fore.GREEN}BOT OTOMATIS REEDEM VOUCHER CODE DI WEBSITE LOSTSAGA ORIGIN {Style.RESET_ALL}
""")

class LostsagaVoucher:
    def __init__(self, url) -> None:
        self.url = url
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def openUrl(self, email, password) -> None:
        self.driver.get(self.url)
        input_email = self.driver.find_element(By.XPATH, '/html/body/section/div[3]/div/div/div/div/form/div[1]/input')
        input_email.send_keys(email)

        input_pass = self.driver.find_element(By.XPATH, '/html/body/section/div[3]/div/div/div/div/form/div[2]/input')
        input_pass.send_keys(password + Keys.ENTER)

        
    def reedemCode(self, query:str) -> None:
        self.driver.get(self.url)
        reedem_input = self.driver.find_element(By.XPATH, '/html/body/nav/div[1]/ul[1]/li[7]/a')
        reedem_input.click()

        input_reedem = self.driver.find_element(By.XPATH, '/html/body/section/div[2]/div/div/div[1]/div/form/div/input[1]')
        input_reedem.send_keys(query + Keys.ENTER)

        path = [
            '/html/body/div[2]/div[7]/div/button','/html/body/section/div[2]/div/div/div[1]/div[1]/a'
        ]

        for x in path:
            element = self.driver.find_element(By.XPATH, x)
            element.click()

    def quit_ls(self) -> None:
        
        self.driver.quit()

main = LostsagaVoucher('https://lostsaga.gnjoy.id/member')
main.openUrl('kokon200','Profesional1')
reedem = (
'66HPRNP','VCPLSTD','9IWHGFE'
'KTJX240','BJMZTGP','D4CPSVQ'
)

for red in reedem:
    main.reedemCode(red)


# input('Ketik Enter Untuk Stop')

main.quit_ls()
print('BOT SELESAI, TERIMAKASIH ~')
