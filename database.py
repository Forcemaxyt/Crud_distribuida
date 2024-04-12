from pymongo import MongoClient
import certifi

MONGO_URI = 'mongodb+srv://force:123@crud.1okqllu.mongodb.net/?retryWrites=true&w=majority&appName=CRUD'
ca = certifi.where()

def dbConexion():
    try:
        client = MongoClient(MONGO_URI, tlsCAFile=ca)
        db = client["db_usuarios"] #si no existe base de datos se crea una
    except ConnectionError:
        print('Error de conexión con la base de datos')
    return db