class WindowController:
    def __init__(self, page):
        self.page = page

    def minimize(self, e=None):
        """Minimiza a janela."""
        self.page.window.minimized = True
        self.page.update()

    def maximize(self, e=None):
        """Maximiza a janela."""
        self.page.window.minimized = False
        self.page.update()