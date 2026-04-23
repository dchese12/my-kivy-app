[app]
# (Keep your title and package name as they are)

# CRITICAL: Clean requirements. No version numbers!
requirements = python3,kivy,sqlite3

# CRITICAL: Match this to the GitHub Runner architecture
android.archs = arm64-v8a

# CRITICAL: Auto-accept licenses so the build doesn't hang
android.accept_sdk_license = True

# Ensure this is set to 0 (debug mode)
android.debug = 1

# If you have external files, ensure they are included
source.include_exts = py,png,jpg,kv,atlas,db
