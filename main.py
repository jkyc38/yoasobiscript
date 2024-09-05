from yoasobiscript.emailsetup import send_email
from yoasobiscript.yoasobi import init_browser, get_prices
import time

from_email = 'email'
to_email = 'email'

TARGET_PRICE = 150
price = 200
URL = 'https://www.stubhub.com/yoasobi-new-york-city-tickets-8-6-2024/event/153463870/?quantity=6'

while price>TARGET_PRICE:
    data = init_browser()
    price = min(get_prices(data))
    body = f'Lowest Price right now is ${price} \nCheck it out!: {URL}'
    subject = "Yoasobi Tickets"
    send_email(from_email, to_email, body, subject)
    minute = 60
    
    time.sleep(minute * 30)







