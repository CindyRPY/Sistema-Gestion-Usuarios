from PySide6.QtWidgets import (
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QComboBox,
    QDateEdit,
    QSpinBox,
    QDoubleSpinBox,
    QTableWidget,
    QHeaderView,
    QTextEdit
)

from View.estilos import STYLE_CRUD


class Ui_Incidente:

    def setupUi(self, IncidenteWidget):

        IncidenteWidget.setObjectName(
            "CrudWidget"
        )

        IncidenteWidget.setStyleSheet(
            STYLE_CRUD
        )

        layout = QVBoxLayout()

        self.lbl_titulo = QLabel(
            "Gestión de Incidentes"
        )

        self.lbl_titulo.setObjectName(
            "titulo"
        )

        layout.addWidget(
            self.lbl_titulo
        )

        # ===========================
        # REPORTE Y FECHA
        # ===========================

        fila1 = QHBoxLayout()

        self.inp_reporte = QLineEdit()

        self.inp_reporte.setPlaceholderText(
            "Número de reporte"
        )

        self.inp_fecha = QDateEdit()

        fila1.addWidget(
            self.inp_reporte
        )

        fila1.addWidget(
            self.inp_fecha
        )

        layout.addLayout(
            fila1
        )

        # ===========================
        # TIPO Y GRAVEDAD
        # ===========================

        fila2 = QHBoxLayout()

        self.cmb_tipo = QComboBox()

        self.cmb_gravedad = QComboBox()

        fila2.addWidget(
            self.cmb_tipo
        )

        fila2.addWidget(
            self.cmb_gravedad
        )

        layout.addLayout(
            fila2
        )

        # ===========================
        # VEHÍCULOS / HERIDOS / FALLECIDOS
        # ===========================

        fila3 = QHBoxLayout()

        self.spn_vehiculos = QSpinBox()

        self.spn_vehiculos.setPrefix(
            "Vehículos: "
        )

        self.spn_heridos = QSpinBox()

        self.spn_heridos.setPrefix(
            "Heridos: "
        )

        self.spn_fallecidos = QSpinBox()

        self.spn_fallecidos.setPrefix(
            "Fallecidos: "
        )

        fila3.addWidget(
            self.spn_vehiculos
        )

        fila3.addWidget(
            self.spn_heridos
        )

        fila3.addWidget(
            self.spn_fallecidos
        )

        layout.addLayout(
            fila3
        )

        # ===========================
        # RECURSO Y ETAPA
        # ===========================

        fila4 = QHBoxLayout()

        self.cmb_recurso = QComboBox()

        self.cmb_etapa = QComboBox()

        self.cmb_etapa.addItems([
            "En Atención",
            "Cerrado",
            "En Investigación"
        ])

        fila4.addWidget(
            self.cmb_recurso
        )

        fila4.addWidget(
            self.cmb_etapa
        )

        layout.addLayout(
            fila4
        )

        # ===========================
        # UBICACIÓN
        # ===========================

        fila_ubicacion = QHBoxLayout()

        self.cmb_provincia = QComboBox()

        self.cmb_canton = QComboBox()

        self.cmb_distrito = QComboBox()

        fila_ubicacion.addWidget(
            self.cmb_provincia
        )

        fila_ubicacion.addWidget(
            self.cmb_canton
        )

        fila_ubicacion.addWidget(
            self.cmb_distrito
        )

        layout.addLayout(
            fila_ubicacion
        )

        # ===========================
        # TIEMPO Y COSTO
        # ===========================

        fila5 = QHBoxLayout()

        self.spn_tiempo = QSpinBox()

        self.spn_tiempo.setSuffix(
            " min"
        )

        self.spn_costo = QDoubleSpinBox()

        self.spn_costo.setMaximum(
            999999999
        )

        self.spn_costo.setPrefix(
            "₡ "
        )

        fila5.addWidget(
            self.spn_tiempo
        )

        fila5.addWidget(
            self.spn_costo
        )

        layout.addLayout(
            fila5
        )

        # ===========================
        # OBSERVACIONES
        # ===========================

        self.txt_observaciones = QTextEdit()

        self.txt_observaciones.setPlaceholderText(
            "Observaciones del incidente..."
        )

        layout.addWidget(
            self.txt_observaciones
        )

        # ===========================
        # BOTONES CRUD
        # ===========================

        fila_botones = QHBoxLayout()

        self.btn_guardar = QPushButton(
            "Guardar"
        )

        self.btn_guardar.setObjectName(
            "btnGuardar"
        )

        self.btn_nuevo = QPushButton(
            "Nuevo"
        )

        self.btn_nuevo.setObjectName(
            "btnNuevo"
        )

        self.btn_eliminar = QPushButton(
            "Eliminar"
        )

        self.btn_eliminar.setObjectName(
            "btnEliminar"
        )

        self.btn_eliminar.setEnabled(
            False
        )

        fila_botones.addWidget(
            self.btn_guardar
        )

        fila_botones.addWidget(
            self.btn_nuevo
        )

        fila_botones.addWidget(
            self.btn_eliminar
        )

        layout.addLayout(
            fila_botones
        )

        # ===========================
        # TABLA
        # ===========================

        self.tabla = QTableWidget()

        self.tabla.setColumnCount(9)

        self.tabla.setHorizontalHeaderLabels([
            "ID",
            "Reporte",
            "Tipo",
            "Gravedad",
            "Provincia",
            "Cantón",
            "Distrito",
            "Heridos",
            "Costo"
        ])

        self.tabla.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch
        )

        layout.addWidget(
            self.tabla
        )

        IncidenteWidget.setLayout(
            layout
        )