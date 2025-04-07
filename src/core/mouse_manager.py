from core import log
import pyautogui as py
from time import sleep

class MousePositionManager:
    def __init__(self, window_controller):
        # Gerenciador de captura de posição do mouse
        """
        Args:
            window_controller (WindowController): Controlador de janela
        """
        self.window_controller = window_controller

    def capturar_posicao(self, novo_nome):
        # Captura a posição do mouse 
        """
        Args:
            novo_nome (str): Nome para identificar a captura
        
        Returns:
            tuple: Coordenadas (x, y) da posição do mouse
        """
        # Log de início da captura
        log.add_log('INFO', 'Foi Clicado para localizar uma posição')
        
        # Obtém o tempo de espera do log
        numero = log.ler_numero_primeira_linha(log.app_state)
        
        # Minimiza a janela
        self.window_controller.minimize()
        
        # Tempo de espera
        sleep(numero)
        
        # Captura a posição do mouse
        posicao = py.position()
        
        # Log da posição
        log.add_log_app('[Posicão]:', f"{novo_nome}: {posicao}")
        
        # Maximiza a janela
        self.window_controller.maximize()
        
        return posicao