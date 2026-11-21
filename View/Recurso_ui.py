from PySide6.QtWidgets import (
    QLabel,
    QLineEdit,
    QPushButton,
    QTableWidget,
    QHeaderView,
    QVBoxLayout,
    QHBoxLayout
)

from View.estilos import STYLE_CRUD


class Ui_Recurso:

    def setupUi(self, RecursoWidget):

        RecursoWidget.setObjectName(
            "CrudWidget"
        )

        RecursoWidget.setStyleSheet(
            STYLE_CRUD
        )

        layout = QVBoxLayout(
            RecursoWidget
        )

        self.lbl_titulo = QLabel(
            "Gestión de Recursos"
        )

        self.lbl_titulo.setObjectName(
            "titulo"
        )

        layout.addWidget(
            self.lbl_titulo
        )

        self.lbl_seccion = QLabel(
            "RECURSOS DE EMERGENCIA"
        )

        self.lbl_seccion.setObjectName(
            "seccion"
        )

        layout.addWidget(
            self.lbl_seccion
        )

        self.inp_nombre = QLineEdit()

        self.inp_nombre.setPlaceholderText(
            "Nombre del recurso"
        )

        layout.addWidget(
            self.inp_nombre
        )

        botones = QHBoxLayout()

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

        self.btn_eliminar.setEnabled(False)

        botones.addWidget(
            self.btn_guardar
        )

        botones.addWidget(
            self.btn_nuevo
        )

        botones.addWidget(
            self.btn_eliminar
        )

        layout.addLayout(
            botones
        )

        self.tabla = QTableWidget()

        self.tabla.setColumnCount(2)

        self.tabla.setHorizontalHeaderLabels([
            "ID",
            "Nombre"
        ])

        self.tabla.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )

        layout.addWidget(
            self.tabla
        )