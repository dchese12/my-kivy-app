[app]

title = My Kivy App
package.name = myapp
package.domain = org.test

source.dir = .
source.include_exts = py,kv,db

version = 0.1

requirements = python3,kivy==2.2.1,sqlite3

orientation = portrait

android.permissions = INTERNET

android.api = 33
android.minapi = 21

android.bootstrap = sdl2

log_level = 2
warn_on_root = 0
