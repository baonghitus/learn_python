import requests
import json
from time import strftime, localtime
from PyQt6.QtCore import QObject, pyqtSignal, QTimer

class Order(QObject):

    apiDomain = 'http://localhost'
    apiToken = '5383927e1735118fe4599c28e9f1e8704014f861f2c4146dca4ba5542fcb59bb'

    updated = pyqtSignal(str, arguments=['time'])

    def __init__(self):
        super().__init__()
        self.getOder()

        # Define timer.
        self.timer = QTimer()
        self.timer.setInterval(60 * 1000)  # msecs 100 = 1/10th sec
        self.timer.timeout.connect(self.getOder)
        self.timer.start()

    def getOder(self):
        # Pass the current time to QML.
        curr_time = strftime("%H:%M:%S", localtime())

        # api-endpoint
        URL = "{}/app-api/getPrintOrderList/".format(self.apiDomain)

        # header
        requestsHeader = {'Accept': 'application/json, text/plain, */*', 'Content-Type':'application/json', 'Authorization': 'Bearer {}'.format(self.apiToken)}


        print('start --------------------------')
        try:
            # sending get request and saving the response as response object
            r = requests.get(url = URL, headers=requestsHeader)
            # extracting data in json format
            res = r.json()
            if 'success' not in res:
                if 'message' in res:
                    raise ValueError(res['message'])
                else:
                    raise ValueError('not connect')

            if res['success'] != True:
                raise ValueError("No true")

            if 'data' not in res:
                raise ValueError("No data")
            else:
                data = res['data']

        except Exception as e:
            print(e)
            return

        for item in data:
            print(item['id'])

