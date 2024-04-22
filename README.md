<h1>Implementación de un CRUD con python flask mongodb (con replicación) y restful api</h1>

<H>MARCO TEORICO</H>
<h4>Python</h4>

Python es un lenguaje de programación de alto nivel, conocido por su simplicidad y legibilidad de código. Es ampliamente utilizado en diversos campos como desarrollo web, análisis de datos, inteligencia artificial y automatización de tareas.

En Python, el paradigma de programación es muy flexible, permitiendo a los desarrolladores adoptar diferentes estilos como programación imperativa, orientada a objetos y funcional. Esto hace que Python sea una herramienta poderosa para abordar una variedad de problemas y adaptarse a diferentes necesidades de desarrollo.

Una de las características distintivas de Python es su amplia biblioteca estándar, que ofrece módulos y funciones predefinidas para realizar diversas tareas, desde operaciones básicas de entrada y salida hasta complejas operaciones de procesamiento de datos y manipulación de archivos.

Además, Python cuenta con una activa comunidad de desarrolladores que contribuyen constantemente con nuevas bibliotecas y herramientas, lo que facilita aún más el desarrollo de aplicaciones y proyectos.

Se implementará Python en el proyecto debido a sus numerosos beneficios, como su simplicidad y facilidad de aprendizaje, su amplia comunidad de soporte, su versatilidad para diversos tipos de aplicaciones y su capacidad para integrarse con otras tecnologías y sistemas. Los desarrolladores utilizan Python porque es eficiente y fácil de aprender, además de que se puede ejecutar en muchas plataformas diferentes. El software Python se puede descargar gratis, se integra bien a todos los tipos de sistemas y aumenta la velocidad del desarrollo. Python proporciona una base sólida para el desarrollo eficiente y escalable de software, lo que lo convierte en una elección ideal para proyectos modernos de desarrollo de software.

referencia: https://aws.amazon.com/es/what-is/python/

<h4>MongoDB</h4>

MongoDB es un sistema de base de datos NoSQL, lo que significa que no utiliza el modelo relacional de las bases de datos tradicionales basadas en SQL. En lugar de eso, MongoDB utiliza un modelo de datos flexible basado en documentos JSON (JavaScript Object Notation), lo que lo hace especialmente adecuado para aplicaciones web y móviles modernas.
En MongoDB, los datos se almacenan en documentos que están organizados en colecciones. Cada documento es una estructura de datos compuesta por pares de clave-valor, similar a los objetos en la programación orientada a objetos. Esto permite almacenar datos de manera flexible y escalable, ya que no se requiere un esquema fijo.
Algunas de las características clave de MongoDB incluyen su capacidad para escalar horizontalmente a través de múltiples servidores, su capacidad de indexación para consultas rápidas y su soporte para consultas complejas utilizando su propio lenguaje de consulta, así como también para operaciones de agregación y geoespaciales.
Se implementará MongoDB en el proyecto por que proporciona beneficios significativos, como flexibilidad de esquema, escalabilidad horizontal, velocidad de desarrollo, consultas flexibles y alto rendimiento.

Referencia: https://www.mongodb.com/es/company/what-is-mongodb

<h4>Flask</h4>

Flask es un framework web ligero y flexible para Python que proporciona las herramientas necesarias para construir aplicaciones web rápidas y eficientes. Su simplicidad y facilidad de aprendizaje lo hacen ideal para proyectos como un CRUD en Python. En un proyecto CRUD, donde la manipulación de datos es fundamental, Flask ofrece la flexibilidad necesaria para integrar diferentes componentes y bibliotecas según las necesidades específicas del proyecto. Además, su capacidad de extensión permite agregar funcionalidades adicionales fácilmente, lo que lo convierte en una opción versátil para adaptarse a los requisitos cambiantes del proyecto. Con una documentación detallada y fácil de seguir, Flask facilita la construcción de la aplicación CRUD, lo que te permite desarrollar rápidamente una aplicación web eficiente y fácil de mantener.
Referencia: https://flask.palletsprojects.com/en/3.0.x/

<h4>Postman</h4>

