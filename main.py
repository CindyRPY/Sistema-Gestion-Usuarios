import sys

from PySide6.QtWidgets import QApplication

from Controllers.loginController import loginController

if __name__ == "__main__":

    app = QApplication(sys.argv)

    ventana = loginController()

    ventana.show()

    sys.exit(app.exec())