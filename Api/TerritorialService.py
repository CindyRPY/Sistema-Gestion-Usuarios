from Api.client import APIClient

from Api.endpoints import (
    PROVINCIAS,
    CANTONES,
    DISTRITOS
)


class TerritorialService:

    def __init__(self):

        self.api = APIClient()

    def obtener_provincias(self):

        return self.api.get(
            PROVINCIAS
        )

    def obtener_cantones(
        self,
        id_provincia
    ):

        endpoint = CANTONES.format(
            idProvincia=id_provincia
        )

        return self.api.get(
            endpoint
        )

    def obtener_distritos(
        self,
        id_provincia,
        id_canton
    ):

        endpoint = DISTRITOS.format(
            idProvincia=id_provincia,
            idCanton=id_canton
        )

        return self.api.get(
            endpoint
        )