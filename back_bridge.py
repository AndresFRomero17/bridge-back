import xmlrpc.client
url = 'https://andresromero1.odoo.com'
db = 'andresromero1'
username = 'fishoaxyz@gmail.com'
password = '68aa0e1793938ba8b3b400d8eca9eeae4d05e904'

#Inicio de sesión
common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
print(common.version())