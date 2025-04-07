from screeninfo import get_monitors

class MonitorResolucao:
    def __init__(self, log_manager):
        """
        Inicializa a classe e recebe o gerenciador de logs.
        """
        self.log_manager = log_manager
        self.monitores = get_monitors()  # Obtém informações de todos os monitores conectados

    def obter_resolucao(self):
        """
        Captura as resoluções de todos os monitores e registra no log.
        :return: Lista de resoluções dos monitores conectados.
        """
        self.log_manager.log.add_log('INFO', 'Foi clicado para verificar a resolução dos monitores')

        # Lista para armazenar informações de todos os monitores
        resolucoes = []
        for idx, monitor in enumerate(self.monitores):
            # Captura as dimensões do monitor
            resolucao = f"Monitor {idx + 1}: {monitor.width}x{monitor.height}s"
            resolucoes.append(resolucao)

            # Adiciona log e anotação para cada monitor
            self.log_manager.log.add_log('INFO', f"{resolucao}")
            self.log_manager.adicionar_anotacao(f"{resolucao}")
