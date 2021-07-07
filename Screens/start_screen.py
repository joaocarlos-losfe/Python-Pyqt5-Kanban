from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QEvent
from PyQt5.QtWidgets import QMessageBox, QListWidgetItem

from string_cheks import StringCheck

from Screens.styles import *

from Screens.home import HomeScreen

from Model.database import Database

class StartScreen():
    def __init__(self, theme):
        self.defined_theme = None
        if theme == "Light Theme":
            self.defined_theme = LightTheme()
        elif theme == "Dark Theme":
            self.defined_theme = DarkTheme()
        else:
            self.defined_theme = LightTheme()

        self._list_project = []

    #conexoes dos botoes, entradas, etc a suas respectivas açoes
    def action_connect_start(self):
        if self.defined_theme.theme_description == "Light Theme":
            self.claro_radio_btn.setChecked(True)
            self.escuro_radio_btn.setChecked(False)
        elif self.defined_theme.theme_description == "Dark Theme":
            self.escuro_radio_btn.setChecked(True)
            self.claro_radio_btn.setChecked(False)

        self.del_btn.setVisible(False)
        self.load_projects()

        self.claro_radio_btn.clicked.connect(self.set_light_theme)
        self.escuro_radio_btn.clicked.connect(self.set_dark_theme)
        self.criar_btn.clicked.connect(self.save_project)
        self.carregar_btn.clicked.connect(self.show_home_screen)
        self.projetos_list_view.itemClicked.connect(self.show_delete_btn)

        self.del_btn.clicked.connect(self.delete_project)

    #exibir segunda tela
    def show_home_screen(self):
        if self.projetos_list_view.currentRow() != -1:
            self.home_window = QtWidgets.QMainWindow()
            self.ui = HomeScreen(self.defined_theme, self.projetos_list_view.currentItem().text())
            self.ui.setupUi(self.home_window)
            self.home_window.show()

    #temas
    def set_light_theme(self):
        self.show_dialog('Tema CLARO definido. Reinicie a aplicaçao para aplicar', "Tema")
        self.save_theme("Light Theme")

    def set_dark_theme(self):
        self.show_dialog('Tema ESCURO definido. Reinicie a aplicaçao para aplicar', 'Tema')
        self.save_theme("Dark Theme")

    def save_theme(self, theme):
        try:
            arquivo = open("config.dat", "w")
            arquivo.write(theme)
        except:
            self.show_dialog("Erro ao salvar...", "erro")

    #projeto
    def save_project(self):
        project_id = self.titulo_projeto_input.text()

        if project_id in self._list_project:
            self.show_dialog(f"Já existe um projeto com o nome \"{project_id}\"", "Projeto existente !!")
        else:
            if not StringCheck.is_space_or_null(project_id):
                item = QListWidgetItem()
                item.setText(project_id)
                item.setTextAlignment(Qt.AlignHCenter)
                self.projetos_list_view.addItem(item)
                self._list_project.append(item)
                try:
                    arq = open("projects.dat", "a")
                    arq.write(item.text() + "\n")
                except:
                    pass

        self.titulo_projeto_input.setText("")

    def delete_project(self):
        if self.projetos_list_view.currentRow() != -1:

            row = self.projetos_list_view.currentRow()
            project_id = self.projetos_list_view.currentItem().text()
            self._list_project.pop(row)

            self.projetos_list_view.takeItem(self.projetos_list_view.currentRow())
            self.projetos_list_view.clearSelection()

            db = Database()
            db.delete_project(project_id)

            self.del_btn.setEnabled(False)
            self.del_btn.setVisible(False)

            try:
                arq = open("projects.dat", "w") #apaga e reescreve no arquivo, mais sem o dado que foi removido
                arq = open ("projects.dat", "a")

                for project in self._list_project:
                    arq.write(project+"\n")

            except:
                pass

    def load_projects(self):

        try:
            arq = open("projects.dat", "r")
            list_project = arq.readlines()

            if len(list_project) > 0:
                for project in list_project:
                    item = QListWidgetItem()
                    it = project.removesuffix('\n')
                    item.setText(it)
                    item.setTextAlignment(Qt.AlignHCenter)
                    self.projetos_list_view.addItem(item)
                    self._list_project.append(it)
        except:
            pass


    def show_delete_btn(self):
        self.del_btn.setEnabled(True)
        self.del_btn.setVisible(True)

    def show_dialog(self, mensage, title):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(mensage)
        msg.setWindowTitle(title)
        msg.setStandardButtons(QMessageBox.Ok)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Assets/icone.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        msg.setWindowIcon(icon)
        retval = msg.exec_()

    def setupUi(self, StartScreen):

        StartScreen.setObjectName("ProjectStart")
        StartScreen.setEnabled(True)
        StartScreen.resize(640, 480)
        StartScreen.setMinimumSize(QtCore.QSize(640, 480))
        StartScreen.setMaximumSize(QtCore.QSize(640, 480))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        StartScreen.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Assets/icone.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        StartScreen.setWindowIcon(icon)
        StartScreen.setStyleSheet(self.defined_theme.style_background())
        self.centralwidget = QtWidgets.QWidget(StartScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.title_lbl = QtWidgets.QLabel(self.centralwidget)
        self.title_lbl.setStyleSheet(self.defined_theme.style_project_title())
        self.title_lbl.setObjectName("title_lbl")
        self.horizontalLayout.addWidget(self.title_lbl)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.tema_lbl = QtWidgets.QLabel(self.centralwidget)
        self.tema_lbl.setStyleSheet(self.defined_theme.style_info())
        self.tema_lbl.setObjectName("tema_lbl")
        self.horizontalLayout.addWidget(self.tema_lbl, 0, QtCore.Qt.AlignVCenter)
        self.claro_radio_btn = QtWidgets.QRadioButton(self.centralwidget)
        self.claro_radio_btn.setStyleSheet("QRadioButton\n" "{\n" " font-size: 12px;\n" "color: #757CA5;\n" " font-weight: bold;\n" "}")
        self.claro_radio_btn.setText("")
        self.claro_radio_btn.setChecked(True)
        self.claro_radio_btn.setObjectName("claro_radio_btn")
        self.horizontalLayout.addWidget(self.claro_radio_btn)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setStyleSheet(self.defined_theme.style_radio_button())
        self.pushButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Assets/sol.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(24, 24))
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem1 = QtWidgets.QSpacerItem(16, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.escuro_radio_btn = QtWidgets.QRadioButton(self.centralwidget)
        self.escuro_radio_btn.setStyleSheet(self.defined_theme.style_radio_button())
        self.escuro_radio_btn.setText("")
        self.escuro_radio_btn.setObjectName("escuro_radio_btn")
        self.horizontalLayout.addWidget(self.escuro_radio_btn)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setStyleSheet("QPushButton\n" "{\n" "background: transparent; \n" "padding: 0;\n" "}")
        self.pushButton_2.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Assets/noite.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.projetos_list_view = QtWidgets.QListWidget(self.centralwidget)

        self.projetos_list_view.setStyleSheet(self.defined_theme.style_list_widget())
        self.projetos_list_view.setObjectName("projetos_list_view")
        self.verticalLayout.addWidget(self.projetos_list_view)

        self.del_btn = QtWidgets.QPushButton(self.centralwidget)
        self.del_btn.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.del_btn.sizePolicy().hasHeightForWidth())

        self.del_btn.setSizePolicy(sizePolicy)
        self.del_btn.setStyleSheet(self.defined_theme.style_background())
        self.del_btn.setFlat(False)
        self.del_btn.setObjectName("del_btn")
        self.verticalLayout.addWidget(self.del_btn, alignment=QtCore.Qt.AlignRight)
        icon_del = QtGui.QIcon()
        icon_del.addPixmap(QtGui.QPixmap("Assets/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.del_btn.setIcon(icon_del)
        self.del_btn.setIconSize(QtCore.QSize(30, 30))
        self.del_btn.setStyleSheet(self.defined_theme.style_action_button())

        self.carregar_btn = QtWidgets.QPushButton(self.centralwidget)
        self.carregar_btn.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.carregar_btn.sizePolicy().hasHeightForWidth())
        self.carregar_btn.setSizePolicy(sizePolicy)
        self.carregar_btn.setStyleSheet(self.defined_theme.style_button())
        self.carregar_btn.setFlat(False)
        self.carregar_btn.setObjectName("carregar_btn")
        self.verticalLayout.addWidget(self.carregar_btn)

        spacerItem2 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem2)
        self.titulo_projeto_input = QtWidgets.QLineEdit(self.centralwidget)
        self.titulo_projeto_input.setStyleSheet(self.defined_theme.style_input())
        self.titulo_projeto_input.setMaxLength(50)
        self.titulo_projeto_input.setAlignment(QtCore.Qt.AlignCenter)
        self.titulo_projeto_input.setObjectName("titulo_projeto_input")
        self.verticalLayout.addWidget(self.titulo_projeto_input)
        self.criar_btn = QtWidgets.QPushButton(self.centralwidget)
        self.criar_btn.setStyleSheet(self.defined_theme.style_button())
        self.criar_btn.setObjectName("criar_btn")
        self.verticalLayout.addWidget(self.criar_btn, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        StartScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(StartScreen)

        self.action_connect_start()

        QtCore.QMetaObject.connectSlotsByName(StartScreen)

    def retranslateUi(self, ProjectStart):
        _translate = QtCore.QCoreApplication.translate
        ProjectStart.setWindowTitle(_translate("ProjectStart", "Tarefas Sequenciais"))
        self.title_lbl.setText(_translate("ProjectStart", "Seus projetos"))
        self.tema_lbl.setText(_translate("ProjectStart", "Escolher tema: "))
        self.claro_radio_btn.setToolTip(_translate("ProjectStart", "Define o tema do aplicativo para a cor clara. Recomendado para uso Diurno"))
        self.escuro_radio_btn.setToolTip(_translate("ProjectStart", "<html><head/><body><p>Define o tema do aplicativo para a cor escura. Recomendado para uso Noturno</p></body></html>"))
        self.projetos_list_view.setToolTip(_translate("ProjectStart", "Lista do seus projetos salvos até o momento"))
        self.carregar_btn.setToolTip(_translate("ProjectStart", "Carrega um projeto selecionado"))
        self.carregar_btn.setText(_translate("ProjectStart", "CARREGAR "))
        self.titulo_projeto_input.setPlaceholderText(_translate("ProjectStart", "Digite um titulo de projeto"))
        self.criar_btn.setToolTip(_translate("ProjectStart", "<html><head/><body><p>Cria um novo projeto com o titulo definido na caixa de texto</p></body></html>"))
        self.criar_btn.setText(_translate("ProjectStart", "CRIAR"))

    def show(self):
        import sys
        app = QtWidgets.QApplication(sys.argv)
        ProjectStart = QtWidgets.QMainWindow()
        ui = StartScreen(self.defined_theme.theme_description)
        ui.setupUi(ProjectStart)
        ProjectStart.show()
        sys.exit(app.exec_())