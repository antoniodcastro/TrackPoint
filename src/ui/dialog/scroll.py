import flet as ft
import os

class ScrollTestManager:
    def __init__(self, page, scroll_manager, sty):
        """
        :para page: Instância da página do Flet.
        :para scroll_manager: Instância do ScrollManager para gerenciar o scroll.
        :para ass: Variáveis de estilo.
        """
        self.page = page
        self.scroll_manager = scroll_manager
        self.sty = sty

        # Campo de texto para o valor do scroll
        self.scroll_tempo = ft.TextField(label="", border_color=self.sty.color_branco)

        # Dialog para capturar o valor do scroll
        self.dialog_scroll = ft.AlertDialog(
            modal=True,
            title=ft.Text("Digite um valor, para definir o scroll"),
            actions=[
                self.scroll_tempo,
                ft.Row(
                    controls=[
                        ft.ElevatedButton(
                            "Testa",
                            on_click=self.salvar_scroll,
                            bgcolor=self.sty.color_branco,
                            color=self.sty.color_preto_d1
                        ),
                        ft.ElevatedButton(
                            "Cancelar",
                            on_click=self.fechar_scroll,
                            bgcolor=self.sty.color_branco,
                            color=self.sty.color_preto_d1
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

        # Dialog para confirmar se deseja salvar o valor do scroll
        self.dialog_salva_scroll = ft.AlertDialog(
            modal=True,
            title=ft.Text("Deseja salvar o scroll usado?"),
            actions=[
                ft.Row(
                    controls=[
                        ft.ElevatedButton(
                            "Salvar",
                            on_click=self.salva_scroll_alert,
                            bgcolor=self.sty.color_branco,
                            color=self.sty.color_preto_d1
                        ),
                        ft.ElevatedButton(
                            "Testa outro",
                            on_click=self.fechar_scroll_true,
                            bgcolor=self.sty.color_branco,
                            color=self.sty.color_preto_d1
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

    def abrir_scroll(self):
        """Abre o diálogo para inserir o valor do scroll."""
        self.page.overlay.append(self.dialog_scroll)
        self.dialog_scroll.open = True
        self.page.update()

    def fechar_scroll(self, e):
        """Fecha o diálogo de inserção do valor do scroll."""
        self.page.close(self.dialog_scroll)

    def salvar_scroll(self, e):
        """Salva o valor do scroll, executa o teste e fecha o diálogo."""
        try:
            novo_valor = int(self.scroll_tempo.value)  # Obtém o valor inserido
            self.scroll_manager.set_valor(novo_valor)  # Define o valor do scroll no manager
            self.page.close(self.dialog_scroll)  # Fecha o diálogo de input

            # Executa o teste do scroll
            self.scroll_manager.executar_scroll_teste()

            # Abre o diálogo de confirmação de salvar
            self.abrir_scroll_true()

        except ValueError:
            self.page.add(ft.Text("Por favor, insira um valor numérico válido."))
            self.page.update()

    def abrir_scroll_true(self, e=None):
        """Abre o diálogo perguntando se o usuário deseja salvar o scroll usado."""
        self.page.open(self.dialog_salva_scroll)
        self.page.update()

    def fechar_scroll_true(self, e):
        """Fecha o diálogo de confirmação de salvar e retorna ao teste."""
        self.page.close(self.dialog_salva_scroll)
        self.abrir_scroll()  # Reabre o diálogo para testar outro scroll

    def salva_scroll_alert(self, e=None):
        """Salva o valor do scroll no log e fecha o diálogo."""
        self.page.close(self.dialog_salva_scroll)
        self.page.update()
        self.scroll_manager.salvar_scroll()  # Salva o valor do scroll no log