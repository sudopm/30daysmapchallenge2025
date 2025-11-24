import pandas as pd
import requests
import os


_OUTPUT_ = '20 Eau/blois'
# reading csv file 
def lire_csv():
    None



df = pd.read_csv('20 Eau/liste lidar 2 blois.csv')

url_list = list(df['url'])

for url in url_list:
    r = requests.get(url, allow_redirects=True,timeout=500)
    filename = url[-45:]
    path = os.path.join(_OUTPUT_,filename)
    print(path)
    open(path, 'wb').write(r.content)
