import flet as ft
from ui import sty

class Botao(ft.ElevatedButton):
    def __init__(self, texto):  
        super().__init__(text=texto, width=200, bgcolor=sty.color_branco, color=sty.color_preto_d1)      

abrir =  Botao(texto="Abrir")
tempo =  Botao(texto="Tempo")
anotacao =  Botao(texto="Anotar")

posicao_visualizar = Botao(texto="Executar")
scroll_visualizar = Botao(texto="Executar")
resolucao = Botao(texto="Executar")

# ======================================= conteudos
class Container(ft.Container):
    def __init__(self, conteudo):  
        super().__init__(content=conteudo , padding=10 ,border_radius=10 ,bgcolor=sty.color_fundo_bt, width=618, alignment=ft.alignment.center),


# ======================================= Colunas
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

conteudo_resolucao = ft.Row(
    controls=[
        ft.Container(ft.Text('Resolução'),scale=1.5,expand=True,alignment= ft.alignment.center),
        ft.Container(content=resolucao,expand=True, alignment=ft.alignment.center_right)
    ],
    alignment=ft.MainAxisAlignment.CENTER,
    spacing=60
)