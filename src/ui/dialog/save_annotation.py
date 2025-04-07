import flet as ft

class SalvaAnotacao:
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
        self.nova_anotacao = ft.TextField(label="", border_color=self.ass.color_branco)

        # Dialog
        self.dialog_nova_anotacao = ft.AlertDialog(
            modal=True,
            title=ft.Text("Salva Sua anotacao"),
            actions=[
                self.nova_anotacao,
                ft.Row(
                    controls=[
                        ft.ElevatedButton(
                            "Salvar",
                            on_click=self.salvar_novo_anotacao,
                            bgcolor=self.ass.color_branco,
                            color=self.ass.color_preto_d1
                        ),
                        ft.ElevatedButton(
                            "Cancelar",
                            on_click=self.fechar_novo_anotacao,
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
    
    def abrir_dialogo_anotacao(self):
        """Abre o diálogo para alteração do tempo."""
        self.page.overlay.append(self.dialog_nova_anotacao)
        self.dialog_nova_anotacao.open = True
        self.page.update()

    def fechar_novo_anotacao(self, e=None):
        """Fecha o diálogo de alteração do tempo."""
        self.page.close(self.dialog_nova_anotacao)
        self.page.update()

    def salvar_novo_anotacao(self, e=None):
        """Salva o novo tempo inserido e fecha o diálogo."""
        anotacao = self.nova_anotacao.value
        self.log.add_log('[Anotacação]:', f'Foi alterado tempo de espera para: {anotacao}')
        self.log_manager.adicionar_anotacao(anotacao)
        self.fechar_novo_anotacao()