Postman es una plataforma de colaboración para el desarrollo de APIs que ofrece herramientas para probar, documentar y compartir APIs de forma eficiente. En un proyecto CRUD en Python, Postman se utilizaría para probar y validar las diferentes operaciones CRUD (Crear, Leer, Actualizar y Eliminar) de la API desarrollada. 
Gracias a su interfaz intuitiva y fácil de usar, Postman permite enviar solicitudes HTTP a la API y verificar las respuestas recibidas, lo que facilita la depuración y el aseguramiento de la calidad del código. Además, Postman ofrece características como la automatización de pruebas y la generación de documentación, lo que ayuda a mejorar la eficiencia y la colaboración en el desarrollo de la API.

Referencia: https://www.postman.com/


<h4>Restful</h4>

RESTful es un estilo arquitectónico para el diseño de servicios web que se basa en los principios de REST (Representational State Transfer). En lugar de utilizar un enfoque basado en sesiones y estado, RESTful se centra en recursos y operaciones sobre estos recursos, lo que lo hace ideal para crear interfaces de API web simples, eficientes y escalables.

En una arquitectura RESTful, los recursos son identificados por URLs únicas y se manipulan utilizando métodos HTTP estándar, como GET, POST, PUT y DELETE. Esto proporciona una interfaz uniforme y predecible para interactuar con el sistema, lo que facilita su comprensión y uso. En términos sencillos, RESTful se basa en la idea de que los recursos (como datos o funciones) son accesibles a través de URLs bien definidas. Cada recurso tiene una representación, que puede ser un documento XML, JSON, HTML u otros formatos. Las operaciones comunes sobre estos recursos se realizan utilizando los métodos HTTP estándar, como GET, POST, PUT y DELETE..

Además, RESTful promueve la separación clara entre el cliente y el servidor, lo que permite una mayor modularidad y escalabilidad en el diseño de sistemas distribuidos. Los servicios RESTful son altamente interoperables y pueden ser consumidos por una amplia variedad de clientes, incluyendo aplicaciones web, móviles y de escritorio.

Algunas de las características clave de las APIs RESTful incluyen su capacidad para soportar formatos de datos como JSON y XML, su énfasis en la caché para mejorar la eficiencia y su capacidad para evolucionar de manera incremental sin romper la compatibilidad con versiones anteriores.

Se implementará una arquitectura RESTful en el proyecto porque proporciona beneficios significativos, como una interfaz de API clara y coherente, interoperabilidad entre plataformas, facilidad de escalabilidad y mantenimiento, y soporte para el desarrollo ágil de aplicaciones web y móviles. RESTful es una opción sólida para crear servicios web modernos y flexibles que pueden adaptarse a las necesidades cambiantes del negocio y del mercado

referencia: https://www.soybeto.dev/introduccion-a-restful-simplificando-la-comunicacion-entre-aplicaciones/

<h4>Api</h4>

Qué es una API?
API significa Interfaz de Programación de Aplicaciones. Es un conjunto de reglas y definiciones que permiten que dos aplicaciones se comuniquen entre sí. Funciona como un intermediario, traduciendo las solicitudes de una aplicación al lenguaje que la otra puede entender.


Existen muchas razones para elegir una API. Algunas de las más importantes son:

Facilidad de uso: Las APIs simplifican el desarrollo de software al proporcionar una forma estándar de interactuar con diferentes aplicaciones. No es necesario conocer los detalles internos de cada aplicación, solo las reglas de la API.

Eficiencia: Las APIs pueden mejorar la eficiencia al automatizar tareas que de otro modo se realizarían manualmente. Esto puede ahorrar tiempo y dinero.

Escalabilidad: Las APIs permiten que las aplicaciones se escalen fácilmente. Si necesitas agregar más usuarios o funcionalidades, la API puede adaptarse sin necesidad de reescribir el código de la aplicación.

Flexibilidad: Las APIs te dan la flexibilidad de conectar diferentes aplicaciones y servicios. Esto te permite crear soluciones más robustas y personalizadas.

<h4>Verbos</h4>

En programación, los verbos son acciones o métodos que realizan operaciones sobre objetos o datos. Estos verbos representan las acciones que se pueden llevar a cabo en un programa. Por ejemplo, en un proyecto de gestión de usuarios, algunos verbos podrían ser "crearUsuario", "eliminarUsuario", "actualizarUsuario" y "obtenerUsuario".

La implementación de verbos en un proyecto de programación es esencial por varias razones:

Organización y estructura: Los verbos permiten organizar el código de manera lógica y estructurada. Al dividir las acciones en verbos específicos, el código se vuelve más comprensible y mantenible.

