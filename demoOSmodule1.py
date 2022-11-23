import os

os.chdir("e:\\newpy")
try:
    filename = 'pythonfile.txt'
    f = open(filename, 'r')
    text = f.read()
    print(text)
    f.close()
    
except IOError:
    print('Problem reading:' + filename)
