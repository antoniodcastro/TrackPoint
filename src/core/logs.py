import os

app_state = 'app_state.txt'

# ======================================== Criar log de Manutenção
def criar_log():
    mensagem = f"TrackPoint Iniciou"
    escrever_log(mensagem)

def escrever_log(mensagem):
    diretorio_logs = './assets/logs/system'
    if not os.path.exists(diretorio_logs):
        os.makedirs(diretorio_logs)
    arquivo_log = os.path.join(diretorio_logs, f"trackpoint.log")
    with open(arquivo_log, 'a+', encoding='utf-8') as log:
        log.write(f"{mensagem}\n")

def add_log(status, mensagem):
    mensagem = f"{status}: {mensagem}"
    escrever_log(mensagem)

# ======================================== Adcição de logs do app
def log(mensagem):
    app_state = 'app_state.txt'
    with open(app_state, 'a', encoding='utf-8') as arquivo:  # Abre o arquivo em modo de adição
        arquivo.write(f"{mensagem}\n")  # Escreve a mensagem seguida por uma nova linha

def add_log_app(status, mensagem):
    mensagem = f"{status}: {mensagem}"
    log(mensagem)

# ======================================== Criar Log + tempo padrão
def criar_app_state(app_state):
    if not os.path.exists(app_state):
        with open (app_state, 'w')as arquivo:
            arquivo.write('Tempo: 5')
        add_log('SUCESSO', "Arquivo TrackPoint criado com sucesso.")
    else:
        add_log('INFO',"Arquivo TrackPoint já existe.")

# ======================================== Lê a primeira linha e remove espaços em branco
def ler_numero_primeira_linha(app_state):
    try:
        with open(app_state, 'r') as arquivo:
            primeira_linha = arquivo.readline().strip()
            if primeira_linha.startswith("Tempo:"):
                numero = int(primeira_linha.split(":")[1].strip())
                return numero
            else:
                add_log('ERROR',"A primeira linha não está no formato esperado.")
    except FileNotFoundError:
        add_log('ERROR',"O arquivo do TrackPoint não foi encontrado.")
    except ValueError:
        add_log('ERROR',"Não foi possível converter o valor para um número.")
    except Exception as e:
        add_log('ERROR',f"Ocorreu um erro: {e}")