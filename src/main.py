import flet as ft
from core import LogManager,log,WindowController, ScrollManager,MousePositionManager,MonitorResolucao,detect
from ui import TimeDialog,NameDialog,ScrollTestManager,SalvaAnotacao,sty,comp
from config import cam

# ======================================== App
def main(page: ft.Page) -> None:
    log.criar_log()
    log.criar_app_state(log.app_state)  

    log_manager = LogManager(log)

    window_controller = WindowController(page)
    mouse_manager = MousePositionManager(window_controller)
    scroll_manager = ScrollManager(window_controller)
    monitor = MonitorResolucao(log_manager)

    scroll_test_manager = ScrollTestManager(page, scroll_manager, sty)
    time_dialog = TimeDialog(page, log, log_manager, sty)
    name_dialog = NameDialog(page, mouse_manager, sty)
    anotacao = SalvaAnotacao(page, log, log_manager, sty)
    
    detect(page)
    
    page.title = "TrackPoint"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = sty.color_fundo
    page.window.width = 700        
    page.window.height = 500        
    page.window.icon = cam.caminho_img
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 0

    page.fonts = {
        "YaroOp-Bold": "assets/fonts/YaroOp-Bold.ttf",
    }
    page.theme = ft.Theme(font_family="YaroOp-Bold")

    img_trackpoint = ft.Image(
        src=cam.caminho_img, 

    )

    fundo = ft.Container(
        image=ft.DecorationImage(
            src=cam.caminho_fundo,
            fit=ft.ImageFit.COVER,
            alignment=ft.alignment.center,
            ),
        expand=True,
    )
# ======================================== Coluna
    coluna = ft.Column(
        controls=[
            ft.Container(),
            img_trackpoint,
            ft.Row(
                controls=[
                    ft.Container(content=comp.abrir, expand=True, alignment=ft.alignment.top_right),
                    ft.Container(content=comp.anotacao, alignment=ft.alignment.center), 
                    ft.Container(content=comp.tempo, expand=True, alignment=ft.alignment.top_left),
                ],
            ),
            comp.Container(conteudo=comp.conteudo_posicao),
            comp.Container(conteudo=comp.conteudo_scroll),
            comp.Container(conteudo=comp.conteudo_resolucao), 
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=20,
        expand=True,
        
    )
    
    page.add(
        ft.Container( 
            expand=True,
            content=ft.Stack(
                controls=[
                    fundo,
                    coluna
                ]
            ),
        )
    )
    page.update()

    comp.abrir.on_click = lambda _: log_manager.abrir_pasta_log ()
    comp.tempo.on_click = lambda _: time_dialog.abrir()
    comp.anotacao.on_click = lambda _: anotacao.abrir_dialogo_anotacao()
    comp.posicao_visualizar.on_click = lambda _: name_dialog.abrir()
    comp.scroll_visualizar.on_click = lambda _: scroll_test_manager.abrir_scroll()
    comp.resolucao.on_click = lambda _: monitor.obter_resolucao()

ft.app(target=main, assets_dir="assets")