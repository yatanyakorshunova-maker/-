name: Build Kivy APK

on:
  push:
    branches: [ main ]
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest
    
    steps:
      - name: Проверка кода
        uses: actions/checkout@v4

      - name: Установка Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Установка зависимостей (исправлено для Ubuntu 24.04)
        run: |
          sudo apt-get update
          sudo apt-get install -y \
            git zip unzip \
            openjdk-17-jdk \
            python3-pip \
            autoconf libtool pkg-config \
            zlib1g-dev libncurses5-dev libncursesw5-dev \
            cmake libffi-dev libssl-dev \
            liblzma-dev libbz2-dev \
            libtinfo6

          # СОЗДАЁМ СИМВОЛИЧЕСКУЮ ССЫЛКУ: libtinfo5 → libtinfo6
          sudo ln -s /usr/lib/x86_64-linux-gnu/libtinfo.so.6 /usr/lib/x86_64-linux-gnu/libtinfo.so.5

      - name: Установка Buildozer
        run: |
          pip install --upgrade pip
          pip install buildozer

      - name: Сборка APK
        run: buildozer -v android debug

      - name: Загрузка APK
        uses: actions/upload-artifact@v4
        with:
          name: kivy-apk
          path: bin/*.apk
