import flet as ft 
from .log import add_log

def detect (page: ft.Page):
    global system 

    system = ''

    if page.platform == ft.PagePlatform.LINUX:
        add_log('INFO', 'Aplicativo foi iniciado aparte de um dispositivo Linux')
        system = 'Linux'
        page.window.min_width = 700    
        page.window.min_height = 500   
        page.window.max_width = 800   
        page.window.max_height = 500   

    elif page.platform == ft.PagePlatform.WINDOWS:
        add_log('INFO', 'Aplicativo foi iniciado aparte de um dispositivo Windows')
        system = 'Win'
        page.window.resizable = False  
        page.window.maximizable = True 

    else:
        add_log('INFO', 'Adcionar Sua nova sistema.')