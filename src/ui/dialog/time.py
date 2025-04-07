import flet as ft

class TimeDialog:
    def __init__(self, page, log, log_manager, ass):
        """
        :para page: Instância da página do Flet.
        :para log: Instância do logger.
        :para mod: Módulo para alterar o tempo.
        :para ass: Variáveis auxiliares.
        """
        self.page = page
        self.log = log
        self.log_manager = log_manager
        self.ass = ass

        # Campo de texto para o novo tempo
        self.novo_tempo = ft.TextField(label="", border_color=self.ass.color_branco)

        # Dialog
        self.dialog_nova_tempo = ft.AlertDialog(
            modal=True,
            title=ft.Text("Digite um valor, para definir o tempo de espera"),
            actions=[
                self.novo_tempo,
                ft.Row(
                    controls=[
                        ft.ElevatedButton(
                            "Salvar",
                            on_click=self.salvar_novo_tempo,
                            bgcolor=self.ass.color_branco,
                            color=self.ass.color_preto_d1
                        ),
                        ft.ElevatedButton(
                            "Cancelar",
                            on_click=self.fechar_novo_tempo,
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
        """Abre o diálogo para alteração do tempo."""
        self.page.overlay.append(self.dialog_nova_tempo)
        self.dialog_nova_tempo.open = True
        self.page.update()

    def fechar_novo_tempo(self, e=None):
        """Fecha o diálogo de alteração do tempo."""
        self.page.close(self.dialog_nova_tempo)
        self.page.update()

    def salvar_novo_tempo(self, e=None):
        """Salva o novo tempo inserido e fecha o diálogo."""
        novo_numero = self.novo_tempo.value
        self.log.add_log('INFO', f'Foi alterado tempo de espera para: {novo_numero}')
        self.log_manager.alterar_tempo(novo_numero)
        self.fechar_novo_tempo()