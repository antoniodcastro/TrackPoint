from core import log
import pyautogui as py
from time import sleep

class ScrollManager:
    def __init__(self, window_controller):
        
        # Gerenciador de scroll
        """
        Args:
            window_controller (WindowController): Controlador de janela
        """ 
        self.window_controller = window_controller
        self._valor_scroll = 0
        self._historico_scrolls = []

    def set_valor(self, valor):

        # Define o valor de scroll
        """
        Args:
            valor (int): Valor do scroll
        """
        self._valor_scroll = valor
        self._historico_scrolls.append(valor)

    def get_valor(self):

        # Obtém o valor atual de scroll
        """
        Returns:
            int: Valor de scroll
        """
        return self._valor_scroll

    def executar_scroll_teste(self):
        # Executa o scroll 

        # Log de início do scroll
        log.add_log('INFO', 'Foi Clicado para testar o scroll')
        
        # Obtém o tempo de espera do log
        numero = log.ler_numero_primeira_linha(log.app_state)
        
        # Minimiza a janela
        self.window_controller.minimize()
        
        # Tempo de espera
        sleep(numero)
        
        # Executa o scroll
        py.scroll(self._valor_scroll)
        
        # Log do scroll
        log.add_log('INFO', f'Foi testado um scroll de {self._valor_scroll}')
        
        # Tempo adicional
        sleep(2)
        
        # Maximiza a janela
        self.window_controller.maximize()

    def salvar_scroll(self):
        """
        Salva o valor atual de scroll no log
        """
        log.add_log('INFO', 'Foi clicado para salvar scroll')
        log.add_log_app('[Scroll]:', f"{self._valor_scroll}")