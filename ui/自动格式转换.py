import os

files = [file for file in os.listdir() if os.path.splitext(file)[1] == '.ui']
for file in files:
    os.system('pyside6-uic {} > {}'.format(file,os.path.splitext(file)[0] + '.py'))