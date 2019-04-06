"""
Módulos Externos

Utilizamos o gerenciador de pacotes Python chamado Pip (Python Installer Package)

Você pode conhecer todos os pacotes externos oficiais em: http://pypi.org

colorama -> é utilizado para permitir impressão de textos coloridos no terminal

Instalando um módulo

pip install colorama

# Utilizando o pacotes instalado

from colorama import init, Fore, Back
init()
print(Fore.MAGENTA + 'Geek University')
"""

import pydf

pdf = pydf.generate_pdf('<h1>Geek University</h1><br/><br/><strong>Programa&ccedil;&atilde;o em Python: Essencial</strong>')
with open('test_doc.pdf', 'wb') as f:
    f.write(pdf)
