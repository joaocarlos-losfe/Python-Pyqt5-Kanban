from PyQt5 import QtGui
from PyQt5.QtWidgets import QMessageBox

class Dialogs:

    @classmethod
    def alert_mensage(self, mensage, title):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(mensage)
        msg.setWindowTitle(title)
        msg.setStandardButtons(QMessageBox.Ok)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Assets/icone.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        msg.setWindowIcon(icon)
        retval = msg.exec_()

    @classmethod
    def confirmation_mensage(self, mensage, title):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(mensage)
        msg.setWindowTitle(title)
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)

        confirmation = msg.exec()
        if confirmation == QMessageBox.Yes:
            return True
        else:
            return False
