import abc

class Istyles(abc.ABC):

    """
    define um estilo comum e padrão para
    cada tema criado e deve ser usado globalmente em toda a aplicação
    """

    @abc.abstractmethod
    def style_text_input(self):
        """retorna o estilo das caixas de entradas de texto longo"""


    @abc.abstractmethod
    def style_action_button(self):
        """estilo de botões de ações relacionadas as tarefas"""


    @abc.abstractmethod
    def style_radio_button(self):
        """estilo comun dos botões radiais"""


    @abc.abstractmethod
    def style_text_info(self):
        """define o estilo de textos fora das list view para apresentação de informações em lista"""


    @abc.abstractmethod
    def style_list_widget(self):
        """estilo das list views comuns"""


    @abc.abstractmethod
    def style_input(self):
        """retorna o estilo das caixas de entradas de texto simples e pequenos"""


    @abc.abstractmethod
    def style_info(self):
        """representação de informações indicando ao usuario"""


    @abc.abstractmethod
    def style_project_title(self):
        """estilo dos titulos"""


    @abc.abstractmethod
    def style_background(self):
        """plano de fundo base do aplicativo"""


    @abc.abstractmethod
    def style_button(self):
        """estilo de botões simples"""