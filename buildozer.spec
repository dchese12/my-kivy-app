[app]
title = My Caribbean App
package.name = rajean.myapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,db
version = 0.1

# REQUIREMENTS (Fixed versions for stability)
requirements = python3,kivy==2.3.0,sqlite3,requests

# ANDROID SETTINGS (The "Nuclear" Sweet Spot)
orientation = portrait
fullscreen = 0
android.archs = arm64-v8a
android.allow_backup = True
android.api = 33
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21
android.accept_sdk_license = True
android.skip_update = False
android.gradle_dependencies = 'com.android.tools.build:gradle:7.4.2'

[buildozer]
log_level = 2
warn_on_root = 1
