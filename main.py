import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QWidget, QGridLayout, QTextEdit, QScrollArea
from PyQt5.QtGui import QColor

class MainWindow(QMainWindow):
    pages = [
        {
          'id': 'home',
          'page': None
        },
        {
          'id': 'chat',
          'page': None
        }
    ]
    def __init__(self):
        super().__init__()

        #设置窗口位置和大小
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('请疯狂点击我的身体吧')
        self.container = QWidget()  # 创建一个容器 widget 用于存放不同的页面
        self.setCentralWidget(self.container)
        self.layout = QVBoxLayout()
        self.container.setLayout(self.layout)


        self.pagesSet('home', HomePage())
        self.pagesSet('chat', PageChat())

        self.showPage('home')

    def pagesSet(self, pageId, pageInstance):
        for page in self.pages:
            if page['id'] == pageId:
                page['page'] = pageInstance
                self.layout.addWidget(pageInstance)
        
    def showPage(self, pageId):
        for page in self.pages:
            if page['id'] == pageId:
                page['page'].show()
            else:
                page['page'].hide()

class HomePage(QWidget):
    gridUIs = [
        {
          'position': (0, 0, 150, 100),
          'name': '局域网聊天',
          'id': 'chat'
        },
        {
          'position': (0, 1, 150, 100),
          'name': 'button2',
          'id': 'button2'
        },
        {
          'position': (0, 2, 150, 100),
          'name': 'button3',
          'id': 'button3'
        },
        {
          'position': (1, 0, 150, 100),
          'name': 'button4',
          'id': 'button4'
        }
    ]
    def __init__(self):
        super().__init__()
        layoutHome = QVBoxLayout()
        grid = QGridLayout()
        gridWidget = QWidget()
        for gridUIItem in self.gridUIs:
            button = QPushButton(gridUIItem['name'])
            if gridUIItem['id'] == 'chat':
              button.clicked.connect(lambda: self.goToChatPage())
            button.setFixedSize(*gridUIItem['position'][2:4])
            grid.addWidget(button, *gridUIItem['position'][0:2])
        gridWidget.setLayout(grid)
        layoutHome.addWidget(gridWidget)
        self.setLayout(layoutHome)

    def goToChatPage(self):
        self.window().showPage('chat')

class PageChat(QWidget):
    def __init__(self):
        super().__init__()
        layoutChat = QVBoxLayout()
        output_panel = QTextEdit()
        output_panel.setFixedSize(800, 400)  # 设置输出面板大小
        output_panel.setTextColor(QColor('white'))  # 设置文本颜色为白色
        output_panel.setStyleSheet("background-color: black")  # 设置背景颜色为黑色
        output_panel.setReadOnly(True)
        layoutChat.addWidget(output_panel)
        self.setLayout(layoutChat)

    def goBackHome(self):
        self.window().showPage('home')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
