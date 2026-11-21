from PySide6.QtWidgets import (
    QWidget,
    QMessageBox,
    QTableWidgetItem
)

from View.Incidente_ui import Ui_Incidente

from Models.Incidente import Incidente
from Models.TipoIncidente import TipoIncidente
from Models.Gravedad import Gravedad
from Models.Recurso import Recurso
from Api.TerritorialService import TerritorialService

class IncidenteController(QWidget):

    def __init__(self, rol, parent=None):

        super().__init__(parent)

        self.rol = rol
         
        self.ui = Ui_Incidente()
        self.ui.setupUi(self)
        self.territorio = TerritorialService()

        self.cargar_provincias()

        self.ui.cmb_provincia.currentIndexChanged.connect(
            self.cargar_cantones
        )

        self.ui.cmb_canton.currentIndexChanged.connect(
            self.cargar_distritos
        )


        self.cargar_combos()

        # TEMPORAL HASTA CONECTAR API
        self.ui.cmb_provincia.addItem("Alajuela")
        self.ui.cmb_canton.addItem("San Ramón")
        self.ui.cmb_distrito.addItem("Santiago")

        self.cargar_tabla()

        self.ui.btn_guardar.clicked.connect(
            self.guardar
        )

        self.id_incidente = None

        self.ui.tabla.itemSelectionChanged.connect(
            self.fila_seleccionada
        )

        self.ui.btn_nuevo.clicked.connect(
            self.limpiar_form
        )

        self.ui.btn_eliminar.clicked.connect(
            self.eliminar
        )
        self.configurar_permisos()

    def cargar_combos(self):

        self.ui.cmb_tipo.clear()

        tipos = TipoIncidente.get_all()

        for tipo in tipos:

            self.ui.cmb_tipo.addItem(
                tipo["nombre"]
            )

        self.ui.cmb_gravedad.clear()

        gravedades = Gravedad.get_all()

        for gravedad in gravedades:

            self.ui.cmb_gravedad.addItem(
                gravedad["nombre"]
            )

        self.ui.cmb_recurso.clear()

        recursos = Recurso.get_all()

        for recurso in recursos:

            self.ui.cmb_recurso.addItem(
                recurso["nombre"]
            )

    def guardar(self):

        numero_reporte = (
            self.ui.inp_reporte.text().strip()
        )

        if not numero_reporte:

            QMessageBox.warning(
                self,
                "Validación",
                "Ingrese un número de reporte."
            )

            return

        fecha = self.ui.inp_fecha.date().toString(
            "yyyy-MM-dd"
        )

        tipo = self.ui.cmb_tipo.currentText()

        gravedad = self.ui.cmb_gravedad.currentText()

        vehiculos = self.ui.spn_vehiculos.value()

        heridos = self.ui.spn_heridos.value()

        fallecidos = self.ui.spn_fallecidos.value()

        etapa = self.ui.cmb_etapa.currentText()

        recurso = self.ui.cmb_recurso.currentText()

        tiempo = self.ui.spn_tiempo.value()

        costo = self.ui.spn_costo.value()

        provincia = (
            self.ui.cmb_provincia.currentText()
        )

        canton = (
            self.ui.cmb_canton.currentText()
        )

        distrito = (
            self.ui.cmb_distrito.currentText()
        )

        observaciones = (
            self.ui.txt_observaciones.toPlainText()
        )

        try:

            incidente = Incidente(
                numero_reporte,
                fecha,
                tipo,
                gravedad,
                vehiculos,
                heridos,
                fallecidos,
                etapa,
                recurso,
                tiempo,
                costo,
                provincia,
                canton,
                distrito,
                observaciones
            )

            incidente.insertar()

            QMessageBox.information(
                self,
                "Éxito",
                "Incidente registrado correctamente."
            )

            self.limpiar_form()

            self.cargar_tabla()

        except Exception as e:

            QMessageBox.critical(
                self,
                "Error",
                str(e)
            )

    def cargar_tabla(self):

        self.ui.tabla.setRowCount(0)

        datos = Incidente.get_all()

        for doc in datos:

            fila = self.ui.tabla.rowCount()

            self.ui.tabla.insertRow(fila)

            self.ui.tabla.setItem(
                fila,
                0,
                QTableWidgetItem(
                    str(doc["_id"])
                )
            )

            self.ui.tabla.setItem(
                fila,
                1,
                QTableWidgetItem(
                    str(doc.get(
                        "numero_reporte", ""
                    ))
                )
            )

            self.ui.tabla.setItem(
                fila,
                2,
                QTableWidgetItem(
                    str(doc.get(
                        "tipo_incidente", ""
                    ))
                )
            )

            self.ui.tabla.setItem(
                fila,
                3,
                QTableWidgetItem(
                    str(doc.get(
                        "gravedad", ""
                    ))
                )
            )

            self.ui.tabla.setItem(
                fila,
                4,
                QTableWidgetItem(
                    str(doc.get(
                        "provincia", ""
                    ))
                )
            )

            self.ui.tabla.setItem(
                fila,
                5,
                QTableWidgetItem(
                    str(doc.get(
                        "canton", ""
                    ))
                )
            )

            self.ui.tabla.setItem(
                fila,
                6,
                QTableWidgetItem(
                    str(doc.get(
                        "distrito", ""
                    ))
                )
            )

            self.ui.tabla.setItem(
                fila,
                7,
                QTableWidgetItem(
                    str(doc.get(
                        "heridos", 0
                    ))
                )
            )

            self.ui.tabla.setItem(
                fila,
                8,
                QTableWidgetItem(
                    str(doc.get(
                        "costo", 0
                    ))
                )
            )
    def cargar_provincias(self):

        self.ui.cmb_provincia.clear()

        self.provincias = (
            self.territorio.obtener_provincias()
        )

        for id_prov, nombre in self.provincias.items():

            self.ui.cmb_provincia.addItem(
                nombre,
                id_prov
            )

    def cargar_cantones(self):

        self.ui.cmb_canton.clear()

        id_provincia = (
            self.ui.cmb_provincia.currentData()
        )

        if not id_provincia:
            return

        self.cantones = (
            self.territorio.obtener_cantones(
                id_provincia
            )
        )

        for id_canton, nombre in self.cantones.items():

            self.ui.cmb_canton.addItem(
                nombre,
                id_canton
            )

    def cargar_distritos(self):

        self.ui.cmb_distrito.clear()

        id_provincia = (
            self.ui.cmb_provincia.currentData()
        )

        id_canton = (
            self.ui.cmb_canton.currentData()
        )

        if not id_provincia:
            return

        if not id_canton:
            return

        distritos = (
            self.territorio.obtener_distritos(
                id_provincia,
                id_canton
            )
        )

        for _, nombre in distritos.items():

            self.ui.cmb_distrito.addItem(
                nombre
            )

    def fila_seleccionada(self):

        fila = self.ui.tabla.currentRow()

        if fila < 0:
            return

        self.id_incidente = (
            self.ui.tabla.item(fila, 0).text()
        )

        self.ui.inp_reporte.setText(
            self.ui.tabla.item(fila, 1).text()
        )

        if self.rol != "Consulta":

            self.ui.btn_guardar.setText(
                "Actualizar"
            )

        if self.rol == "Administrador":

            self.ui.btn_eliminar.setEnabled(
                True
            )

    def limpiar_form(self):

        self.id_incidente = None

        self.ui.inp_reporte.clear()

        self.ui.spn_vehiculos.setValue(0)
        self.ui.spn_heridos.setValue(0)
        self.ui.spn_fallecidos.setValue(0)
        self.ui.spn_tiempo.setValue(0)
        self.ui.spn_costo.setValue(0)

        self.ui.txt_observaciones.clear()

        self.ui.btn_eliminar.setEnabled(False)

        self.ui.btn_guardar.setText(
            "Guardar"
        )

        self.ui.tabla.clearSelection()

    def eliminar(self):

        if not self.id_incidente:
            return

        respuesta = QMessageBox.question(
            self,
            "Confirmar",
            "¿Desea eliminar el incidente?",
            QMessageBox.StandardButton.Yes |
            QMessageBox.StandardButton.No
        )

        if respuesta != QMessageBox.StandardButton.Yes:
            return

        try:

            Incidente.delete_by_id(
                self.id_incidente
            )

            QMessageBox.information(
                self,
                "Éxito",
                "Incidente eliminado correctamente."
            )

            self.limpiar_form()

            self.cargar_tabla()

        except Exception as e:

            QMessageBox.critical(
                self,
                "Error",
                str(e)
            )

    def configurar_permisos(self):

        if self.rol == "Administrador":
            return

        elif self.rol == "Digitador":

            self.ui.btn_eliminar.setVisible(False)

        elif self.rol == "Consulta":

            self.ui.btn_guardar.setVisible(False)
            self.ui.btn_nuevo.setVisible(False)
            self.ui.btn_eliminar.setVisible(False)

            self.ui.inp_reporte.setEnabled(False)
            self.ui.cmb_tipo.setEnabled(False)
            self.ui.cmb_gravedad.setEnabled(False)
            self.ui.spn_vehiculos.setEnabled(False)
            self.ui.spn_heridos.setEnabled(False)
            self.ui.spn_fallecidos.setEnabled(False)
            self.ui.cmb_etapa.setEnabled(False)
            self.ui.cmb_recurso.setEnabled(False)
            self.ui.spn_tiempo.setEnabled(False)
            self.ui.spn_costo.setEnabled(False)
            self.ui.cmb_provincia.setEnabled(False)
            self.ui.cmb_canton.setEnabled(False)
            self.ui.cmb_distrito.setEnabled(False)
            self.ui.txt_observaciones.setEnabled(False)
            