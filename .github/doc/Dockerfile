# Usa imagem leve com Python 3.10 já instalado
FROM python:3.10-slim

# Instala dependências de sistema (libGL, libx11, etc)
RUN apt-get update && apt-get install -y \
    libgl1 libnss3 libxss1 libasound2 \
    libx11-xcb1 libxcomposite1 libxcursor1 \
    libxi6 libxtst6 libxrandr2 curl git \
    binutils && \
    python3-tk python3-dev\
    rm -rf /var/lib/apt/lists/*

# Cria diretório de trabalho
WORKDIR /app

# Copia os arquivos da sua aplicação
COPY . .

# Instala dependências Python
RUN pip install --upgrade pip && \
    pip install flet pyautogui PyInstaller screeninfo

# Comando default (pode ser alterado para flet pack se quiser build automático)
CMD [ "bash" ]
