# TrackPoint 🖱️

## Visão Geral

TrackPoint é uma aplicação desktop construída com Flet e Python que fornece ferramentas utilitárias para rastreamento de tela e interações. A aplicação oferece recursos para registro de logs, rastreamento de posição do mouse, teste de rolagem e detecção de resolução de monitores.

## Funcionalidades

- 🖥️ Controle de Janela (Minimizar/Maximizar)
- 🌟 Rastreamento de Posição do Mouse
- 📜 Teste de Rolagem (Scroll)
- 🖼️ Detecção de Resolução de Monitores
- 📊 Registro de Logs e Anotações Personalizadas

## Pré-requisitos

- Python 3.8+
- pip 

## Instalação

1. Clone o repositório:
```bash
git clone https://github.com/antoniodcastro/TrackPoint.git
cd TrackPoint
```

2. Crie um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # No Windows use `venv\Scripts\activate`
```

3. Instale as dependências:
```bash
pip install flet pyautogui screeninfo
```

## Componentes Principais

### Controlador de Janela
- Gerencia minimização e maximização de janelas
- Fornece controles básicos de interação com janelas

### Gerenciador de Posição do Mouse
- Captura e registra posições do cursor do mouse
- Permite nomear e rastrear localizações do cursor

### Gerenciador de Rolagem
- Permite teste e registro de rolagem
- Rastreia valores e histórico de rolagem

### Detector de Resolução de Monitor
- Recupera e registra informações sobre monitores conectados
- Fornece detalhes de resolução de tela

### Gerenciamento de Logs
- Cria e gerencia arquivos de log
- Suporta adição de anotações e rastreamento de informações relacionadas a tempo

## Uso

Execute a aplicação:
```bash
python main.py
```

### Recursos da Interface Principal
- Abrir Pasta de Logs
- Alterar Tempo de Espera
- Adicionar Anotações
- Capturar Posição do Mouse
- Testar Valores de Rolagem
- Verificar Resoluções de Monitores

## Personalização

- Modifique `util/utility.py` para cores e caminhos da UI
- Ajuste o comportamento de log em `util/log.py`

## Contribuição

1. Faça um fork do repositório
2. Crie sua branch de feature (`git checkout -b feature/Recurso`)
3. Commit suas alterações (`git commit -m 'Adiciona algum Recurso'`)
4. Envie para a branch (`git push origin feature/RecursoIncrivel`)
5. Abra um Pull Request
