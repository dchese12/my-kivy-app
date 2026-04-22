[app]

# App info
title = My Kivy App
package.name = myapp
package.domain = org.test

# Where your code is
source.dir = .
source.include_exts = py,kv

# Requirements
requirements = python3,kivy,sqlite3

# Version
version = 0.1

# Orientation
orientation = portrait

# Permissions (important)
android.permissions = INTERNET

# Fullscreen
fullscreen = 0


[buildozer]
log_level = 2