Reusabilidad: Al encapsular las acciones en verbos, se promueve la reutilización del código. Esto significa que si necesitas realizar una acción similar en diferentes partes del proyecto, puedes simplemente llamar al mismo verbo en lugar de volver a escribir el código desde cero.

Claridad y legibilidad: Al utilizar verbos descriptivos, el código se vuelve más legible y comprensible tanto para ti como para otros desarrolladores que puedan trabajar en el proyecto en el futuro. Esto facilita la colaboración y el mantenimiento del código a largo plazo.

<H1>MARCO METODOLOGICO</H1>

1 Planificación y Diseño 

1.1 Definición de Requisitos
Reunión del equipo para discutir y definir los requisitos del sistema, incluyendo las operaciones CRUD necesarias y los datos a ser manipulados.
[![horario](horario "horario")](https://drive.google.com/file/d/11FMt6hbYnsT528loL0Dn9rdpBDv48JAO/view?usp=sharing "horario")
Requisitos Previos
Asegúrese de que tener el siguiente instalado y configurado en su computadora:
Python 3.4 o superior
PIP 18.0 o superior
si no se encuentra instalado seguir los siguientes pasos

2. Desarrollo

2.1 Configuración del Entorno
2.1.1 Instalación y configuración de Python (contiene el gestor de paquetes pip)
[![](instalar python)](https://drive.google.com/file/d/1D-PvCLZcYivPnhi42KDExjJIFwY22SBm/view?usp=drive_link)

Paso 2 Instalación flask 
Se ha de instalar flask con el siguiente comando
<< pip install flask >>
[![](instalacion flask)](https://drive.google.com/file/d/1m7xXq_ZCx5qxSrJFv2rVcJpPW13FTQ88/view?usp=drive_link)

Paso 3 Crear un cluster en mongoDB Atlas
Para poder utilizar servicios en la nube de MongoDB, necesitarás una cuenta de MongoDB Atlas. Para crear uno, ir a su página de inicio y presione el botón Comenzar Gratis.
link: https://www.mongodb.com/

Luego de crearse la cuenta de mongo se creará el clúster de la siguiente manera:

[![](crear clouster)](https://drive.google.com/file/d/1tcEvA3CGheLehANkgrCoxOQyJ8vPh4vn/view?usp=sharing)

 paso 4 En la sección Nivel de Clúster, seleccione la opción de M0 para crear el clúster de nivel libre. Ofrece 512 MB de espacio de almacenamiento, una versión reciente de MongoDB con WiredTiger como el motor de almacenamiento, un conjunto de réplicas de tres nodos y un generoso 10 GB de ancho de banda por semana.
 
 [![](m 0)](https://drive.google.com/file/d/1L7IklHvErk_6ZbZl5x6bhvtaAgvgowVJ/view?usp=drive_link)

Nota: el nombre del clúster no se podrá cambiar una vez creado

paso 5 El resto lo dejamos por defecto y le damos a créate Deployment

[![](m0 develpment)](https://drive.google.com/file/d/1Vneie6i_VrozCJwi7mKzHzSBxnXOhwIr/view?usp=drive_link)

paso 6 damos a choose a connection method

[![](connect y)](https://drive.google.com/file/d/1rkV9NATqmdlOIzJgb0fL0sSnwAUX6YnL/view?usp=drive_link)

paso 7  damos a drivers

[![](drives u)](https://drive.google.com/file/d/1NYOXWT7jkxmIqkusehUnEM0sjhJvJLMl/view?usp=drive_link)

paso 8 Seleccionamos Python e instalamos el driver como nos dice el propio mongo con 
<< python -m pip install "pymongo[srv]" >> , tambien instalaremos para luego darle a a review setup steps.

[![](mongo o)](https://drive.google.com/file/d/19J6gFHjJPL0bXpJt8xsGiZPIQZnba-iv/view?usp=drive_link)

paso 9 Instalación de pymongo: biblioteca de Python que se utiliza para interactuar con la base de datos MongoDB.
<< pip install pymongo >>

[![](pip p)](https://drive.google.com/file/d/1UQQw-4zKKSQNHwKMSf6sgvwgHNgItLDe/view?usp=drive_link)

paso 10 Instalación de pymongo srv: Cuando se habla de pymongo srv, se está haciendo referencia a la funcionalidad de conexión a una base de datos MongoDB utilizando una cadena de conexión SRV.

[![](pymongo srv)](https://drive.google.com/file/d/1qIGTqTbq6lldIEnA_NObDmTQC_Q2_0vk/view?usp=drive_link)

paso 11 Instalalcion de certifi :  biblioteca de Python que proporciona certificados de confianza para la verificación de la autenticidad de certificados SSL/TLS en aplicaciones Python. Esta biblioteca es utilizada por otras bibliotecas que realizan conexiones seguras a servidores web utilizando el protocolo HTTPS, como requests, urllib3, http.client, entre otras.
<<pip install certifi >>

[![](certifi i)](https://drive.google.com/file/d/1UH1d9snLycKmf8uYjR4P22QwTQr7mr05/view?usp=drive_link)

paso 12 Se copia la uri donde dice connection string , con este accederemos a la base de datos y por ultimo le damos a done.

[![](connect string)](https://drive.google.com/file/d/1N6gHC-6UXE8CyOkOutTU2DLtl0Bc5s2Z/view?usp=drive_link)

paso 13 Crearemos un usuario para la gestión de las bases de datos para ser mas eficientes a la hora de editar la uri, nos vamos a Database Access,luego se selecciona add new database user

[![](usuarios s)](https://drive.google.com/file/d/1dkS2aop5FUnbNWLqVipT6VH4FL6IBoun/view?usp=drive_link)

paso 14 Seleccionamos password como método de identificación creamos un usuario con su respectiva contraseña y le añadimos el rol de atlas admin para luego guardarlo.

[![](do s)](https://drive.google.com/file/d/1lfqbaPd5pc66r-gnXQnATHz-ucyzubXp/view?usp=drive_link)

2.2 Desarrollo de la API RESTful
Asignación de tareas para desarrollar las rutas y controladores de la API RESTful utilizando Flask, definiendo las operaciones CRUD para interactuar con la base de datos MongoDB.

#Se importan los modulos

    from flask import Flask, render_template, request, Response, jsonify, redirect, url_for
    import database as dbase  
    from usuario import Usuario  #Importacion de la clase Usuario

#Conexion a la base de datos

    db = dbase.dbConexion()

#Creación de una instancia Flask

    app = Flask(__name__)

#Rutas de la aplicación

    @app.route('/')
    def Pt_principal():
    usuarios = db['usuarios']
    usuario_recibido = usuarios.find()

# Verificar si la solicitud acepta HTML
    if 'text/html' in request.headers.get('Accept', ''):
        return render_template('index.html', usuarios=usuario_recibido)
    else:
        usuarios_json = []
        for usuario in usuario_recibido:
            usuarios_json.append({
                'Id': usuario['Id'],
                'Nombre': usuario['Nombre'],
                'Correo': usuario['Correo']
            })
        return jsonify(usuarios_json)

# Verbo Post
    @app.route('/usuarios_agg', methods=['POST'])
    def aggusuario():
    usuarios = db['usuarios'] #crea la base de datos si no esta creada
    Id = request.form['Id']
    Nombre = request.form['Nombre']
    Correo = request.form['Correo']

    if Id and Nombre and Correo:
        usuario = Usuario(Nombre, Id, Correo)
        usuarios.insert_one(usuario.Formato_mongo())
        response = jsonify({
            'Id' : Id,
            'Nombre' : Nombre,
            'Correo' : Correo
        })
        return redirect(url_for('Pt_principal'))
    else:
        return notFound()

# Verbo delete
    @app.route('/delete/<string:usuario_identifi>', methods=['POST','DELETE'])
    def delete(usuario_identifi):
    usuarios = db['usuarios']
    result = usuarios.delete_one({'Id' : usuario_identifi})
    if result.deleted_count == 1:
        return redirect(url_for('Pt_principal'))  # Redirige al usuario a la página principal después de eliminar
    else:
        return '', 404  # Si no se encuentra el usuario, devuelve un código de estado 404
    
# Verbo Put o Post
    @app.route('/edit/<string:usuario_identifi>', methods=['POST','PUT'])
    def edit(usuario_identifi):
    usuarios = db['usuarios']
    Id = request.form['Id']
    Nombre = request.form['Nombre']
    Correo = request.form['Correo']

    if Id and Nombre and Correo:
        usuarios.update_one({'Id' : usuario_identifi}, {'$set' : {'Id' : Id,'Nombre' : Nombre, 'Correo' : Correo}})
        return redirect(url_for('Pt_principal'))
    else:
        return notFound()

    @app.errorhandler(404)
    def notFound(error=None):
    message ={
        'message': 'No encontrado ' + request.url,
        'status': '404 Not Found'
    }
    response = jsonify(message)
    response.status_code = 404
    return response

#Inicio de la aplicacion Flask

    if __name__ == '__main__':
    app.run(debug=True, port=777)


2.3 Configuración de Replicación en MongoDB
Configuración de la replicación en MongoDB para garantizar la disponibilidad y la redundancia de los datos, dividiendo las tareas para establecer un clúster replicado.
<h3>probar replicación</h3>
Mongodb Atlas configura automáticamente un sistema de replicación con tres bases de datos: una principal y dos secundarias. Si la base de datos principal falla, una de las secundarias asumirá su función, garantizando la continuidad del servicio.
Para comprobar si la replicación está activa, necesitas conectarte a la base de datos remota utilizando el shell de mongo.
 MongoDB Shell
Se descarga el msi proporcionado por MongoDB

[![](un o)](https://drive.google.com/file/d/11WPyzMnjIZ37uOQZN4-Xr3xRmCRflvoy/view?usp=drive_link)

1. Ve a la página de MongoDB donde está tu clúster de base de datos.
2. Haz clic en "Conectar" y elige el método deseado. En este caso, usaremos el shell de mongo.
3. Ejecuta la línea de comando proporcionada por MongoDB en una consola CMD o PowerShell, reemplazando `<username>` con tu usuario:
   mongosh "mongodb+srv://crud.1okqllu.mongodb.net/" --apiVersion 1 --username <username>   
4. Luego, proporciona la contraseña correspondiente a ese usuario.
 Verificar el Estado de la Replicación
Una vez que estás conectado en la consola de comandos, ejecuta el siguiente comando para revisar el estado de la replicación:
rs.status()


3. Pruebas

3.1 Pruebas de Integración
Realización de pruebas de integración para verificar el funcionamiento conjunto de los diferentes módulos del sistema.
 escribimos en nuestro navegador: localhost:777
 
 [![]](https://drive.google.com/file/d/1zw3hAJi1KtcUKOpy5BunZ6-NKic1IG4e/view?usp=drive_link)
 
4. Implementación
verificamos el correcto funcionamiento del crud
 verificamos el correcto funcionamiento del crear
[![]](https://drive.google.com/file/d/1Dg2sgQI20nL1HR0cYWL38zA8DekETMws/view?usp=sharing)

verificamos el correcto funcionamiento del eliminar
[![]](https://drive.google.com/file/d/1Dg2sgQI20nL1HR0cYWL38zA8DekETMws/view?usp=sharing)

verificamos el correcto funcionamiento del editar
[![]](https://drive.google.com/file/d/1yHcqvOX0PQDHRY8kHxgeJVUA5Ylg6kmK/view?usp=drive_link)

4.1 verificacion con postman 

verificación del agregar
verificamos el editar
[![]](https://drive.google.com/file/d/1aqomJq9yf3DrvUuhPG4r8Hkm4l9Ya3ns/view?usp=sharing)

verificamos el eliminar

[![]](https://drive.google.com/file/d/1j65AHkKRUi-fm2CViBbsC7AoJ-GKbUgX/view?usp=drive_link)
verificamos el ver

[![]](https://drive.google.com/file/d/1Ox9w40Y2JCKBOfH1Z9n6nSUcZVjo2jya/view?usp=sharing)

verificamos el editar
[![]](https://drive.google.com/file/d/1Gm1vPJ1T9zL462g4ddGUagszf6dDuPvt/view?usp=sharing)

Abstracción y modularidad: Los verbos permiten abstraer las operaciones subyacentes, lo que facilita la modularidad del código. Esto significa que puedes cambiar la implementación interna de un verbo sin afectar el resto del código que lo utiliza, siempre y cuando la interfaz del verbo permanezca igual.


¿por que no se puede utilizar potamn para cambiar la base primaria a segundaria? 

Postman en sí mismo no tiene la capacidad de bloquear el acceso a una IP específica en MongoDB Atlas. 

MongoDB Atlas solo permite conexiones de cliente a la implementación de la base de datos desde las entradas en la lista de acceso IP del proyecto. Cada entrada es una dirección IP única o un rango de direcciones notado por CIDR. Para bloquear el acceso a una IP específica, tendrías que eliminar esa entrada de la lista de acceso IP en la configuración de tu proyecto en MongoDB Atlas.

