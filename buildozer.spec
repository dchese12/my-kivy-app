[app]
# (Section 1: Basic Info)
title = My Caribbean App
package.name = rajean.myapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,db
version = 0.1

# (Section 2: Requirements)
# Explicitly include sqlite3 so the compiler links the libraries correctly
requirements = python3,kivy==2.3.0,sqlite3

# (Section 3: Android Configuration - THE CRITICAL PART)
orientation = portrait
fullscreen = 0
android.archs = arm64-v8a
android.allow_backup = True

# We are pinning these to version 31 to match the GitHub Runner's stable SDK
android.api = 31
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21
android.build_tools_version = 31.0.0

# Security and Permissions
android.accept_sdk_license = True
android.skip_update = True
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# (Section 4: Build Settings)
# This helps avoid Gradle 9.0 conflicts
android.gradle_dependencies = 'com.android.tools.build:gradle:7.4.2'
android.enable_androidx = True

[buildozer]
log_level = 2
warn_on_root = 1
