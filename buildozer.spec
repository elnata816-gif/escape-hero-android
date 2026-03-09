[app]

# (str) Título do seu aplicativo
title = Escape Hero

# (str) Nome do pacote (sem espaços ou caracteres especiais)
package.name = escapehero

# (str) Domínio do pacote (usado para identificar o app na loja)
package.domain = org.elna

# (str) Diretório onde está o código fonte (neste caso, na mesma pasta)
source.dir = .

# (list) Extensões de arquivos que devem ser incluídas no APK
source.include_exts = py,png,jpg,kv,atlas,json

# (str) Versão do seu aplicativo
version = 0.1

# (list) Bibliotecas Python necessárias para rodar o app
requirements = python3,kivy

# (str) Orientação da tela do celular (portrait = em pé)
orientation = portrait

# (bool) Se o app deve rodar em tela cheia
fullscreen = 0

# (list) Permissões necessárias
android.permissions = INTERNET

# (int) Nível da API do Android alvo (33 é o padrão atual recomendado pelo Google)
android.api = 33

# (int) Nível mínimo da API suportada
android.minapi = 21

# (str) Arquitetura do processador (Removido o espaço após a vírgula para evitar falha no script de build)
android.archs = arm64-v8a,armeabi-v7a

# --- CONFIGURAÇÃO CRÍTICA PARA O GITHUB ACTIONS ---
# (bool) Aceitar automaticamente as licenças do SDK do Android. 
android.accept_sdk_license = True


[buildozer]
# (int) Nível de log no console (2 = debug, bom para ver erros no GitHub)
log_level = 2
warn_on_root = 1
