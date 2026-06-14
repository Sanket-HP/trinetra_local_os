[app]

title = Trinetra OS
package.name = trinetra
package.domain = com.sanket

source.dir = .
source.include_exts = py,png,jpg,kv

version = 0.1

requirements = python3,kivy,pyjnius


orientation = portrait

fullscreen = 0

android.api = 33
android.minapi = 24
android.ndk = 28c
android.ndk_api = 24
android.accept_sdk_license = True

android.archs = arm64-v8a,armeabi-v7a

android.allow_backup = True

android.debug_artifact = apk

[buildozer]

log_level = 2
warn_on_root = 0


android.permissions = RECORD_AUDIO,WAKE_LOCK

