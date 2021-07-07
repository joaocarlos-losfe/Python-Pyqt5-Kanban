from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QEvent
from PyQt5.QtWidgets import QMessageBox, QListWidgetItem

import string_cheks
from Model.database import Database
from Model.task import Task

from Screens.detailsscreen import Ui_DetailsScreen

class HomeScreen():
    def __init__(self, theme, project_id):
        self.defined_theme = theme
        self.project_id = project_id

        self._new_tasks = []
        self._in_progress = []
        self._concluded = []

        self.selected_list_view = None

    def show_details_screen(self):

        if self.selected_list_view is not None:
            details = None
            if self.selected_list_view is Task.NEW_TASK:
                row = self.listview_new_task.currentRow()
                task = self._new_tasks[row]
                details = task.get_all_details()

            elif self.selected_list_view is Task.IN_PROGRESS:
                row = self.listview_in_progress.currentRow()
                task = self._in_progress[row]
                details = task.get_all_details()

            elif self.selected_list_view is Task.CONCLUDED:
                row = self.listview_concluded.currentRow()
                task = self._concluded[row]
                details = task.get_all_details()

            if details is not None:
                self.home_window = QtWidgets.QMainWindow()
                self.ui = Ui_DetailsScreen(self.defined_theme, details)
                self.ui.setupUi(self.home_window)
                self.home_window.show()
                


    def update_number_of_tasks(self):
        self.new_task_lbl.setText(f"Nova tarefa ({str(len(self._new_tasks))} tarefas)")
        self.in_progress_lbl.setText(f"Em progresso ({str(len(self._in_progress))} tarefas)")
        self.concluded_lbl.setText(f"Concluidos ({str(len(self._concluded))} tarefas)")

    def back_task(self):

        if self.selected_list_view is not None:
            if self.selected_list_view is Task.CONCLUDED:

                row = self.listview_concluded.currentRow()
                task = self._concluded[row]
                task.update_stage(2)

                self.listview_concluded.takeItem(row)
                self._concluded.pop(row)
                self._in_progress.append(task)

                item = self.create_item(task.get_text)
                self.listview_in_progress.addItem(item)


            elif self.selected_list_view is Task.IN_PROGRESS:
                row = self.listview_in_progress.currentRow()
                task = self._in_progress[row]
                task.update_stage(1)

                self.listview_in_progress.takeItem(row)
                self._in_progress.pop(row)
                self._new_tasks.append(task)

                item = self.create_item(task.get_text)
                self.listview_new_task.addItem(item)

            self.update_number_of_tasks()


    def delete_project(self):
        if self.selected_list_view is not None:
            if self.selected_list_view is Task.NEW_TASK:
                if self.listview_new_task.currentRow() != -1:

                    row = self.listview_new_task.currentRow()
                    task = self._new_tasks[row]

                    task.remove_from_data_base()
                    self.listview_new_task.takeItem(row)
                    self._new_tasks.pop(row)


            elif self.selected_list_view is Task.IN_PROGRESS:
                if self.listview_in_progress.currentRow() != -1:

                    row = self.listview_in_progress.currentRow()
                    task = self._in_progress[row]
                    task.remove_from_data_base()

                    self.listview_in_progress.takeItem(row)
                    self._in_progress.pop(row)


            elif self.selected_list_view is Task.CONCLUDED:
                if self.listview_concluded.currentRow() != -1:

                    row = self.listview_concluded.currentRow()
                    task = self._concluded[row]

                    task.remove_from_data_base()
                    self.listview_concluded.takeItem(row)
                    self._concluded.pop(row)


            self.selected_list_view = None
            self.hide_action_buttons()

            self.listview_new_task.clearSelection()
            self.listview_in_progress.clearSelection()
            self.listview_concluded.clearSelection()

            self.update_number_of_tasks()


    def action_connect_start(self):
        self.hide_action_buttons()
        self.add_task_btn.clicked.connect(self.new_task)
        self.listview_new_task.itemClicked.connect(self.selected_new_task)
        self.listview_in_progress.itemClicked.connect(self.selected_inprogress_task)
        self.listview_concluded.itemClicked.connect(self.selected_concluded_task)
        self.delete_task_btn.clicked.connect(self.delete_project)
        self.task_to_in_progress_btn.clicked.connect(self.move_task_to_improgress)
        self.in_progress_to_concluded_btn.clicked.connect(self.move_improgress_to_concluded)
        self.back_task_btn.clicked.connect(self.back_task)
        self.details_task_btn.clicked.connect(self.show_details_screen)

    def move_task_to_improgress(self):

        if self.selected_list_view is not None:
            if self.selected_list_view is Task.NEW_TASK:
                row = self.listview_new_task.currentRow()
                task = self._new_tasks[row]
                task.update_stage(2) #atualiza o estage no bd

                self.listview_new_task.takeItem(row)
                self._new_tasks.pop(row)
                self._in_progress.append(task)

                item = self.create_item(task.get_text)
                self.listview_in_progress.addItem(item)

                self.update_number_of_tasks()

    def move_improgress_to_concluded(self):
        if self.selected_list_view is not None:
            if self.selected_list_view is Task.IN_PROGRESS:

                row = self.listview_in_progress.currentRow()
                task = self._in_progress[row]
                task.update_stage(3) #atualiza o estage no bd

                self.listview_in_progress.takeItem(row)
                self._in_progress.pop(row)
                self._concluded.append(task)
                
                item = self.create_item(task.get_text)
                self.listview_concluded.addItem(item)

                self.update_number_of_tasks()

    def selected_new_task(self):
        self.selected_list_view = Task.NEW_TASK
        self.show_action_buttons()

    def selected_inprogress_task(self):
        self.selected_list_view = Task.IN_PROGRESS
        print("selected: " + self.selected_list_view)
        self.show_action_buttons()

    def selected_concluded_task(self):
        self.selected_list_view = Task.CONCLUDED
        print("selected: " + self.selected_list_view)
        self.show_action_buttons()

    def show_action_buttons(self):
        self.back_task_btn.setVisible(True)
        self.details_task_btn.setVisible(True)
        self.delete_task_btn.setVisible(True)

    def hide_action_buttons(self):
        self.back_task_btn.setVisible(False)
        self.details_task_btn.setVisible(False)
        self.delete_task_btn.setVisible(False)

    def load(self):
        db = Database()
        data_load = db.get_tasks(self.project_id)

        for key in data_load.keys():

            task = Task()

            task.recovery(data_load[key][0], data_load[key][1], data_load[key][2], data_load[key][3], data_load[key][4], data_load[key][5])

            if data_load[key][4] == Task.NEW_TASK:
                self.listview_new_task.addItem(self.create_item(data_load[key][5]))
                self._new_tasks.append(task)

            elif data_load[key][4] == Task.IN_PROGRESS:
                self.listview_in_progress.addItem(self.create_item(data_load[key][5]))
                self._in_progress.append(task)

            elif data_load[key][4] == Task.CONCLUDED:
                self.listview_concluded.addItem(self.create_item(data_load[key][5]))
                self._concluded.append(task)


    def create_item(self, text):
        item = QListWidgetItem()
        item.setText(text)
        item.setTextAlignment(Qt.AlignHCenter)
        return item

    def new_task(self):
        if not string_cheks.StringCheck.is_space_or_null(self.new_task_input.toPlainText()):
            task = Task()
            task.create(self.project_id, self.new_task_input.toPlainText())
            item = QListWidgetItem()
            item.setText(self.new_task_input.toPlainText())
            item.setTextAlignment(Qt.AlignHCenter)
            self.listview_new_task.addItem(item)
            self._new_tasks.append(task)

            self.update_number_of_tasks()


    def setupUi(self, HomeScreen):
        HomeScreen.setObjectName("mainWindow")
        HomeScreen.setWindowModality(QtCore.Qt.NonModal)
        HomeScreen.resize(1000, 613)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(HomeScreen.sizePolicy().hasHeightForWidth())
        HomeScreen.setSizePolicy(sizePolicy)
        HomeScreen.setMinimumSize(QtCore.QSize(1000, 400))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        HomeScreen.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Assets/icone.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        HomeScreen.setWindowIcon(icon)
        HomeScreen.setWindowOpacity(1.0)
        HomeScreen.setStyleSheet("background: #F9FAFF;")
        HomeScreen.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(HomeScreen)
        self.centralwidget.setStyleSheet(self.defined_theme.style_background())

        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.project_list_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.project_list_btn.sizePolicy().hasHeightForWidth())
        self.project_list_btn.setSizePolicy(sizePolicy)
        self.project_list_btn.setStyleSheet(self.defined_theme.style_action_button())
        self.project_list_btn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Assets/projects.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.project_list_btn.setIcon(icon1)
        self.project_list_btn.setIconSize(QtCore.QSize(32, 32))
        self.project_list_btn.setFlat(False)
        self.project_list_btn.setObjectName("project_list_btn")

        self.horizontalLayout_10.addWidget(self.project_list_btn)
        self.title_lbl = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(-1)
        self.title_lbl.setFont(font)
        self.title_lbl.setStyleSheet(self.defined_theme.style_project_title())
        self.title_lbl.setObjectName("title_lbl")
        self.horizontalLayout_10.addWidget(self.title_lbl)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem)
        self.back_task_btn = QtWidgets.QPushButton(self.centralwidget)
        self.back_task_btn.setStyleSheet(self.defined_theme.style_action_button())
        self.back_task_btn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Assets/back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.back_task_btn.setIcon(icon2)
        self.back_task_btn.setIconSize(QtCore.QSize(24, 24))
        self.back_task_btn.setObjectName("back_task_btn")
        self.horizontalLayout_10.addWidget(self.back_task_btn)
        self.details_task_btn = QtWidgets.QPushButton(self.centralwidget)
        self.details_task_btn.setStyleSheet(self.defined_theme.style_action_button())
        self.details_task_btn.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Assets/details.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.details_task_btn.setIcon(icon3)
        self.details_task_btn.setIconSize(QtCore.QSize(24, 24))
        self.details_task_btn.setObjectName("details_task_btn")
        self.horizontalLayout_10.addWidget(self.details_task_btn)
        self.delete_task_btn = QtWidgets.QPushButton(self.centralwidget)
        self.delete_task_btn.setStyleSheet(self.defined_theme.style_action_button())
        self.delete_task_btn.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Assets/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delete_task_btn.setIcon(icon4)
        self.delete_task_btn.setIconSize(QtCore.QSize(24, 24))
        self.delete_task_btn.setObjectName("delete_task_btn")
        self.horizontalLayout_10.addWidget(self.delete_task_btn)
        self.verticalLayout_12.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.new_task_lbl = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.new_task_lbl.setFont(font)
        self.new_task_lbl.setStyleSheet(self.defined_theme.style_info())
        self.new_task_lbl.setObjectName("new_task_lbl")
        self.verticalLayout_13.addWidget(self.new_task_lbl)
        self.new_task_input = QtWidgets.QTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.new_task_input.sizePolicy().hasHeightForWidth())
        self.new_task_input.setSizePolicy(sizePolicy)
        self.new_task_input.setMaximumSize(QtCore.QSize(16777215, 100))
        self.new_task_input.setStyleSheet(self.defined_theme.style_text_input())
        self.new_task_input.setObjectName("new_task_input")
        self.verticalLayout_13.addWidget(self.new_task_input)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem1)
        self.add_task_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_task_btn.setMinimumSize(QtCore.QSize(50, 35))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.add_task_btn.setFont(font)
        self.add_task_btn.setStyleSheet(self.defined_theme.style_button())
        self.add_task_btn.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("Assets/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_task_btn.setIcon(icon5)
        self.add_task_btn.setObjectName("add_task_btn")
        self.horizontalLayout_9.addWidget(self.add_task_btn)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem2)
        self.verticalLayout_13.addLayout(self.horizontalLayout_9)
        self.listview_new_task = QtWidgets.QListWidget(self.centralwidget)
        self.listview_new_task.setStyleSheet(self.defined_theme.style_list_widget())
        self.listview_new_task.setObjectName("listview_new_task")
        self.listview_new_task.setSpacing(5)
        self.listview_new_task.setWordWrap(True)
        self.verticalLayout_13.addWidget(self.listview_new_task)
        self.horizontalLayout_8.addLayout(self.verticalLayout_13)
        self.verticalLayout_19 = QtWidgets.QVBoxLayout()
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.task_to_in_progress_btn = QtWidgets.QPushButton(self.centralwidget)
        self.task_to_in_progress_btn.setMinimumSize(QtCore.QSize(50, 30))
        self.task_to_in_progress_btn.setStyleSheet(self.defined_theme.style_button())
        self.task_to_in_progress_btn.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("Assets/next.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.task_to_in_progress_btn.setIcon(icon6)
        self.task_to_in_progress_btn.setDefault(False)
        self.task_to_in_progress_btn.setFlat(False)
        self.task_to_in_progress_btn.setObjectName("task_to_in_progress_btn")
        self.verticalLayout_19.addWidget(self.task_to_in_progress_btn)
        self.horizontalLayout_8.addLayout(self.verticalLayout_19)
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.in_progress_lbl = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.in_progress_lbl.setFont(font)
        self.in_progress_lbl.setStyleSheet(self.defined_theme.style_info())
        self.in_progress_lbl.setObjectName("in_progress_lbl")
        self.verticalLayout_16.addWidget(self.in_progress_lbl)
        self.listview_in_progress = QtWidgets.QListWidget(self.centralwidget)
        self.listview_in_progress.setStyleSheet(self.defined_theme.style_list_widget())
        self.listview_in_progress.setObjectName("listview_in_progress")
        self.listview_in_progress.setWordWrap(True)
        self.listview_in_progress.setSpacing(5)
        self.verticalLayout_16.addWidget(self.listview_in_progress)
        self.horizontalLayout_8.addLayout(self.verticalLayout_16)
        self.in_progress_to_concluded_btn = QtWidgets.QPushButton(self.centralwidget)
        self.in_progress_to_concluded_btn.setMinimumSize(QtCore.QSize(50, 30))
        self.in_progress_to_concluded_btn.setStyleSheet(self.defined_theme.style_button())
        self.in_progress_to_concluded_btn.setText("")
        self.in_progress_to_concluded_btn.setIcon(icon6)
        self.in_progress_to_concluded_btn.setObjectName("in_progress_to_concluded_btn")
        self.horizontalLayout_8.addWidget(self.in_progress_to_concluded_btn)
        self.verticalLayout_20 = QtWidgets.QVBoxLayout()
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.horizontalLayout_8.addLayout(self.verticalLayout_20)
        self.verticalLayout_17 = QtWidgets.QVBoxLayout()
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.concluded_lbl = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.concluded_lbl.setFont(font)
        self.concluded_lbl.setStyleSheet(self.defined_theme.style_info())
        self.concluded_lbl.setObjectName("concluded_lbl")
        self.verticalLayout_17.addWidget(self.concluded_lbl)
        self.listview_concluded = QtWidgets.QListWidget(self.centralwidget)
        self.listview_concluded.setStyleSheet(self.defined_theme.style_list_widget())
        self.listview_concluded.setObjectName("listview_concluded")
        self.listview_concluded.setWordWrap(True)
        self.listview_concluded.setSpacing(5)
        self.verticalLayout_17.addWidget(self.listview_concluded)
        self.horizontalLayout_8.addLayout(self.verticalLayout_17)
        self.verticalLayout_12.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_5.addLayout(self.verticalLayout_12)
        HomeScreen.setCentralWidget(self.centralwidget)

        self.project_list_btn.clicked.connect(HomeScreen.close)
        self.action_connect_start()
        self.load()
        self.retranslateUi(HomeScreen)
        QtCore.QMetaObject.connectSlotsByName(HomeScreen)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Tarefas sequenciais"))
        self.title_lbl.setText(_translate("mainWindow", self.project_id))
        self.new_task_lbl.setText(_translate("mainWindow", f"Nova tarefa ({str(len(self._new_tasks))} tarefas)"))
        self.new_task_input.setPlaceholderText(_translate("mainWindow", "Digite a nova tarefa aqui..."))
        self.in_progress_lbl.setText(_translate("mainWindow", f"Em progresso ({str(len(self._in_progress))} tarefas)"))
        self.concluded_lbl.setText(_translate("mainWindow", f"Concluidos ({str(len(self._concluded))} tarefas)"))