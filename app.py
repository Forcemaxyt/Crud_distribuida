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



#Verbo Post
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
@app.route('/delete/<string:usuario_identifi>', methods=['DELETE'])
def delete(usuario_identifi):
    usuarios = db['usuarios']
    result = usuarios.delete_one({'Id' : usuario_identifi})
    if result.deleted_count == 1:
        return '', 200  # Devuelve una respuesta vacía con un código de estado 200
    else:
        return '', 404  # Si no se encuentra el usuario, devuelve un código de estado 404

#Verbo Put o post
@app.route('/edit/<string:usuario_identifi>', methods=['POST'])
def edit(usuario_identifi):
    usuarios = db['usuarios']
    Id = request.form['Id']
    Nombre = request.form['Nombre']
    Correo = request.form['Correo']

    if Id and Nombre and Correo:
        usuarios.update_one({'Id' : usuario_identifi}, {'$set' : {'Id' : Id,'Nombre' : Nombre, 'Correo' : Correo}})
        response = jsonify({'message' : 'Usuario ' + usuario_identifi + ' actualizado correctamente'})
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

#Inicio de la aplicacion Flask
if __name__ == '__main__':
    app.run(debug=True, port=777)
