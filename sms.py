import os
import requests
from dotenv import load_dotenv


class Sms():

    def __init__(self):
        load_dotenv()
        self.url_for_get = f'https://portal.nigeriabulksms.com/api/?username={os.getenv("sms_username")}&password={os.getenv("sms_password")}&action'
        self.url_for_post  = f'https://portal.nigeriabulksms.com/api/?username={os.getenv("sms_username")}&password={os.getenv("sms_password")}'
    
    def balance_getter(self):
        url = f'{self.url_for_get}=balance'
        balance = requests.get(url=url).json()
        return balance

    def report_getter(self):
        url = f'{self.url_for_get}=reports'
        balance = requests.get(url=url).json()
        return balance

    def sms_sender(self, sender, phone_numbers, message):
        msg_number =f'{self.url_for_post}&message={message}&sender={sender}&mobiles={phone_numbers}'
        send_sms = requests.post(msg_number)
        return send_sms

