from bson import ObjectId
from bson.errors import InvalidId

from Models.Conexion import client


class Recurso:

    coleccion = client["CookieVialCR"]["Recursos"]

    def __init__(self, nombre, _id=None):

        self._id = _id
        self.nombre = nombre

    def to_dict(self):

        return {
            "nombre": self.nombre
        }

    def insertar(self):

        resultado = Recurso.coleccion.insert_one(
            self.to_dict()
        )

        self._id = str(resultado.inserted_id)

        return self

    def update(self):

        Recurso.coleccion.update_one(
            {"_id": ObjectId(self._id)},
            {"$set": self.to_dict()}
        )

    def delete(self):

        Recurso.coleccion.delete_one(
            {"_id": ObjectId(self._id)}
        )

    @staticmethod
    def get_all():

        return list(
            Recurso.coleccion.find()
        )

    @staticmethod
    def get_by_id(id_recurso):

        try:

            return Recurso.coleccion.find_one(
                {"_id": ObjectId(id_recurso)}
            )

        except InvalidId:

            return None