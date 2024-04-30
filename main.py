# 导入所需的模块
import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QPushButton,
    QWidget,
    QGridLayout,
    QTextEdit,
    QToolBar,
    QAction,
)
from PyQt5.QtGui import QColor, QIcon
from PyQt5.QtCore import Qt
from utils.path import get_path


# 主窗口类
class MainWindow(QMainWindow):
    # 定义页面列表
    pages = [{"id": "home", "page": None}, {"id": "chat", "page": None}]

    # 初始化方法
    def __init__(self):
        super().__init__()

        # 设置窗口位置和大小
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle("请疯狂点击我的身体吧")  # 设置窗口标题
        self.container = QWidget()  # 创建一个容器 widget 用于存放不同的页面
        self.setCentralWidget(self.container)  # 将容器设置为中心窗口
        self.layout = QVBoxLayout()
        self.container.setLayout(self.layout)

        # 工具栏
        self.toolbar = QToolBar()

        # 定义页面
        self.pagesSet("home", HomePage())  # 设置主页
        self.pagesSet("chat", PageChat())  # 设置聊天页面

        self.showPage("home")  # 显示主页

    # 设置页面实例
    def pagesSet(self, pageId, pageInstance):
        for page in self.pages:
            if page["id"] == pageId:
                page["page"] = pageInstance
                self.layout.addWidget(pageInstance)

    # 切换页面方法
    def showPage(self, pageId):
        for page in self.pages:
            if page["id"] == pageId:
                page["page"].show()
                self.backContainer(pageId)
            else:
                page["page"].hide()

    # 返回区域方法
    def backContainer(self, pageId):
        # 返回按钮
        if pageId == "home":
            self.removeToolBar(self.toolbar)
        else:
            self.toolbar = QToolBar()
            self.toolbar.setMovable(False)
            self.addToolBar(self.toolbar)
            self.backAction = QAction(
                QIcon(get_path("./static/back.png")), "返回", self
            )
            self.backAction.triggered.connect(lambda: self.goBack("home"))
            self.toolbar.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
            self.toolbar.addAction(self.backAction)

    # 返回事件方法
    def goBack(self, pageId):
        for page in self.pages:
            if page["id"] == pageId:
                page["page"].show()
                if pageId == "home":
                    self.removeToolBar(self.toolbar)
            else:
                page["page"].hide()


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


# 聊天页面类
class PageChat(QWidget):
    # 初始化方法
    def __init__(self):
        super().__init__()
        layoutChat = QVBoxLayout()
        output_panel = QTextEdit()
        output_panel.setFixedSize(800, 400)  # 设置输出面板大小
        output_panel.setTextColor(QColor("white"))  # 设置文本颜色为白色
        output_panel.setStyleSheet("background-color: black")  # 设置背景颜色为黑色
        output_panel.setReadOnly(True)
        layoutChat.addWidget(output_panel)
        self.setLayout(layoutChat)

    # 返回主页方法
    def goBackHome(self):
        self.window().showPage("home")


# 应用程序入口
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
