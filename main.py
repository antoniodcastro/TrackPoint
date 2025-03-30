import flet as ft
import pyautogui as py
import os
from time import sleep

log_tempo = 'log_tempo.txt'

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
    log_tempo = 'log_tempo.txt'
    with open(log_tempo, 'a', encoding='utf-8') as arquivo:  # Abre o arquivo em modo de adição
        arquivo.write(f"{mensagem}\n")  # Escreve a mensagem seguida por uma nova linha

def add_log_app(status, mensagem):
    mensagem = f"{status}: {mensagem}"
    log(mensagem)

# ======================================== Criar Log + tempo padrão
def criar_log_tempo(log_tempo):
    if not os.path.exists(log_tempo):
        with open (log_tempo, 'w')as arquivo:
            arquivo.write('Tempo: 5')
        add_log('SUCESSO', "Arquivo TrackPoint criado com sucesso.")
    else:
        add_log('INFO',"Arquivo TrackPoint já existe.")

# ======================================== Lê a primeira linha e remove espaços em branco
def ler_numero_primeira_linha(log_tempo):
    try:
        with open(log_tempo, 'r') as arquivo:
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

color_fundo = "#2E393F"
color_botao = '#483D8B'
color_branco = "#F2F2F2"
colo_titulo = '#4F6B77'
color_preto_d1 = "#1D2423"
color_fundo_bt = "#4F6B77"
caminho_img = "img/trackpoint.png"
caminho_ico = "img/trackpoint.png"

apagar = ft.ElevatedButton(text="Apagar", height=50, bgcolor=color_branco, color=color_preto_d1, width=200)
abrir = ft.ElevatedButton(text="Abrir", height=50, bgcolor=color_branco, color=color_preto_d1, width=200)
tempo = ft.ElevatedButton(text="Tempo", height=50, bgcolor=color_branco, color=color_preto_d1, width=200)

posicao_visualizar = ft.ElevatedButton(text="Roda", height=50, bgcolor=color_branco, color=color_preto_d1, width=300)
scroll_visualizar = ft.ElevatedButton(text="Roda", height=50, bgcolor=color_branco, color=color_preto_d1, width=300)

conteudo_posicao = ft.Row(
    controls=[
        ft.Container(ft.Text('Posição'),scale=1.5,expand=True,alignment= ft.alignment.center),
        ft.Container(content=posicao_visualizar,expand=True, alignment=ft.alignment.center_right)
    ],
    alignment=ft.MainAxisAlignment.CENTER,
    spacing=60
)
conteudo_scroll = ft.Row(
    controls=[
        ft.Container(ft.Text('Scroll'),scale=1.5,expand=True,alignment= ft.alignment.center),
        ft.Container(content=scroll_visualizar,expand=True, alignment=ft.alignment.center_right)
    ],
    alignment=ft.MainAxisAlignment.CENTER,
    spacing=60
)

# ======================================== Abrir Pasta Log
def abrir_pasta_log():
    add_log('INFO','Foi Clicado para abre a pasto onde o Log está')
    pasta = os.path.dirname(os.path.abspath(log_tempo))  
    os.startfile(pasta)  

