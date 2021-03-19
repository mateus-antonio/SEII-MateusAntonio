import os
from datetime import datetime

# print(dir(os)) lista oq tem no modulo
# os.chdir() muda diretorio
# os.mkdir() cria diretorio
# os.makedev() cria diretorio e o caminho p ele
# os.rmdir() remove diretorio
# os.removedirs() remove diretorio e o caminho p ele
# os.rename() renomeia arquivo


print(os.getcwd())
print(os.listdir())
print(os.stat('prog09.py').st_size)
mod_time = os.stat('prog09.py').st_mtime
print(datetime.fromtimestamp(mod_time))