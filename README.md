Implementación de un CRUD con python flask mongodb (con replicación) y restful api

MARCO TEORICO

MongoDB

MongoDB es un sistema de base de datos NoSQL, lo que significa que no utiliza el modelo relacional de las bases de datos tradicionales basadas en SQL. En lugar de eso, MongoDB utiliza un modelo de datos flexible basado en documentos JSON (JavaScript Object Notation), lo que lo hace especialmente adecuado para aplicaciones web y móviles modernas.
En MongoDB, los datos se almacenan en documentos que están organizados en colecciones. Cada documento es una estructura de datos compuesta por pares de clave-valor, similar a los objetos en la programación orientada a objetos. Esto permite almacenar datos de manera flexible y escalable, ya que no se requiere un esquema fijo.
Algunas de las características clave de MongoDB incluyen su capacidad para escalar horizontalmente a través de múltiples servidores, su capacidad de indexación para consultas rápidas y su soporte para consultas complejas utilizando su propio lenguaje de consulta, así como también para operaciones de agregación y geoespaciales.
Se implementará MongoDB en el proyecto por que proporciona beneficios significativos, como flexibilidad de esquema, escalabilidad horizontal, velocidad de desarrollo, consultas flexibles y alto rendimiento.

Referencia: https://www.mongodb.com/es/company/what-is-mongodb

Flask

Flask es un framework web ligero y flexible para Python que proporciona las herramientas necesarias para construir aplicaciones web rápidas y eficientes. Su simplicidad y facilidad de aprendizaje lo hacen ideal para proyectos como un CRUD en Python. En un proyecto CRUD, donde la manipulación de datos es fundamental, Flask ofrece la flexibilidad necesaria para integrar diferentes componentes y bibliotecas según las necesidades específicas del proyecto. Además, su capacidad de extensión permite agregar funcionalidades adicionales fácilmente, lo que lo convierte en una opción versátil para adaptarse a los requisitos cambiantes del proyecto. Con una documentación detallada y fácil de seguir, Flask facilita la construcción de la aplicación CRUD, lo que te permite desarrollar rápidamente una aplicación web eficiente y fácil de mantener.
Referencia: https://flask.palletsprojects.com/en/3.0.x/

Postman

Postman es una plataforma de colaboración para el desarrollo de APIs que ofrece herramientas para probar, documentar y compartir APIs de forma eficiente. En un proyecto CRUD en Python, Postman se utilizaría para probar y validar las diferentes operaciones CRUD (Crear, Leer, Actualizar y Eliminar) de la API desarrollada. 
Gracias a su interfaz intuitiva y fácil de usar, Postman permite enviar solicitudes HTTP a la API y verificar las respuestas recibidas, lo que facilita la depuración y el aseguramiento de la calidad del código. Además, Postman ofrece características como la automatización de pruebas y la generación de documentación, lo que ayuda a mejorar la eficiencia y la colaboración en el desarrollo de la API.

Referencia: https://www.postman.com/

Python

Python es un lenguaje de programación de alto nivel, conocido por su simplicidad y legibilidad de código. Es ampliamente utilizado en diversos campos como desarrollo web, análisis de datos, inteligencia artificial y automatización de tareas.

En Python, el paradigma de programación es muy flexible, permitiendo a los desarrolladores adoptar diferentes estilos como programación imperativa, orientada a objetos y funcional. Esto hace que Python sea una herramienta poderosa para abordar una variedad de problemas y adaptarse a diferentes necesidades de desarrollo.

Una de las características distintivas de Python es su amplia biblioteca estándar, que ofrece módulos y funciones predefinidas para realizar diversas tareas, desde operaciones básicas de entrada y salida hasta complejas operaciones de procesamiento de datos y manipulación de archivos.

Además, Python cuenta con una activa comunidad de desarrolladores que contribuyen constantemente con nuevas bibliotecas y herramientas, lo que facilita aún más el desarrollo de aplicaciones y proyectos.

Se implementará Python en el proyecto debido a sus numerosos beneficios, como su simplicidad y facilidad de aprendizaje, su amplia comunidad de soporte, su versatilidad para diversos tipos de aplicaciones y su capacidad para integrarse con otras tecnologías y sistemas. Los desarrolladores utilizan Python porque es eficiente y fácil de aprender, además de que se puede ejecutar en muchas plataformas diferentes. El software Python se puede descargar gratis, se integra bien a todos los tipos de sistemas y aumenta la velocidad del desarrollo. Python proporciona una base sólida para el desarrollo eficiente y escalable de software, lo que lo convierte en una elección ideal para proyectos modernos de desarrollo de software.

referencia: https://aws.amazon.com/es/what-is/python/

Restful

RESTful es un estilo arquitectónico para el diseño de servicios web que se basa en los principios de REST (Representational State Transfer). En lugar de utilizar un enfoque basado en sesiones y estado, RESTful se centra en recursos y operaciones sobre estos recursos, lo que lo hace ideal para crear interfaces de API web simples, eficientes y escalables.

En una arquitectura RESTful, los recursos son identificados por URLs únicas y se manipulan utilizando métodos HTTP estándar, como GET, POST, PUT y DELETE. Esto proporciona una interfaz uniforme y predecible para interactuar con el sistema, lo que facilita su comprensión y uso. En términos sencillos, RESTful se basa en la idea de que los recursos (como datos o funciones) son accesibles a través de URLs bien definidas. Cada recurso tiene una representación, que puede ser un documento XML, JSON, HTML u otros formatos. Las operaciones comunes sobre estos recursos se realizan utilizando los métodos HTTP estándar, como GET, POST, PUT y DELETE..

Además, RESTful promueve la separación clara entre el cliente y el servidor, lo que permite una mayor modularidad y escalabilidad en el diseño de sistemas distribuidos. Los servicios RESTful son altamente interoperables y pueden ser consumidos por una amplia variedad de clientes, incluyendo aplicaciones web, móviles y de escritorio.

Algunas de las características clave de las APIs RESTful incluyen su capacidad para soportar formatos de datos como JSON y XML, su énfasis en la caché para mejorar la eficiencia y su capacidad para evolucionar de manera incremental sin romper la compatibilidad con versiones anteriores.

Se implementará una arquitectura RESTful en el proyecto porque proporciona beneficios significativos, como una interfaz de API clara y coherente, interoperabilidad entre plataformas, facilidad de escalabilidad y mantenimiento, y soporte para el desarrollo ágil de aplicaciones web y móviles. RESTful es una opción sólida para crear servicios web modernos y flexibles que pueden adaptarse a las necesidades cambiantes del negocio y del mercado

referencia: https://www.soybeto.dev/introduccion-a-restful-simplificando-la-comunicacion-entre-aplicaciones/
