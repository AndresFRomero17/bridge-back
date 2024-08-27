import xmlrpc.client
#Se usa el URL base de la cuenta odoo
url = 'https://andresromero1.odoo.com'
#El nombre se encuentra en las database
db = 'andresromero1'
#El nombre aparece en el cambio de contraseña
username = 'fishoaxyz@gmail.com'
#APIkey que se genera
password = '68aa0e1793938ba8b3b400d8eca9eeae4d05e904'

#Inicio de sesión
common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
print(common.version(), "\n \n")
uid = common.authenticate(db, username, password, {})

#Llamando los methods
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
print(models.execute_kw(db, uid, password, 'res.partner', 'check_access_rights', ['read'], {'raise_exception': False}), "\n \n")

#Enlistar Registros
customer_companies = models.execute_kw(db, uid, password, 'res.partner', 'search', [[['is_company', '=', True]]])
print ("Empresas cliente: ", customer_companies, "\n \n")
#Paginación
#De forma predeterminada, una búsqueda devolverá los identificadores de todos los registros que coincidan con la condición, 
#que pueden ser una cantidad enorme, offsety limitlos parámetros están disponibles para recuperar solo un subconjunto de todos los 
#registros coincidentes.
pagination = models.execute_kw(db, uid, password, 'res.partner', 'search', [[['is_company', '=', True]]], {'offset': 10, 'limit': 5})
print("Paginación: ", pagination, "\n \n")

#Contar registros
#En lugar de recuperar una lista de registros posiblemente gigantesca y contarlos, search_count()se puede utilizar para recuperar
#solo la cantidad de registros que coinciden con la consulta. Utiliza el mismo filtro de dominiosearch() y ningún otro parámetro.
register_count=models.execute_kw(db, uid, password, 'res.partner', 'search_count', [[['is_company', '=', True]]])
print("Cuento de registros: ",register_count, "\n \n")

#Leer registros
#Se puede acceder a los datos de registro a través del read()método, que toma una lista de identificadores 
#(tal como los devuelve search()) y, opcionalmente, una lista de campos para recuperar. De manera predeterminada, 
#recupera todos los campos que el usuario actual puede leer, lo que suele ser una gran cantidad.
ids = models.execute_kw(db, uid, password, 'res.partner', 'search', [[['is_company', '=', True]]], {'limit': 1})
[record] = models.execute_kw(db, uid, password, 'res.partner', 'read', [ids])
count_record = len(record)
print("Numero de campos obtenidos: ", count_record, "\n \n")

#Listar campos de refistro
#fields_get()se puede utilizar para inspeccionar los campos de un modelo y comprobar cuáles parecen ser de interés.
#Debido a que devuelve una gran cantidad de metainformación (también lo utilizan los programas cliente), debe filtrarse
#antes de imprimirse. Los elementos más interesantes para un usuario humano son string(la etiqueta del campo), 
#help(un texto de ayuda si está disponible) y type(saber qué valores esperar o enviar al actualizar un registro).
record_fields=models.execute_kw(db, uid, password, 'res.partner', 'fields_get', [], {'attributes': ['string', 'help', 'type']})
print("Campos de registro: ", record_fields, "\n \n")

#Buscar y leer
#Debido a que es una tarea muy común, Odoo proporciona un search_read()acceso directo que, como su nombre lo indica, 
#es equivalente a un search()seguido de un read(), pero evita tener que realizar dos solicitudes y mantener los identificadores.
#Sus argumentos son similares a los de search()'s, pero también puede tomar una lista de fields(como read(), si no se proporciona 
#esa lista, buscará todos los campos de los registros coincidentes).
example_search_read=models.execute_kw(db, uid, password, 'res.partner', 'search_read', [[['is_company', '=', True]]], {'fields': ['name', 'country_id', 'comment'], 'limit': 5})
print("Ejemplo de busqueda: ", example_search_read, "\n \n")

#***Crear Registros***
#Los registros de un modelo se crean mediante create(). El método crea un único registro y devuelve su identificador de base de datos.
#create()Toma una asignación de campos a valores, que se utiliza para inicializar el registro. Para cualquier campo que tenga un valor 
#predeterminado y no se configure mediante el argumento de asignación, se utilizará el valor predeterminado.
id = models.execute_kw(db, uid, password, 'res.partner', 'create', [{'name': "New Partner"}])
print("ID: ",id,"\n""\n")

#***Actualizar registros***
#Los registros se pueden actualizar mediante write(). Se necesita una lista de registros para actualizar y una asignación de
#  los campos actualizados a valores similares a create(). Se pueden actualizar varios registros simultáneamente, pero todos
#  obtendrán los mismos valores para los campos que se configuran. No es posible realizar actualizaciones "calculadas" 
# (donde el valor que se configura depende de un valor existente de un registro).