from collections import defaultdict

import matplotlib
matplotlib.use("QtAgg")

from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure

from PySide6.QtWidgets import QWidget, QMessageBox

from View.Graficos_ui import Ui_Graficos
from Models.Incidente import Incidente

import matplotlib.pyplot as plt

class GraficosController(QWidget):
    
    plt.style.use('dark_background')


    OPCIONES = [

        "Costos atención vs recuperación",

        "Evolución incidentes por zona",

        "Mortalidad vial por provincia",

        "Indicadores comparativos",

        "Consumo recursos",

        "Impacto económico"
    ]

    def __init__(self, parent=None):

        super().__init__(parent)

        self.ui = Ui_Graficos()

        self.ui.setupUi(self)

        self.ui.combo_grafico.addItems(
            self.OPCIONES
        )

        self.figure = Figure()

        self.canvas = FigureCanvasQTAgg(
            self.figure
        )

        self.ui.layout_canvas.addWidget(
            self.canvas
        )

        self.ui.btn_refresh.clicked.connect(
            self.cargar_datos
        )

        self.ui.combo_grafico.currentIndexChanged.connect(
            self.dibujar
        )

        self.cargar_datos()

    def cargar_datos(self):

        try:

            self.datos = Incidente.get_all()

            self.dibujar()

        except Exception as e:

            QMessageBox.critical(
                self,
                "Error",
                str(e)
            )

    def dibujar(self):

        opcion = (
            self.ui.combo_grafico.currentIndex()
        )

        if opcion == 0:

            self.grafico_costos()

        elif opcion == 1:

            self.grafico_evolucion()

        elif opcion == 2:

            self.grafico_mortalidad()

        elif opcion == 3:

            self.grafico_comparativo()

        elif opcion == 4:

            self.grafico_recursos()

        elif opcion == 5:

            self.grafico_impacto()

    def grafico_costos(self):

        self.figure.clear()

        ax = self.figure.add_subplot(111)

        zonas = defaultdict(float)

        recuperacion = defaultdict(float)

        for d in self.datos:

            zona = d.get(
                "provincia",
                "Sin zona"
            )

            zonas[zona] += float(
                d.get("costo", 0)
            )

            recuperacion[zona] += float(
                d.get(
                    "Costos de atención por zona",
                    0
                )
            )

        labels = list(zonas.keys())

        costos = list(zonas.values())

        rec = list(recuperacion.values())

        x = range(len(labels))

        ax.bar(
            x,
            costos,
            label="Costo",
            color="#55B590"
        )

        ax.bar(
            x,
            rec,
            label="Recuperación",
            color="#6DCCA7"
        )

        ax.set_xticks(x)

        ax.set_xticklabels(
            labels
        )

        ax.legend()

        self.canvas.draw()

    def grafico_mortalidad(self):

        self.figure.clear()

        ax = self.figure.add_subplot(111)

        datos = {}

        for d in self.datos:

            provincia = d.get(
                "provincia",
                "Sin provincia"
            )

            fallecidos = int(
                d.get(
                    "fallecidos",
                    0
                )
            )

            datos[provincia] = (
                datos.get(
                    provincia,
                    0
                )
                + fallecidos
            )

        ax.bar(
            datos.keys(),
            datos.values(),
            color="#55B590"
        )

        ax.set_title(
            "Mortalidad vial por provincia"
        )

        ax.set_ylabel(
            "Fallecidos"
        )

        self.canvas.draw()

    def grafico_recursos(self):

        self.figure.clear()

        ax = self.figure.add_subplot(111)

        datos = {}

        for d in self.datos:

            provincia = d.get(
                "provincia",
                "Sin provincia"
            )

            datos[provincia] = (
                datos.get(
                    provincia,
                    0
                )
                + 1
            )

        ax.bar(
            datos.keys(),
            datos.values(),
            color="#55B590"
        )

        ax.set_title(
            "Consumo recursos por zona"
        )

        ax.set_ylabel(
            "Cantidad"
        )

        self.canvas.draw()

    def grafico_evolucion(self):

        self.figure.clear()

        ax = self.figure.add_subplot(111)

        datos = {}

        for d in self.datos:

            fecha = d.get(
                "fecha",
                ""
            )

            datos[fecha] = (
                datos.get(
                    fecha,
                    0
                )
                + 1
            )

        fechas = sorted(
            datos.keys()
        )

        valores = [
            datos[f]
            for f in fechas
        ]

        ax.plot(
            fechas,
            valores,
            marker="*",
            markersize=12,
            color="#55B590"
        )

        ax.set_title(
            "Evolución de incidentes"
        )

        ax.tick_params(
            axis="x"
        )

        self.canvas.draw()

    def grafico_comparativo(self):

        self.figure.clear()

        ax = self.figure.add_subplot(111)

        heridos = {}
        fallecidos = {}

        for d in self.datos:

            provincia = d.get(
                "provincia",
                ""
            )

            heridos[provincia] = (
                heridos.get(
                    provincia,
                    0
                )
                + int(
                    d.get(
                        "heridos",
                        0
                    )
                )
            )

            fallecidos[provincia] = (
                fallecidos.get(
                    provincia,
                    0
                )
                + int(
                    d.get(
                        "fallecidos",
                        0
                    )
                )
            )

        provincias = list(
            heridos.keys()
        )

        x = range(
            len(provincias)
        )

        ax.bar(
            x,
            list(
                heridos.values()
            ),
            label="Heridos",
            color="#55B590"
        )

        ax.bar(
            x,
            list(
                fallecidos.values()
            ),
            label="Fallecidos",
            color="#1c472a"
        )

        ax.legend()

        ax.set_xticks(x)

        ax.set_xticklabels(
            provincias
        )

        self.canvas.draw()

    def grafico_impacto(self):

        self.figure.clear()

        ax = self.figure.add_subplot(111)

        datos = {}

        for d in self.datos:

            provincia = d.get(
                "provincia",
                "Sin provincia"
            )

            costo = float(
                d.get(
                    "costo",
                    0
                )
            )

            datos[provincia] = (
                datos.get(
                    provincia,
                    0
                )
                + costo
            )

        ax.bar(
            datos.keys(),
            datos.values(),
            color="#55B590"
        )

        ax.set_title(
            "Impacto económico por zona"
        )

        ax.set_ylabel(
            "Costo acumulado"
        )

        self.canvas.draw()