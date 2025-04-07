import flet as ft

class NameDialog:
    def __init__(self, page, mouse_manager, ass):
        """
        :para page: Instância da página do Flet.
        :para mouse_manager: Gerenciador de mouse, responsável por capturar a posição.
        :para ass: Variáveis auxiliares (ex: cores, caminhos).
        """
        self.page = page
        self.mouse_manager = mouse_manager
        self.ass = ass

        # Campo de texto para capturar o nome
        self.nome = ft.TextField(label="", border_color=self.ass.color_branco)

        # Definição do diálogo
        self.dialog_name = ft.AlertDialog(
            modal=True,
            title=ft.Text("Digite um nome"),
            actions=[
                self.nome,
                ft.Row(
                    controls=[
                        ft.ElevatedButton(
                            "Salvar",
                            on_click=self.salvar_novo_nome,
                            bgcolor=self.ass.color_branco,
                            color=self.ass.color_preto_d1
                        ),
                        ft.ElevatedButton(
                            "Cancelar",
                            on_click=self.fechar_novo_nome,
                            bgcolor=self.ass.color_branco,
                            color=self.ass.color_preto_d1
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

    def abrir(self):
        """
        Abre o diálogo para captura do nome.
        """
        self.page.overlay.append(self.dialog_name)
        self.dialog_name.open = True
        self.page.update()

    def fechar_novo_nome(self, e=None):
        """
        Fecha o diálogo de captura do nome.
        """
        self.page.close(self.dialog_name)
        self.page.update()

    def salvar_novo_nome(self, e=None):
        """
        Captura o nome inserido e chama o método do mouse_manager para registrar a posição.
        """
        novo_nome = self.nome.value
        self.page.close(self.dialog_name)
        self.mouse_manager.capturar_posicao(novo_nome)
