from dataclasses import dataclass

@dataclass
class Canton:
    idCanton: int
    descripcion: str

    @staticmethod
    def from_dict(data):
        return Canton(
            idCanton=data["idCanton"],
            descripcion=data["descripcion"]
        )