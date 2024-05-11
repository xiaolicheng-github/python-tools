
from PyQt5.QtWidgets import (
  QHBoxLayout,
  QVBoxLayout,
  QWidget
)

def cteate_layout(type, *items):
  box: QHBoxLayout | QVBoxLayout = None
  if(type == 'h'):
    box = QHBoxLayout()
  elif(type == 'v'):
    box = QVBoxLayout()
  qW = QWidget()
  for item in items:
    if(isinstance(item, int)):
      box.addStretch(item)
    else:
      box.addWidget(item)
  qW.setLayout(box)
  return qW
