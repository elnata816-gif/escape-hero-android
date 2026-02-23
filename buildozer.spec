[app]
title = Escape Hero
package.name = escapehero
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,txt
version = 0.1

# Apenas Python3 e Kivy padrão
requirements = python3,kivy

orientation = portrait
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE
android.api = 31
android.minapi = 21
android.ndk_api = 21
android.private_storage = True
android.accept_sdk_license = True
android.archs = arm64-v8a, armeabi-v7a
fullscreen = 1
android.add_packaging_options = "exclude 'META-INF/common.kotlin_module'", "exclude 'META-INF/*.kotlin_module'"

# Motor padrão e moderno
p4a.bootstrap = sdl2
p4a.branch = master

[buildozer]
log_level = 2
warn_on_root = 1
