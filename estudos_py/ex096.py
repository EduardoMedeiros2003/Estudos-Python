import urllib.request

try:
    site = urllib.request.urlopen('https://github.com/EduardoMedeiros2003')
except:
    print('O site NÃO está acessível no momento.')
else:
    print('O site está acessível!')
