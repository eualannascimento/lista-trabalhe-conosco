# Import modules
import requests
import pandas as pd
import urllib.request
import urllib.error
from datetime import date
import IPython.display as display
import socket
from requests.exceptions import ConnectionError

# Import career-websites.csv to DataFrame
carrer_websites_df = pd.read_csv('src/csv/career-websites.csv', encoding='utf-8')

# Define function to get html from website through webscraping
def verify_website_status(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return '1'
    except requests.exceptions.HTTPError:
        try:
            response = requests.post(url)
            if response.status_code == 200:
                return '1'
        except requests.exceptions.HTTPError:
            try:
                response = urllib.request.urlopen(url)
                if response.getcode() == 200:
                    return '1'
                else:
                    return '0'
            except urllib.error.URLError:
                return '0'
            except socket.gaierror:
                return '0'  # Trate socket.gaierror aqui
        except ConnectionError:
            return '0'  # Trate ConnectionError aqui
    except socket.gaierror:
        return '0'  # Trate socket.gaierror aqui
    except requests.exceptions.ConnectionError:
        return '0'  # Trate socket.gaierror aqui

# Loop through the 'Site' column of the DataFrame and call the `verify_website_status` function on each URL
for index, row in carrer_websites_df.iterrows():
    url = row['URL']
    status = verify_website_status(url)
    if not status:
        status = 0
    carrer_websites_df.loc[index, 'Data do Status'] = date.today().strftime("%d/%m/%Y")
    carrer_websites_df.loc[index, 'Status da URL'] = status

# Save the DataFrame to a new CSV file
carrer_websites_df.to_csv('src/csv/career-websites.csv', encoding='utf-8', index=False)