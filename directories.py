from pathlib import Path

path = Path("emails")
print(path.exists())
print(path.mkdir())
print(path.exists())
print(path.rmdir())

path = Path()
for file in path.glob('*.py'):
    print(file)

# Absolute path
# C:\Program Files\Microsoft
# /usr/local/bin
# Relative path