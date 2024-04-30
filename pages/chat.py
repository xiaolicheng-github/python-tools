# 导入所需的模块
from PyQt5.QtWidgets import (
    QVBoxLayout,
    QWidget,
    QTextEdit,
)
from PyQt5.QtGui import QColor


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
