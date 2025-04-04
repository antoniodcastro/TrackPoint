import os 
from core import log

class LogManager:
    def __init__(self, log):
        """        
        :para log: Instância do logger usada para registrar eventos.
        """
        self.log = log
        self.app_state = log.app_state  # Caminho do arquivo de log de tempo

    def abrir_pasta_log(self):
        """
        Abre a pasta onde o arquivo de log está localizado.
        """
        self.log.add_log('INFO', 'Foi clicado para abrir a pasta onde o Log está')
        try:
            # Obtém o caminho absoluto da pasta onde o arquivo de log está
            pasta = os.path.dirname(os.path.abspath(self.app_state))
            os.startfile(pasta)  # Abre a pasta no explorador de arquivos
        except Exception as e:
            self.log.add_log('ERROR', f"Erro ao abrir a pasta do log: {e}")

    def alterar_tempo(self, novo_numero):
        """
        Altera o valor do tempo registrado no arquivo de log.
    
        :para novo_numero: Novo valor do tempo a ser registrado.
        """
        self.log.add_log('INFO', 'Foi clicado para alterar o tempo')
        try:
            # Abre o arquivo de log em modo leitura e escrita
            with open(self.app_state, 'r+', encoding='utf-8') as arquivo:
                linhas = arquivo.readlines()  # Lê todas as linhas do arquivo

                if linhas and linhas[0].startswith("Tempo:"):
                    # Atualiza o número na primeira linha
                    linhas[0] = f"Tempo: {novo_numero}\n"
                    
                    # Volta para o início do arquivo e reescreve o conteúdo
                    arquivo.seek(0)
                    arquivo.writelines(linhas)
                    arquivo.truncate()  # Remove qualquer dado que sobra após a nova escrita
                    self.log.add_log('INFO', f"Tempo alterado para: {novo_numero}")
                else:
                    self.log.add_log('ERROR', "O formato da primeira linha não é o esperado.")
        except FileNotFoundError:
            self.log.add_log('ERROR', f"O arquivo de log não foi encontrado.")
        except Exception as e:
            self.log.add_log('ERROR', f"Ocorreu um erro ao alterar o tempo: {e}")

    def adicionar_anotacao(self, anotacao):
        """
        :para anotacao: Texto da anotação a ser registrada.
        """
        self.log.add_log('INFO', 'Foi clicado para adicionar uma anotação no log')
        try:
            # Abre o arquivo de log no modo de anexo
            with open(self.app_state, 'a', encoding='utf-8') as arquivo:
                # Escreve a anotação no final do arquivo com quebra de linha
                arquivo.write(f"INFO: {anotacao}\n")
                self.log.add_log('INFO', f"Anotação adicionada: {anotacao}")
        except FileNotFoundError:
            self.log.add_log('ERROR', f"O arquivo de log não foi encontrado.")
        except Exception as e:
            self.log.add_log('ERROR', f"Ocorreu um erro ao adicionar a anotação: {e}")