import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QGridLayout, QPushButton

class SimpleGUI(QWidget):
    
    gridUIs = [
        {
          'position': (0, 0, 150, 100),
          'name': '局域网聊天'
        },
        {
          'position': (0, 1, 150, 100),
          'name': 'button2'
        },
        {
          'position': (0, 2, 150, 100),
          'name': 'button3'
        },
        {
          'position': (1, 0, 150, 100),
          'name': 'button4'
        }
    ]

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        grid = QGridLayout()
        gridWidget = QWidget()

        print(self.gridUIs)
        for gridUIItem in self.gridUIs:
            button = QPushButton(gridUIItem['name'])
            button.setFixedSize(*gridUIItem['position'][2:4])
            grid.addWidget(button, *gridUIItem['position'][0:2])
        gridWidget.setLayout(grid)
        layout.addWidget(gridWidget)
        self.setLayout(layout)
        #设置窗口位置和大小
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('请疯狂点击我的身体吧')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SimpleGUI()
    sys.exit(app.exec_())
