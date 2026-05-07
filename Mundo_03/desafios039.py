import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
    print('Site acessado com sucesso!')
except urllib.error.URLError:
    print(f'Erro ao acessar o site.')
else:
    print('Site disponível!')
