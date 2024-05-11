# 导入所需的模块
import sys

sys.path.insert(0, sys.path[0] + "/../")
from utils.server import get_ipv4_address
from utils.layout import cteate_layout
from PyQt5.QtWidgets import (
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QTextEdit,
    QLabel,
    QLineEdit,
    QPushButton,
)
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt


# 聊天页面类
class PageChat(QWidget):
    # 初始化方法
    def __init__(self):
        super().__init__()
        layoutChat = QVBoxLayout()
        # 信息确认面板
        iplabel = QLabel("当前ip地址: " + get_ipv4_address())
        iplabel.setTextInteractionFlags(Qt.TextSelectableByMouse)
        infoConfirmBtn = QPushButton("确认下方信息")
        infoConfirmBtn.setStyleSheet("margin-left: 20px; height: 30px; width: 100px;")
        iplabelQW = cteate_layout("h", iplabel, infoConfirmBtn, 1)
        # 昵称输入框
        nameInput = QLineEdit()
        nameInput.setFixedWidth(400)
        nameInputLabel = QLabel("昵称: ")
        nameInputLabel.setFixedWidth(100)
        nameInputQW = cteate_layout("h", nameInputLabel, nameInput, 1)
        # 目标服务器ip地址输入框
        serverIpInput = QLineEdit()
        serverIpInput.setFixedWidth(400)
        serverIpInputLabel = QLabel("目标服务器ip地址: ")
        serverIpInputLabel.setFixedWidth(100)
        serverIpInputHbox = QHBoxLayout()
        serverIpInputHbox.addWidget(serverIpInputLabel)
        serverIpInputHbox.addWidget(serverIpInput)
        serverIpInputHbox.addStretch(1)
        serverIpInputQW = QWidget()
        serverIpInputQW.setLayout(serverIpInputHbox)
        # 输出面板
        output_panel = QTextEdit()
        output_panel.setFixedSize(800, 400)  # 设置输出面板大小
        output_panel.setTextColor(QColor("white"))  # 设置文本颜色为白色
        output_panel.setStyleSheet("background-color: black")  # 设置背景颜色为黑色
        output_panel.setReadOnly(True)
        # 设置布局
        layoutChat.addWidget(iplabelQW)
        layoutChat.addWidget(nameInputQW)
        layoutChat.addWidget(serverIpInputQW)
        layoutChat.addWidget(output_panel)
        self.setLayout(layoutChat)

    # 返回主页方法
    def goBackHome(self):
        self.window().showPage("home")
