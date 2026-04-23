[app]
title = My Caribbean App
package.name = rajean.myapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,db
version = 0.1

# REQUIREMENTS (Must include sqlite3)
requirements = python3,kivy==2.3.0,sqlite3

# SETTINGS
orientation = portrait
android.archs = arm64-v8a
android.api = 31
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True
android.permissions = WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

[buildozer]
log_level = 2
warn_on_root = 1
