name: Build Android APK

on:
  push:
    branches: [ main ]
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout do Código
        uses: actions/checkout@v4

      # 1. Dá permissão total para a pasta, evitando que o Docker bloqueie a criação do APK
      - name: Ajustar Permissões de Pasta
        run: chmod -R 777 ${{ github.workspace }}

      # 2. Roda a compilação direto da Imagem Oficial do Kivy
      - name: Compilar APK (Oficial Kivy Docker)
        run: docker run --rm -v ${{ github.workspace }}:/home/user/hostcwd kivy/buildozer android debug

      # 3. Salva o arquivo gerado
      - name: Upload do APK Final
        uses: actions/upload-artifact@v4
        with:
          name: escape-hero-apk
          path: bin/*.apk
          if-no-files-found: error
