

# https://cryptocointracker.com/yahoo-finance/yahoo-finance-api

import requests

user_agent = 'Mozilla/5.0'
user_agent = 'python-requests'

symbol = 'FDS'
params = None

#modules = 'financeData'  # csv
#url = f'https://query1.finance.yahoo.com/v10/finance/quoteSummary/{symbol}?modules={modules}'

module = 'chart'
interval = '1wk'
range = '1mo'
url = f'https://query1.finance.yahoo.com/v8/finance/{module}/{symbol}?interval={interval}&range={range}'

"""
module = 'download'
interval = '1wk'
period1 = 1641059569
period2 = 1641579977
url = f'https://query1.finance.yahoo.com/v7/finance/download/{symbol}?interval={interval}&period1={period1}&period2={period2}'
"""

#??
#params = { 'symbols':'FDS', 'interval':'1wk', 'range':'1mo' }

"""
module = 'quote'
url = f'https://query1.finance.yahoo.com/v8/finance/{module}'
"""

print('URL:', url)

if params is None:
    resp = requests.get(url, headers={'User-agent': user_agent})
else:
    resp = requests.get(url, headers={'User-agent': user_agent}, params=params)

print(resp.status_code, resp.reason)
if resp.status_code == 200:
    if module == 'download':
        print(resp.text)
    else:
        data = resp.json()[module]
        print(data.keys())
        print('ERROR:', data['error'])
        print(data['result'][0].keys())
        for r in data['result']:
            print('SYMBOL:', r['meta']['symbol'])
            print(r['indicators'].keys())
            for k,v in r['indicators'].items():
                print(k,v.__class__.__name__)
                for x in v:
                    for k2,v2 in x.items():
                        print('  ', k2,v2)


print('Done')
