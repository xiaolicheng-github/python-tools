from PyQt5.QtWidgets import (
    QVBoxLayout,
    QPushButton,
    QWidget,
    QGridLayout,
)


# 主页类
class HomePage(QWidget):
    # 定义按钮列表
    gridUIs = [
        {"position": (0, 0, 150, 100), "name": "局域网聊天", "id": "chat"},
        {"position": (0, 1, 150, 100), "name": "button2", "id": "button2"},
        {"position": (0, 2, 150, 100), "name": "button3", "id": "button3"},
        {"position": (1, 0, 150, 100), "name": "button4", "id": "button4"},
    ]

    # 初始化方法
    def __init__(self):
        super().__init__()
        layoutHome = QVBoxLayout()
        grid = QGridLayout()
        gridWidget = QWidget()
        for gridUIItem in self.gridUIs:
            button = QPushButton(gridUIItem["name"])
            if gridUIItem["id"] == "chat":
                button.clicked.connect(lambda: self.goToChatPage())
            button.setFixedSize(*gridUIItem["position"][2:4])
            grid.addWidget(button, *gridUIItem["position"][0:2])
        gridWidget.setLayout(grid)
        layoutHome.addWidget(gridWidget)
        self.setLayout(layoutHome)

    # 转到聊天页面方法
    def goToChatPage(self):
        self.window().showPage("chat")
