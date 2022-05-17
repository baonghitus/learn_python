import sys
from timeview import TimeView
from order import Order
from time import strftime, gmtime, sleep
from PyQt6.QtGui import QGuiApplication
from PyQt6.QtQml import QQmlApplicationEngine
from PyQt6.QtQuick import QQuickWindow

QQuickWindow.setSceneGraphBackend('software')

app = QGuiApplication(sys.argv)
engine = QQmlApplicationEngine()
engine.quit.connect(app.quit)
engine.load('./UI/main.qml')

timeview = TimeView()
order = Order()
engine.rootObjects()[0].setProperty('timeview', timeview)

sys.exit(app.exec())