from io import open
import os.path

file = 'test.txt'

def review(file):
    return os.path.exists(file)

if review(file):
    with open(file,'r+') as f:
        text = f.read()
        print(text)
        print()
        f.seek(0)
        lines = f.readlines()
        print(lines)
        print()
        f.seek(0)
        f.write('Rubén')
        f.seek(0)
        text = f.read()
        print(text)
        print()
        f.writelines(lines)
        f.seek(0)
        texto = f.read()
        print(texto)
        print()
else:
    with open(file, 'w') as f:
        phrase = 'Hello word\nThis is my first file.\nIt was created with: Python\n'
        f.write(phrase)

