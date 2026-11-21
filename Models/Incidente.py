from bson import ObjectId
from bson.errors import InvalidId

from Models.Conexion import client


class Incidente:

    coleccion = client["CookieVialCR"]["Incidentes"]

    def __init__(
        self,
        numero_reporte,
        fecha,
        tipo_incidente,
        gravedad,
        vehiculos,
        heridos,
        fallecidos,
        etapa,
        recurso,
        tiempo_respuesta,
        costo,
        provincia,
        canton,
        distrito,
        observaciones,
        _id=None
    ):

        self._id = _id

        self.numero_reporte = numero_reporte
        self.fecha = fecha

        self.tipo_incidente = tipo_incidente
        self.gravedad = gravedad

        self.vehiculos = vehiculos
        self.heridos = heridos
        self.fallecidos = fallecidos

        self.etapa = etapa

        self.recurso = recurso

        self.tiempo_respuesta = tiempo_respuesta

        self.costo = costo

        self.provincia = provincia
        self.canton = canton
        self.distrito = distrito

        self.observaciones = observaciones

    def to_dict(self):

        return {
            "numero_reporte": self.numero_reporte,
            "fecha": self.fecha,

            "tipo_incidente": self.tipo_incidente,
            "gravedad": self.gravedad,

            "vehiculos": self.vehiculos,
            "heridos": self.heridos,
            "fallecidos": self.fallecidos,

            "etapa": self.etapa,

            "recurso": self.recurso,

            "tiempo_respuesta": self.tiempo_respuesta,

            "costo": self.costo,

            "provincia": self.provincia,
            "canton": self.canton,
            "distrito": self.distrito,

            "observaciones": self.observaciones
        }

    def insertar(self):

        resultado = Incidente.coleccion.insert_one(
            self.to_dict()
        )

        self._id = str(
            resultado.inserted_id
        )

        return self

    def update(self):

        Incidente.coleccion.update_one(
            {"_id": ObjectId(self._id)},
            {"$set": self.to_dict()}
        )

    def delete(self):

        Incidente.coleccion.delete_one(
            {"_id": ObjectId(self._id)}
        )

    @staticmethod
    def get_all():

        return list(
            Incidente.coleccion.find()
        )

    @staticmethod
    def get_by_id(id_incidente):

        try:

            return Incidente.coleccion.find_one(
                {"_id": ObjectId(id_incidente)}
            )

        except InvalidId:

            return None

    @staticmethod
    def delete_by_id(id_incidente):

        Incidente.coleccion.delete_one({
            "_id": ObjectId(id_incidente)
        })