from PySide6.QtWidgets import QWidget, QMessageBox
from View.Login_ui import Ui_Login
from Models.Usuario import Usuario
from View.MainWindow import MainWindow


class loginController(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Login()
        self.ui.setupUi(self)

        self.ui.btn_login.clicked.connect(
            self.iniciar_sesion
        )

    def iniciar_sesion(self):

        usuario = self.ui.txt_usuario.text().strip()
        password = self.ui.txt_password.text().strip()

        if not usuario or not password:

            QMessageBox.warning(
                self,
                "Advertencia",
                "Debe completar usuario y contraseña."
            )

            return

        user = Usuario.login(
            usuario,
            password
        )

        if user:

            try:

                rol = user["rol"]

                QMessageBox.information(
                    self,
                    "Bienvenido",
                    f"Bienvenido {user['nombre']}"
                )

                print("Antes de abrir MainWindow")

                self.main = MainWindow(rol)

                print("MainWindow creado")

                self.main.show()

                print("MainWindow mostrado")

                self.close()

            except Exception as e:

                QMessageBox.critical(
                    self,
                    "ERROR",
                    str(e)
                )
        else:

            QMessageBox.warning(
                self,
                "Error",
                "Usuario o contraseña incorrectos."
            )