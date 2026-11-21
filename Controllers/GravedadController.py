from PySide6.QtWidgets import (
    QWidget,
    QMessageBox,
    QTableWidgetItem
)

from View.Gravedad_ui import Ui_Gravedad
from Models.Gravedad import Gravedad


class GravedadController(QWidget):

    def __init__(self, parent=None):

        super().__init__(parent)

        self.ui = Ui_Gravedad()
        self.ui.setupUi(self)

        self.gravedad_editando_id = None

        self.ui.btn_guardar.clicked.connect(
            self.guardar
        )

        self.ui.btn_nuevo.clicked.connect(
            self.limpiar_form
        )

        self.ui.btn_eliminar.clicked.connect(
            self.eliminar
        )

        self.ui.tabla.itemSelectionChanged.connect(
            self.fila_seleccionada
        )

        self.cargar_tabla()

    def cargar_tabla(self):

        self.ui.tabla.setRowCount(0)

        datos = Gravedad.get_all()

        for doc in datos:

            fila = self.ui.tabla.rowCount()

            self.ui.tabla.insertRow(fila)

            self.ui.tabla.setItem(
                fila,
                0,
                QTableWidgetItem(str(doc["_id"]))
            )

            self.ui.tabla.setItem(
                fila,
                1,
                QTableWidgetItem(doc["nombre"])
            )

    def fila_seleccionada(self):

        fila = self.ui.tabla.currentRow()

        if fila < 0:
            return

        self.gravedad_editando_id = (
            self.ui.tabla.item(fila, 0).text()
        )

        self.ui.inp_nombre.setText(
            self.ui.tabla.item(fila, 1).text()
        )

        self.ui.btn_eliminar.setEnabled(True)

        self.ui.btn_guardar.setText(
            "Actualizar"
        )

    def limpiar_form(self):

        self.gravedad_editando_id = None

        self.ui.inp_nombre.clear()

        self.ui.btn_eliminar.setEnabled(
            False
        )

        self.ui.tabla.clearSelection()

        self.ui.btn_guardar.setText(
            "Guardar"
        )

    def guardar(self):

        nombre = (
            self.ui.inp_nombre.text().strip()
        )

        if not nombre:

            QMessageBox.warning(
                self,
                "Validación",
                "Ingrese un nombre."
            )

            return

        try:

            if self.gravedad_editando_id:

                gravedad = Gravedad(
                    nombre,
                    self.gravedad_editando_id
                )

                gravedad.update()

            else:

                gravedad = Gravedad(
                    nombre
                )

                gravedad.insertar()

            self.limpiar_form()
            self.cargar_tabla()

        except Exception as e:

            QMessageBox.critical(
                self,
                "Error",
                str(e)
            )

    def eliminar(self):

        if not self.gravedad_editando_id:
            return

        respuesta = QMessageBox.question(
            self,
            "Confirmar",
            "¿Desea eliminar el registro?",
            QMessageBox.Yes |
            QMessageBox.No
        )

        if respuesta == QMessageBox.Yes:

            gravedad = Gravedad(
                "",
                self.gravedad_editando_id
            )

            gravedad.delete()

            self.limpiar_form()
            self.cargar_tabla()