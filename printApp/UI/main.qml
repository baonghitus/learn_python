import QtQuick
import QtQuick.Controls.Basic

ApplicationWindow {
    visible: true
    width: 360
    height: 600
    x: screen.desktopAvailableWidth - width - 12
    y: screen.desktopAvailableHeight - height - 48
    title: "PrintApp"

    // flags: Qt.FramelessWindowHint | Qt.Window

    property string currTime: "00:00:00"
    property QtObject backend

    Rectangle {
        anchors.fill: parent
        Image {
            anchors.fill: parent
            source: "./images/test.jpeg"
            smooth: true
            fillMode: Image.PreserveAspectCrop
            horizontalAlignment: Image.AlignHCenter
            verticalAlignment: Image.AlignVCenter
            clip: true
        }
        Rectangle {
            anchors.fill: parent
            color: "transparent"
            Text {
                anchors {
                    bottom: parent.bottom
                    bottomMargin: 12
                    left: parent.left
                    leftMargin: 12
                }
                text: currTime
                font.pixelSize: 48
                color: "white"
            }
        }
    }

    Connections {
        target: backend

        function onUpdated(msg) {
            currTime = msg;
        }
    }
}