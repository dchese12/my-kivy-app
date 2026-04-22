[app]

title = My Kivy App
package.name = myapp
package.domain = org.test

source.dir = .
source.include_exts = py,kv,db,png,jpg

version = 0.1

requirements = python3,kivy,sqlite3

orientation = portrait
fullscreen = 0

android.permissions = INTERNET

# Android settings (IMPORTANT FIX)
android.api = 33
android.build_tools_version = 33.0.2
android.ndk = 25b
android.build_tools_version = 33.0.2

# Optional but helps stability
log_level = 2
warn_on_root = 0

# Kivy window behavior
window = kivy
