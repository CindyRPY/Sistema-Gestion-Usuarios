from bson import ObjectId
from bson.errors import InvalidId

from Models.Conexion import client


class TipoIncidente:

    coleccion = client["CookieVialCR"]["TipoIncidente"]

    def __init__(self, nombre, _id=None):

        self._id = _id
        self.nombre = nombre

    def to_dict(self):

        return {
            "nombre": self.nombre
        }

    def insertar(self):

        resultado = TipoIncidente.coleccion.insert_one(
            self.to_dict()
        )

        self._id = str(resultado.inserted_id)

        return self

    def update(self):

        TipoIncidente.coleccion.update_one(
            {"_id": ObjectId(self._id)},
            {"$set": self.to_dict()}
        )

    def delete(self):

        TipoIncidente.coleccion.delete_one(
            {"_id": ObjectId(self._id)}
        )

    @staticmethod
    def get_all():

        return list(
            TipoIncidente.coleccion.find()
        )

    @staticmethod
    def get_by_id(id_tipo):

        try:

            return TipoIncidente.coleccion.find_one(
                {"_id": ObjectId(id_tipo)}
            )

        except InvalidId:

            return None