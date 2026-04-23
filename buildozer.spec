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

# IMPORTANT: STOP auto build-tools conflicts
android.accept_sdk_license = True

# DO NOT FORCE build-tools version anymore
# (this is what was breaking everything)

log_level = 2
warn_on_root = 0
