from dataclasses import dataclass

@dataclass
class Provincia:
    idProvincia: int
    descripcion: str
    @staticmethod
    def from_dict(data):
        return Provincia(
            idProvincia=data["idProvincia"],
            descripcion=data["descripcion"]
        )