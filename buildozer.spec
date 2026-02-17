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
# Incluimos 'txt' para garantir que o arquivo de progresso seja salvo
source.include_exts = py,png,jpg,kv,atlas,txt

# (list) Source files to exclude (let empty to not exclude anything)
#source.exclude_exts = spec

# (list) List of directory to exclude (let empty to not exclude anything)
#source.exclude_dirs = tests, bin, venv

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
# FIX: Usamos pygame-ce que é compatível com Python 3.11+
requirements = python3,pygame-ce

# (str) Custom source folders for requirements
# Sets custom source for any requirements with recipes
# requirements.source.kivy = ../../kivy

# (list) Supported orientations
# Valid options are: landscape, portrait, portrait-reverse or landscape-reverse
orientation = portrait

# (list) Permissions
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE

# (int) Target Android API, should be as high as possible.
# FIX: Alterado para 31 (Android 12) para maior estabilidade de compilação
android.api = 31

# (int) Minimum API your APK / AAB will support.
android.minapi = 21

# (list) Android additional libraries to copy into libs/armeabi
#android.add_libs_armeabi = libs/android/*.so

# (list) Android application meta-data to set (key=value format)
#android.meta_data =

# (list) The Android archs to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
# In past, was `android.arch` as we weren't supporting builds for multiple archs.
# FIX: Descomentado para garantir compatibilidade com celulares novos e antigos
android.archs = arm64-v8a, armeabi-v7a

# (bool) enables Android auto backup feature (Android API >=23)
android.allow_backup = True

# (str) XML file for custom backup rules (see official auto backup documentation)
# android.backup_rules =

# (str) If you need to insert variables into your AndroidManifest.xml file,
# you can do so with the manifestPlaceholders property.
# This property takes a map of key-value pairs. (via a string)
# Usage example : android.manifest_placeholders = [myCustomUrl:"org.kivy.customurl"]
# android.manifest_placeholders = [:]

# (str) Android entry point, default is ok for Kivy-based app
#android.entrypoint = org.kivy.android.PythonActivity

# (list) Gradle dependencies to add
#android.gradle_dependencies =

# (list) Packaging options to add 
# see https://google.github.io/android-gradle-dsl/current/com.android.build.gradle.internal.dsl.PackagingOptions.html
# can be necessary to solve conflicts in gradle_dependencies
# please enclose in double quotes 
# e.g. android.add_packaging_options = "exclude 'META-INF/common.kotlin_module'"
#android.add_packaging_options =

# (bool) If True, then skip trying to update the Android sdk
# This can be useful to avoid excess Internet downloads or save time
# when an update is due and you just want to test/build your package
# android.skip_update = False

# (bool) If True, then automatically accept SDK license
# agreements. This is intended for automation only. If set to False,
# the default, you will be shown the license when first running
# buildozer.
android.accept_sdk_license = True

# (str) Full name including package path of the Java class that implements Android Activity
# use that parameter together with android.entrypoint to set custom Java class instead of PythonActivity
#android.activity_class_name = org.kivy.android.PythonActivity

# (list) Pattern to whitelist for the whole project
#android.whitelist =

# (str) Path to a custom whitelist file
#android.whitelist_src =

# (list) List of Java .jar files to add to the libs so that pyjnius can access
their classes. Don't add jars that you do not need, since extra jars can slow
down the build process. Allows wildcards matching, for example:
# OUYA-ODK/libs/*.jar
#android.add_jars = foo.jar,bar.jar,path/to/more/*.jar

# (list) Java classes to add as activities to the manifest.
#android.add_activities = com.example.ExampleActivity

# (bool) Copy library instead of making a libpymodules.so
#android.copy_libs = 1

# (bool) Skip byte compile for .py files
# android.no-byte-compile-python = False

# (str) the format used to package the app for release mode (aab or apk or aar).
# android.release_artifact = aab

# (str) the format used to package the app for debug mode (apk or aar).
# android.debug_artifact = apk

#
# Python for android (p4a) specific
#

# (str) extra command line arguments to pass when invoking pythonforandroid.toolchain
# FIX: Excluir módulos problemáticos que não compilam para Android
# _lzma: Não está disponível no NDK
# _uuid: Requer libuuid que não é fornecida pelo NDK
# grp: Não é um módulo padrão do Android
# readline, spwd: Não disponíveis em Android
p4a.extra_args = --ignore-setup-py --disable-module grp --disable-module _lzma --disable-module _uuid --disable-module readline --disable-module spwd

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

# (str) Path to build output (i.e. .apk, .aab, .ipa) storage
# bin_dir = ./bin