# ======================================== Alterar tempo
def alterar_tempo(novo_numero):
    add_log('INFO','Foi Clicado para alterar o tempo')
    try:
        with open(log_tempo, 'r+', encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()  # Lê todas as linhas do arquivo
            if linhas and linhas[0].startswith("Tempo:"):
                # Atualiza o número na primeira linha
                linhas[0] = f"Tempo: {novo_numero}\n"
                
                # Volta para o início do arquivo e reescreve o conteúdo
                arquivo.seek(0)
                arquivo.writelines(linhas)
                arquivo.truncate()  # Remove qualquer dado que sobra após a nova escrita
            else:
                add_log('ERROR',"O formato da primeira linha não é o esperado.")
    except FileNotFoundError:
       add_log('ERROR',f"O arquivo do TrackPoint não foi encontrado.")
    except Exception as e:
        add_log('ERROR',f"Ocorreu um erro: {e}")

# ======================================== Pega posição do mouse
def pega_posicao(novo_nome, e):
    add_log('INFO','Foi Clicado para localizar uma posição')
    numero = ler_numero_primeira_linha(log_tempo)
    minimize(e)
    sleep(numero)
    posicao = py.position()
    add_log_app('INFO',f"{novo_nome}: {posicao}")
    maximize(e)

# ======================================== Testa Scroll
class ScrollManager:
    def __init__(self):
        self.valor = 0

    def set_valor(self, novo_valor):
        self.valor = novo_valor

    def get_valor(self):
        return self.valor

scroll_manager = ScrollManager()

def scroll_teste(e):
    global valor_atual_scroll
    valor_atual_scroll = scroll_manager.get_valor()
    add_log('INFO', 'Foi Clicado para testar o scroll')
    numero = ler_numero_primeira_linha(log_tempo)
    minimize(e)
    sleep(numero)
    py.scroll(valor_atual_scroll)
    add_log('INFO', f'Foi testado um scroll de {valor_atual_scroll}')
    maximize(e)
    abrir_scroll_true()

def salvar_scroll_certo(e):
    add_log('INFO','Foi clicado para salva scroll')
    valor_atual_scroll = scroll_manager.get_valor()
    add_log_app('INFO',f"{valor_atual_scroll}")

# ======================================== App
def main(page: ft.Page) -> None:
    global minimize, maximize, abrir_scroll_true
    criar_log()
    criar_log_tempo(log_tempo)
    global scroll_manager
    scroll_manager = ScrollManager()
    page.title = "TrackPoint"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = color_fundo
    page.window.width = 1000
    page.window.height = 800
    page.window.resizable = False
    page.window.maximizable = False
    page.window.icon = caminho_img
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.fonts = {
        "YaroOp-Bold": "assets/fonts/YaroOp-Bold.ttf",
    }
    page.theme = ft.Theme(font_family="YaroOp-Bold")

    img_trackpoint = ft.Image(src=caminho_img, width=350, height=200)

    def minimize(e):
        page.window.minimized = True
        page.update()

    def maximize(e):
        page.window.minimized = False
        page.update()



# ======================================== Alterar tempo
    def fechar_novo_tempo(e):
        page.close(dialog_nova_tempo)
        
    def salvar_novo_tempo(e):
        novo_numero = novo_tempo.value  
        add_log('INFO', f'Foi alterado tempo de espera para: {novo_numero}')
        page.close(dialog_nova_tempo)
        alterar_tempo(novo_numero)
        page.update()

    def abrir_novo_tempo():
        page.overlay.append(dialog_nova_tempo)
        dialog_nova_tempo.open = True
        page.update()

    novo_tempo = ft.TextField(label="", border_color=color_branco)
    dialog_nova_tempo = ft.AlertDialog(
        modal=True,
        title=ft.Text("Digiter um valor, para definir o tempo de espera"),
        actions=[
            novo_tempo,
            ft.Row(
                controls=[
                    ft.ElevatedButton(
                        "Salvar",
                        on_click=salvar_novo_tempo,
                        bgcolor=color_branco,
                        color=color_preto_d1
                    ),
                    ft.ElevatedButton(
                        "Cancelar",
                        on_click=fechar_novo_tempo,
                        bgcolor=color_branco,
                        color=color_preto_d1
                    ),
                ],
                alignment=ft.MainAxisAlignment.END,
                spacing=50,
                height=70
            )
        ],
        actions_alignment=ft.MainAxisAlignment.END,

        inset_padding=20
    )

# ======================================== Pega posição do mouse

    def fechar_novo_nome(e):
        page.close(dialog_name)
        
    def salvar_novo_nome(e):
        novo_nome = nome.value  
        page.close(dialog_name)
        pega_posicao(novo_nome,e)

    def abrir_novo_nome():
        page.overlay.append(dialog_name)
        dialog_name.open = True
        page.update()

    nome = ft.TextField(label="", border_color=color_branco)
    dialog_name = ft.AlertDialog(
        modal=True,
        title=ft.Text("Der um nome"),
        actions=[
            nome,
            ft.Row(
                controls=[
                    ft.ElevatedButton(
                        "Salvar",
                        on_click=salvar_novo_nome,
                        bgcolor=color_branco,
                        color=color_preto_d1
                    ),
                    ft.ElevatedButton(
                        "Cancelar",
                        on_click=fechar_novo_nome,
                        bgcolor=color_branco,
                        color=color_preto_d1
                    ),
                ],
                alignment=ft.MainAxisAlignment.END,
                spacing=50,
                height=70
            )
        ],
        actions_alignment=ft.MainAxisAlignment.END,

        inset_padding=20
    )

# ======================================== teste pega scroll

    def fechar_scroll(e):
        page.close(dialog_scroll)
        
    def salvar_scroll(e):
        novo_valor = int(scroll_tempo.value)
        scroll_manager.set_valor(novo_valor)
        page.close(dialog_scroll)
        scroll_teste(e)

    def abrir_scroll():
        page.overlay.append(dialog_scroll)
        dialog_scroll.open = True
        page.update()

    scroll_tempo = ft.TextField(label="", border_color=color_branco)
    dialog_scroll = ft.AlertDialog(
        modal=True,
        title=ft.Text("Digite um valor, para definir o scroll"),
        actions=[
            scroll_tempo,
            ft.Row(
                controls=[
                    ft.ElevatedButton(
                        "testa",
                        on_click=salvar_scroll,
                        bgcolor=color_branco,
                        color=color_preto_d1
                    ),
                    ft.ElevatedButton(
                        "Cancelar",
                        on_click=fechar_scroll,
                        bgcolor=color_branco,
                        color=color_preto_d1
                    ),
                ],
                alignment=ft.MainAxisAlignment.END,
                spacing=50,
                height=70
            )
        ],
        actions_alignment=ft.MainAxisAlignment.END,

        inset_padding=20
    )

# ======================================== Salvar Valor do Scroll

    def fechar_scroll_true(e):
        page.close(dialog_salva_scroll)
        abrir_scroll()

    def abrir_scroll_true(e=None):
        page.open(dialog_salva_scroll)
        page.update()

    def salva_scroll_alert(e=None):
        page.close(dialog_salva_scroll)
        page.update()
        salvar_scroll_certo(e)

    dialog_salva_scroll = ft.AlertDialog(
        modal=True,
        title=ft.Text("Deseja salva o scroll usado ?"),
        actions=[
            ft.Row(
                controls=[
                    ft.ElevatedButton(
                        "Salva",
                        on_click=salva_scroll_alert,
                        bgcolor=color_branco,
                        color=color_preto_d1
                    ),
                    ft.ElevatedButton(
                        "Testa outro",
                        on_click=fechar_scroll_true,
                        bgcolor=color_branco,
                        color=color_preto_d1
                    ),
                ],
                alignment=ft.MainAxisAlignment.END,
                spacing=50,
                height=70
            )
        ],
        actions_alignment=ft.MainAxisAlignment.END,

        inset_padding=20
    )

# ======================================== Coluna
    coluna = ft.Column(
        controls=[
            img_trackpoint,
            ft.Row(
                controls=[
                    ft.Container(content=abrir, expand=True, alignment=ft.alignment.top_right),
                    ft.Container(content=tempo, expand=True, alignment=ft.alignment.top_left),
                ],
                spacing=200,
            ),
            ft.Container(content=conteudo_posicao,padding=30,border_radius=10 ,bgcolor=color_fundo_bt, width=700, alignment=ft.alignment.center),
            ft.Container(content=conteudo_scroll,padding=30,border_radius=10 ,bgcolor=color_fundo_bt, width=700, alignment=ft.alignment.center),
            ft.Container(expand=True)      
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=20,
        expand=True,
    )
    
    page.add(coluna)
    page.update()

    abrir.on_click = lambda _: abrir_pasta_log ()
    tempo.on_click = lambda _: abrir_novo_tempo ()
    posicao_visualizar.on_click = lambda _: abrir_novo_nome()
    scroll_visualizar.on_click = lambda _: abrir_scroll()

ft.app(target=main, assets_dir="assets")