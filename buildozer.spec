[app]

# (str) Title of your application
title = Escape Hero

# (str) Package name
package.name = escapehero

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,txt

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
# Usamos pygame-ce (Community Edition)
requirements = python3,pygame-ce

# (list) Supported orientations
orientation = portrait

# (list) Permissions
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE

# (int) Target Android API
android.api = 31

# (int) Minimum API your APK will support
android.minapi = 21

# (int) Android NDK API to use
android.ndk_api = 21

# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = True

# (bool) Accept SDK license agreements automatically
android.accept_sdk_license = True

# (list) The Android archs to build for.
android.archs = arm64-v8a, armeabi-v7a

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (list) Packaging options to avoid gradle conflicts
android.add_packaging_options = "exclude 'META-INF/common.kotlin_module'", "exclude 'META-INF/*.kotlin_module'"

# (str) Bootstrap to use for android builds
p4a.bootstrap = sdl2

# (str) Extra command line arguments
# Ignora setup.py e desabilita módulos inúteis
p4a.extra_args = --ignore-setup-py --disable-module grp --disable-module _lzma --disable-module _uuid --disable-module readline --disable-module spwd --disable-module _gdbm --disable-module nis

# -----------------------------------------------------------------------------
# CORREÇÃO: REMOVIDO "p4a.branch = master"
# Voltamos para a versão estável que é compatível com Ubuntu 22.04
# -----------------------------------------------------------------------------

# iOS specific (defaults)
ios.kivy_ios_url = https://github.com/kivy/kivy-ios
ios.kivy_ios_branch = master
ios.ios_deploy_url = https://github.com/phonegap/ios-deploy
ios.ios_deploy_branch = 1.10.0
ios.codesign.allowed = false

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
