from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QFont, QAction
from PySide6.QtWidgets import (
    QMainWindow,
    QMdiArea,
    QMdiSubWindow,
    QLabel,
    QFrame,
    QToolBar,
    QStatusBar,
)

from View.estilos import STYLE_MAIN
from Controllers.TipoIncidenteController import TipoIncidenteController
from Controllers.GravedadController import GravedadController
from Controllers.RecursoController import RecursoController
from Controllers.IncidenteController import IncidenteController
from Controllers.GraficosController import GraficosController


class MainWindow(QMainWindow):

    def __init__(self, rol):

        super().__init__()

        self.rol = rol

        self.setWindowTitle(
            f"CookieVial CR - {rol}"
        )

        self.setMinimumSize(1200, 700)

        self.setFont(QFont("Segoe UI", 10))

        self.setStyleSheet(STYLE_MAIN)

        # Área MDI

        self.mdi = QMdiArea()

        self.mdi.setHorizontalScrollBarPolicy(
            Qt.ScrollBarAsNeeded
        )

        self.mdi.setVerticalScrollBarPolicy(
            Qt.ScrollBarAsNeeded
        )

        self.setCentralWidget(self.mdi)

        self._crear_toolbar()
        self._crear_statusbar()

        self.configurar_permisos()

        self.showMaximized()

    # ==================================
    # TOOLBAR
    # ==================================

    def _crear_toolbar(self):

        toolbar = QToolBar("Principal")

        toolbar.setMovable(False)

        toolbar.setIconSize(QSize(18, 18))

        self.addToolBar(toolbar)

        lbl_app = QLabel(
            f"🚦 CookieVial CR | {self.rol}"
        )

        lbl_app.setStyleSheet("""
            color:#5EE9B5;
            font-size:15px;
            font-weight:bold;
        """)

        toolbar.addWidget(lbl_app)

        sep = QFrame()
        sep.setFrameShape(QFrame.VLine)

        toolbar.addWidget(sep)

        self.act_usuarios = QAction(
            "Usuarios",
            self
        )

        toolbar.addAction(self.act_usuarios)

        self.act_reportes = QAction(
            "Reportes",
            self
        )

        toolbar.addAction(self.act_reportes)

        # ===============================
        # CRUDS
        # ===============================

        self.act_gravedad = QAction(
            "Gravedad",
            self
        )

        self.act_gravedad.triggered.connect(
            self.abrir_gravedad
        )

        toolbar.addAction(
            self.act_gravedad
        )

        self.act_tipo_incidente = QAction(
            "Tipo Incidente",
            self
        )

        self.act_tipo_incidente.triggered.connect(
            self.abrir_tipo_incidente
        )

        toolbar.addAction(
            self.act_tipo_incidente
        )

        self.act_recursos = QAction(
            "Recursos",
            self
        )

        self.act_recursos.triggered.connect(
            self.abrir_recursos
        )

        toolbar.addAction(
            self.act_recursos
        )

        self.act_incidentes = QAction(
            "Incidentes",
            self
        )

        self.act_incidentes.triggered.connect(
            self.abrir_incidentes
        )

        toolbar.addAction(
            self.act_incidentes
        )

        self.act_graficos = QAction(
            "Gráficos",
            self
        )

        self.act_graficos.triggered.connect(
            self.abrir_graficos
        )

        toolbar.addAction(
            self.act_graficos
        )

    # ==================================
    # STATUS BAR
    # ==================================

    def _crear_statusbar(self):

        status = QStatusBar()

        status.showMessage(
            f"Usuario autenticado | Rol: {self.rol}"
        )

        self.setStatusBar(status)

    # ==================================
    # PERMISOS
    # ==================================

    def configurar_permisos(self):


        if self.rol == "Administrador":

            self.act_usuarios.setVisible(False)
            
            self.act_reportes.setVisible(False)


        elif self.rol == "Digitador":

            self.act_usuarios.setVisible(False)

            self.act_gravedad.setVisible(False)

            self.act_tipo_incidente.setVisible(False)

            self.act_recursos.setVisible(False)

            self.act_reportes.setVisible(False)

        elif self.rol == "Consulta":

            self.act_usuarios.setVisible(False)

            self.act_gravedad.setVisible(False)

            self.act_tipo_incidente.setVisible(False)

            self.act_recursos.setVisible(False)

            self.act_reportes.setVisible(False)

    # ==================================
    # ABRIR CRUD GRAVEDAD
    # ==================================

    def abrir_gravedad(self):

        self.abrir_subventana(
            "Gravedad",
            GravedadController(),
            size=(900, 600)
        )

    # ==================================
    # SUBVENTANAS
    # ==================================

    def abrir_subventana(
        self,
        titulo,
        controller,
        size=None
    ):

        # Buscar si ya existe una ventana abierta
        for sub in self.mdi.subWindowList():

            if sub.windowTitle() == titulo:

                # Si está minimizada, restaurarla
                if sub.isMinimized():
                    sub.showNormal()

                # Activarla
                self.mdi.setActiveSubWindow(sub)

                return

        # Crear nueva subventana
        sub = QMdiSubWindow()

        # Botones de la ventana
        sub.setWindowFlags(
            Qt.WindowType.SubWindow |
            Qt.WindowType.WindowMinimizeButtonHint |
            Qt.WindowType.WindowMaximizeButtonHint |
            Qt.WindowType.WindowCloseButtonHint
        )

        # IMPORTANTE:
        # Cuando se cierre con X, eliminar completamente
        sub.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose, True)

        # Colocar el Controller dentro
        sub.setWidget(controller)

        sub.setWindowTitle(titulo)

        self.mdi.addSubWindow(sub)

        if size:
            sub.resize(*size)

        sub.show()



    def abrir_tipo_incidente(self):

        self.abrir_subventana(
            "Tipo Incidente",
            TipoIncidenteController(),
            size=(900, 600)
        )

    def abrir_recursos(self):

        self.abrir_subventana(
            "Recursos",
            RecursoController(),
            size=(900, 600)
        )

    def abrir_incidentes(self):

        self.abrir_subventana(
            "Incidentes",
            IncidenteController(self.rol),
            size=(1100, 700)
        )

    def abrir_graficos(self):

        self.abrir_subventana(

            "Gráficos",

            GraficosController(),

            size=(1000, 700)
        )