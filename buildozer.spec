[app]
title = Escape Hero
package.name = escapehero
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,txt
version = 0.1

# O SEGREDO ESTÁ AQUI: Kivy 2.2.0 é a versão perfeitamente compatível com o Cython 0.29.33
requirements = python3,kivy==2.2.0

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
p4a.bootstrap = sdl2
p4a.extra_args = --ignore-setup-py --disable-module grp --disable-module _lzma --disable-module _uuid --disable-module readline --disable-module spwd --disable-module _gdbm --disable-module nis
ios.kivy_ios_url = https://github.com/kivy/kivy-ios
ios.kivy_ios_branch = master
ios.ios_deploy_url = https://github.com/phonegap/ios-deploy
ios.ios_deploy_branch = 1.10.0
ios.codesign.allowed = false

[buildozer]
log_level = 2
warn_on_root = 1
