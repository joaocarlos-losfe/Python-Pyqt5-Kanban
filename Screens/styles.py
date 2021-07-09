class LightTheme:
    def __init__(self):
        self._theme_description = "Light Theme"

    @property
    def theme_description(self):
        return self._theme_description

    def style_text_input(self):
        return """
                QTextEdit
                {
                    background: white;
                    padding: 5px;
                    border: 1px solid #111E61;
                    border-radius: 5px;
                    color: #757CA5;
                    font-size: 14px;
                    font-weight: bold;
                }
                """

    def style_action_button(self):
        return """
                QPushButton
                {
                    background-color: transparent;
                    color: white;
                    font-weight: bold;
                    padding: 5px;
                    font-size: 12px;
                    border-radius: 5px;
                    margin: 0px 5px;
                }

                QPushButton:hover
                {
                   background-color: #B4C0CE;
                }

                QPushButton:pressed 
                {
                     background-color: #85B2BC;     
                }
                """

    def style_radio_button(self):
        return """
                QRadioButton
                {
                    font-size: 12px;
                    color: #757CA5;
                    font-weight: bold;
                }
                """
    def style_text_info(self):
        return  """
                QLabel
                {
                    color: #757CA5;
                    font-size: 18px;
                    font-weight: bold;
                }
                """

    def style_list_widget(self):
        return """
                QListWidget
                {
                    background: white;
                    padding: 5px;
                    border: 4px solid #D7E0EF;
                    border-radius: 5px;
                    color: #757CA5;
                    font-size: 18px;
                    font-weight: bold;
                }
                """

    def style_input(self):
        return """
                QLineEdit
                {
                    background: white;
                    padding: 5px;
                    border: 4px solid #D7E0EF;
                    border-radius: 5px;
                    color: #757CA5;
                    font-size: 12px;
                    font-weight: bold;
                }
                """

    def style_info(self):
        return """
                QLabel
                {
                    color: #111E61;
                    font-size: 14px;
                    font-weight: bold;
                }
                """

    def style_project_title(self):
        return """
                QLabel
                {
                    color: #111E61;
                    font-size: 20px;
                }
                """

    def style_background(self):
        return "background: #F9FAFF;\n"

    def style_button(self):
        return """
                QPushButton
                {
                    background-color: #388BC7;
                    color: white;
                    font-weight: bold;
                    padding: 10px 30px ;
                    font-size: 14px;
                    border-radius: 15px;
                }

                QPushButton:hover
                {
                   background-color:#3D95A9;
                }

                QPushButton:pressed 
                {
                     background-color: #85B2BC;
                }
                """


class DarkTheme:
    def __init__(self):
        self._theme_description = "Dark Theme"

    @property
    def theme_description(self):
        return self._theme_description

    def style_text_input(self):
        return """
                QTextEdit
                {
                    background: #302E3B;
                    padding: 5px;
                    border: 1px solid #111E61;
                    border-radius: 5px;
                    color: white;
                    font-size: 14px;
                    font-weight: bold;
                }
                """

    def style_action_button(self):
        return """
                QPushButton
                {
                    background-color: transparent;
                    color: white;
                    font-weight: bold;
                    padding: 5px;
                    font-size: 12px;
                    border-radius: 5px;
                    margin: 0px 5px;
                }

                QPushButton:hover
                {
                   background-color:#2C3354;
                }

                QPushButton:pressed 
                {
                     background-color: #85B2BC;     
                }
                """

    def style_radio_button(self):
        return """
                   QRadioButton
                   {
                       font-size: 12px;
                       color: #757CA5;
                       font-weight: bold;
                   }
                   """

    def style_text_info(self):
        return  """
                QLabel
                {
                    color: white;
                    font-size: 18px;
                    font-weight: bold;
                }
                """

    def style_list_widget(self):
        return """
                   QListWidget
                    {
                        background: #302E3B;
                        padding: 5px;
                        border: 4px solid #D7E0EF;
                        border-radius: 5px;
                        color: white;
                        font-size: 18px;
                        font-weight: bold;
                    }
                   """

    def style_input(self):
        return """
                   QLineEdit
                    {
                        background: #302E3B;
                        padding: 5px;
                        border: 4px solid #D7E0EF;
                        border-radius: 5px;
                        color: white;
                        font-size: 12px;
                        font-weight: bold;
                    }
                   """

    def style_info(self):
        return """
                   QLabel
                    {
                        color: #8A888A;
                        font-size: 14px;
                        font-weight: bold;
                    }
                   """

    def style_project_title(self):
        return  """
                   QLabel
                    {
                        color: #FFFFFF;
                        font-size: 20px;
                    }
                   """

    def style_background(self):
        return "background: #1D1B28;\n"

    def style_button(self):
        return """
                   QPushButton
                   {
                       background-color: #1977BB;
                       color: white;
                       font-weight: bold;
                       padding: 10px 30px ;
                       font-size: 14px;
                       border-radius: 15px;
                   }

                   QPushButton:hover
                   {
                      background-color:#3D95A9;
                   }

                   QPushButton:pressed 
                   {
                        background-color: #85B2BC;
                   }
                   """