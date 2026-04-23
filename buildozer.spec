[app]
title = My Caribbean App
package.name = rajean.myapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,db
version = 0.1

# REQUIREMENTS
requirements = python3,kivy==2.3.0,requests

# THE STABILITY FIXES
orientation = portrait
fullscreen = 0
android.archs = arm64-v8a
android.allow_backup = True
android.api = 31
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21
android.accept_sdk_license = True
android.skip_update = False

# Explicitly set Build Tools to avoid GitHub's newer versions
android.build_tools_version = 31.0.0
