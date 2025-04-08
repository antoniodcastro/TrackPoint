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

## Estrutura do Projeto

```plaintext
TrackPoint/
│
├── readme.md                           # 📘 Documentação principal do projeto: instalação e uso.
├── requirements.txt                    # 📦 Lista de dependências necessárias para o ambiente.
│
└── src/                                # 💻 Código-fonte da aplicação
    ├── __init__.py
    ├── main.py                         # 🧠 Arquivo principal da aplicação (ponto de entrada)
    ├── app_state.txt                   # 🗃️ Controla o tempo e armazena informações globais.
    │
    ├── assets/                         # 🖼️ Recursos estáticos (imagens, fontes, logs)
    │   ├── fonts/
    │   │   └── YaroOp-Bold.ttf         # Fonte personalizada usada na interface
    │   ├── img/
    │   │   ├── ico.ico
    │   │   ├── ico.png
    │   │   └── trackpoint.png          
    │   └── logs/                       # Arquivos de log gerados pela aplicação
    │
    ├── config/                         # ⚙️ Configurações globais do projeto
    │   ├── __init__.py
    │   └── paths.py                    # Caminhos de arquivos e diretórios
    │
    ├── core/                           # 🧩 Lógica central e funcionalidades principais
    │   ├── __init__.py
    │   ├── log_manager.py              # Gerencia logs: salvar, abrir, anotar, etc.
    │   ├── logs.py                     # Manipulação direta de arquivos de log
    │   ├── monito_resol.py             # Verificação da resolução dos monitores
    │   ├── mouse_manager.py            # Controle de posição e clique do mouse
    │   ├── scroll_manager.py           # Lógica de leitura/execução de scroll
    │   └── windows_controller.py       # Controle da janela (minimizar, maximizar)
    │
    ├── ui/                             # 🎨 Interface gráfica do usuário (UI)
    │   ├── __init__.py
    │   ├── components.py               # Componentes reutilizáveis (botões, containers customizados)
    │   ├── styles.py                   # Cores, fontes e estilos visuais padrão
    │   └── dialog/                     # 🗨️ Janelas de diálogo (modais)
    │       ├── name.py                 # Captura o nome da posição do mouse
    │       ├── save_annotation.py      # Adiciona anotações manuais ao log
    │       ├── scroll.py               # Teste de scroll e configuração
    │       └── time.py                 # Configuração do tempo de execução


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

Você pode adaptar o comportamento e o estilo da aplicação conforme sua necessidade:

- 🎨 **Estilos Visuais**  
  Modifique cores, fontes e aparência em `ui/styles.py`.

- 🧩 **Componentes da UI**  
  Altere ou crie novos elementos reutilizáveis em `ui/components.py`.

- ⚙️ **Caminhos de Arquivos**  
  Defina ou ajuste diretórios padrão no arquivo `config/paths.py`.

- 📜 **Lógica de Logs**  
  Customize como logs são criados, anotados ou salvos em `core/log_manager.py` e `core/logs.py`.

## Contribuição

1. Faça um fork do repositório
2. Crie sua branch de feature (`git checkout -b feature/Recurso`)
3. Commit suas alterações (`git commit -m 'Adiciona algum Recurso'`)
4. Envie para a branch (`git push origin feature/RecursoIncrivel`)
5. Abra um Pull Request

## Autor

Desenvolvido por [Antônio Lucas](https://github.com/antoniodcastro) 💻  
Entre em contato: antoniolucas323@gmail.com
