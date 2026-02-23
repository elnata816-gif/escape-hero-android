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

# (str) Application versioning
version = 0.1

# (list) Application requirements
# APENAS python3 e kivy. Sem versões travadas.
requirements = python3,kivy

# (list) Supported orientations
orientation = portrait

# (list) Permissions
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE

# (int) Target Android API
android.api = 31

# (int) Minimum API your APK / AAB will support
android.minapi = 21

# (int) Android NDK API to use
android.ndk_api = 21

# (bool) Use --private data storage
android.private_storage = True

# (bool) If True, then automatically accept SDK license agreements
android.accept_sdk_license = True

# (list) The Android archs to build for
android.archs = arm64-v8a, armeabi-v7a

# (bool) Indicate if the application should be fullscreen
fullscreen = 1

# (str) Bootstrap to use for android builds
p4a.bootstrap = sdl2

# (str) python-for-android branch to use
p4a.branch = master

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
