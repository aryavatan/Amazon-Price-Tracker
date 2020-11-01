import requests
from bs4 import BeautifulSoup
import smtplib
import json

def readSettings():
    with open('Settings.json') as file:
        data = json.load(file)
        return data

def saveSettings(data):
    with open('Settings.json', 'w') as file:
        json.dump(data, file, indent=4)

def checkPrice(data):
    header = data['header']
    watchlist = data['watchlist']

    for url in watchlist:
        # Get page content
        page = requests.get(url, headers=header)
        soup = BeautifulSoup(page.content, "html5lib")

        # Get product title
        title = soup.find(id='productTitle')
        if title is None:
            print('\nCannot get product title of ', url)
            continue
        else:
            title = title.get_text().strip()

        # Get current product price
        price = soup.find(id='priceblock_ourprice')
        if price is None:
            # If no regular price, check for sale price
            price = soup.find(id='priceblock_saleprice')
            if price is None:
                print('\nCannot get price of ', title)
                continue
        # Convert price to float
        price = price.get_text().strip()
        converted_price = float(price[5:])

        # Check to see if lower than previous price
        checkPreviousPrice(data, url, converted_price)

        print('\n')
        print('Product:', title)
        print('Price:', converted_price)

def checkPreviousPrice(data, url, price):
    found = False
    
    for entry in data['previous-prices']:
        if entry['url'] == url:
            found = True
            
            if price < entry['price']:
                # Item is on Sale
                sendMail(data, url)
                entry['price'] = price
                saveSettings(data)
            elif price > entry['price']:
                # Items price went up
                entry['price'] = price
                saveSettings(data)
            
            break
    
    # If no record found, add to previous prices
    if not found:
        print('not found')
        entry = {
            "url":url,
            "price":price
        }
        data['previous-prices'].append(entry)
        saveSettings(data)

def cleanUpSettings(data):
    modified = False
    index = 0

    watchlist = data['watchlist']
    for entry in data['previous-prices']:
        if entry['url'] not in watchlist:
            data['previous-prices'].pop(index)
            modified = True
        index = index + 1

    if modified:
        saveSettings(data)
    
def sendMail(data, url):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    username = data['email-login']['username']
    password = data['email-login']['password']
    server.login(username, password)

    subject = 'Price fell down - Amazon Price Tracker'
    body = 'Check the amazon link: ' + url
    
    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        username,
        username,
        msg
    )
    print('Email has been sent!')

    server.quit()

data = readSettings()  # Get settings
cleanUpSettings(data)  # Clean up settings
checkPrice(data)  # Check the prices of watchlist items