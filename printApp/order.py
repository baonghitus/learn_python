import requests
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

    def updateAfterPrint(self, id):
        # api-endpoint
        URL = "{}/app-api/updatePrintedStatus/{}".format(self.apiDomain, id)

        # header
        requestsHeader = {'Accept': 'application/json, text/plain, */*', 'Content-Type':'application/json', 'Authorization': 'Bearer {}'.format(self.apiToken)}

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

            if 'message' in res:
                print(res['message'])

        except Exception as e:
            print(e)
            return

    def getOder(self):
        # Pass the current time to QML.
        curr_time = strftime("%H:%M:%S", localtime())

        # api-endpoint
        URL = "{}/app-api/getPrintOrderList/".format(self.apiDomain)

        # header
        requestsHeader = {'Accept': 'application/json, text/plain, */*', 'Content-Type':'application/json', 'Authorization': 'Bearer {}'.format(self.apiToken)}

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
            try:
                filename = "orderfile/{}".format(str(item['id']))
                f = open(filename, "a")
                f.seek(0)
                f.truncate()

                f.write('受付：{}\n'.format(item['created_date']))
                f.write('----------------------------\n')
                f.write('{0} {1}様\n'.format(item['first_name'], item['last_name']))
                f.write('受取：{}\n'.format(item['receipt_at']))
                f.write('注文番号：{:0>5}\n'.format(item['id']))
                f.write('----------------------------\n')

                for product in item['product_list']:
                    f.write('□   ')
                    f.write(str(product['product_name']) + '\t')
                    f.write(str(product['quantity']) + '\t')
                    f.write(product['price'])
                    f.write('\n')

                f.write('----------------------------\n')
                f.write('⼩計　 {}\n'.format(item['subtotal']))
                f.write('消費税 {}\n'.format(item['total_tax']))
                f.write('合計　 {}\n'.format(item['total']))
                f.write('----------------------------\n')
                f.write('⽀払⽅法： {}\n'.format(item['payment_text']))
                f.write('⽀払結果： {}\n'.format(item['payment_status']))
                f.write('----------------------------\n')

                f.close()

                self.updateAfterPrint(item['id'])
            except Exception as e:
                print(e)
                return




