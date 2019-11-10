import urllib.request
from bs4 import BeautifulSoup
import logging
from logging.config import fileConfig



class basics:

    def __init__(self):

        fileConfig('../properties/logging_config.ini')
        self.log = logging.getLogger()
        self.log.debug('Logger intiated ')

    def https_get(self,ticker):

        headers = {
              'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
           }
        turl = 'https://in.finance.yahoo.com/quote/'+ ticker +'.NS?p='+ ticker +'.NS&.tsrc=fin-srch'


        request = urllib.request.Request(turl, headers=headers)
        response = urllib.request.urlopen(request)
        response = response.read().decode(encoding='UTF-8').strip()
        decoded = BeautifulSoup(response, "html.parser")
        return decoded


    def decode(self,ticker):  # 对指定ticker发送https请求并进行bs处理
        #url = 'https://finance.yahoo.com/quote/' + ticker + '?p=' + ticker + '&.tsrc=fin-srch'
        new_url = 'https://in.finance.yahoo.com/quote/'+ ticker +'.NS?p='+ ticker +'.NS'
        print( new_url)
        item = basics.https_get(new_url)
        #print (item)
        decoded = BeautifulSoup(item, "html.parser")
        #print (decoded)
        return decoded

if __name__ == "__main__":
   b = basics()

