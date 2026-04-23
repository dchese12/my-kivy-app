[app]

title = My Kivy App
package.name = myapp
package.domain = org.test

source.dir = .
source.include_exts = py,kv,db

version = 0.1

requirements = python3,kivy,sqlite3

orientation = portrait

android.permissions = INTERNET

android.api = 33
android.minapi = 21

android.build_tools_version = 33.0.2
android.ndk = 25b

log_level = 2
warn_on_root = 0
