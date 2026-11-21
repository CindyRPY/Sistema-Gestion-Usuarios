from dataclasses import dataclass

@dataclass
class Distrito:
    idDistrito: int
    descripcion: str
    @staticmethod
    def from_dict(data):
        return Distrito(
            idDistrito=data["idDistrito"],
            descripcion=data["descripcion"]
        )