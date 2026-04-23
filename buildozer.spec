[app]
# (Section 1: The Basics)
title = My Caribbean App
package.name = rajean.myapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,db
version = 0.1

# (Section 2: Requirements)
# CRITICAL: Clean names, no specific versions to avoid crashes
requirements = python3,kivy,sqlite3,requests

# (Section 3: Android Settings)
orientation = portrait
osx.python_version = 3
osx.kivy_version = 1.9.1
fullscreen = 0
android.archs = arm64-v8a
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
