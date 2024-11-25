[app]

# App name
title = Text to Speech

# Package name
package.name = texttospeech

# Package domain (needed for android/ios packaging)
package.domain = org.texttospeech

# Source code where the main.py live
source.dir = .

# Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,mp3

# Application version
version = 0.1

# Application requirements
requirements = python3,kivy,edge_tts,asyncio,aiohttp,certifi

# Android specific
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.api = 31
android.minapi = 21
android.ndk = 25b
android.sdk = 33
android.accept_sdk_license = True

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (string) Presplash background color (for android toolchain)
android.presplash_color = #FFFFFF

# (string) Icon background color (for android toolchain)
android.icon_background_color = #FFFFFF

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
