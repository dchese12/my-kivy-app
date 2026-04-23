[app]
title = My Caribbean App
package.name = rajean.myapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,db
version = 0.1

# Ensure sqlite3 is here!
requirements = python3,kivy==2.3.0,sqlite3

orientation = portrait
android.archs = arm64-v8a
android.api = 31
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True

# Disable auto-update to stop it from grabbing Gradle 9
android.skip_update = True
