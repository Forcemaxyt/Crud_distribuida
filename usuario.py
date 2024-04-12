class Usuario:
    def __init__(self, Nombre, Id, Correo):
        self.Id = Id
        self.Nombre = Nombre
        self.Correo = Correo

    def Formato_mongo(self):
        return{
            'Id': self.Id,
            'Nombre': self.Nombre,
            'Correo': self.Correo
        }