#import sys
#import smallWindow
#from PyQt5.QtWidgets import QApplication, QMainWindow

#def main():
#    app = QApplication(sys.argv)
#    mainWindow = QMainWindow()
#    ui = smallWindow.Ui_MainWindow()
#    ui.setupUi(mainWindow)
#    mainWindow.show()
#    sys.exit(app.exec_())

#if __name__ == '__main__':
#    main()


import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QDesktopWidget, QHBoxLayout, QWidget
from PyQt5.QtGui import QIcon

class FirstMainWindow(QMainWindow):
    def __init__(self):
        super(FirstMainWindow, self).__init__()
        self.setWindowTitle('居中窗口')
        self.resize(400, 300)
        self.status = self.statusBar()
        self.status.showMessage('3sec.', 3000)
        self.quitButton = QPushButton('Exit')
        self.quitButton.clicked.connect(self.onClick_Button())

        layout = QHBoxLayout()
        layout .addWidget(self.quitButton)

        mainFram = QWidget()
        mainFram.setLayout(layout)

        self.setCentralWidget(mainFram)

    def onClick_Button(self):
        sender = self.sender()
        print(sender.text() + '按钮被按下')
        app = QApplication.instance()
        app.quit()

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        newLeft = (screen.width() - size.width()) // 2
        newTop = (screen.height() - size.height()) // 2

        self.move(newLeft, newTop)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    app.setWindowIcon(QIcon('C:\\Users\\20131\\Pictures\\Saved Pictures\\8f5b1cd8bc3eb13517d8e851ab1ea8d3fc1f4489.jpg'))
    main = FirstMainWindow()
    main.center()
    main.onClick_Button
    main.show()

    sys.exit(app.exec_())