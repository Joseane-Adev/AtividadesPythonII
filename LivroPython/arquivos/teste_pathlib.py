import pathlib
from pathlib import Path
import os.path

caminho = Path('C:/python312')
print(caminho)
print(caminho.exists())
print(caminho.is_dir())
print(caminho.is_file())