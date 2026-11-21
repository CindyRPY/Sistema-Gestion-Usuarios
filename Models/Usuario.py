from Models.Conexion import client


class Usuario:

    coleccion = client["CookieVialCR"]["Usuarios"]

    @staticmethod
    def login(usuario, password):

        return Usuario.coleccion.find_one({
            "usuario": usuario,
            "password": password,
            "estado": "Activo"
        })