from PySide6.QtCore import Qt

from PySide6.QtWidgets import (
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QFrame
)


class Ui_Login:

    def setupUi(self, Login):

        Login.setObjectName("LoginWidget")

        layout = QVBoxLayout(Login)

        layout.setContentsMargins(100, 80, 100, 80)
        layout.setSpacing(15)

        self.card = QFrame()
        self.card.setObjectName("cardLogin")

        card_layout = QVBoxLayout(self.card)

        self.lbl_titulo = QLabel("🚦 CookieVial CR")
        self.lbl_titulo.setStyleSheet("""
            font-size:28px;
            font-weight:bold;
            color:#55B590;
            """)
        self.lbl_titulo.setAlignment(Qt.AlignCenter)

        self.lbl_subtitulo = QLabel(
            "Sistema de Gestión de Incidentes Viales"
        )
        self.lbl_subtitulo.setStyleSheet("""            
            font-size:13px;            
            color:#D1D5DB;
            """)
        self.lbl_subtitulo.setAlignment(Qt.AlignCenter)

        self.txt_usuario = QLineEdit()
        self.txt_usuario.setPlaceholderText("Usuario")

        self.txt_password = QLineEdit()
        self.txt_password.setPlaceholderText("Contraseña")
        self.txt_password.setEchoMode(QLineEdit.Password)

        self.btn_login = QPushButton("Iniciar Sesión")

        card_layout.addWidget(self.lbl_titulo)
        card_layout.addWidget(self.lbl_subtitulo)
        card_layout.addWidget(self.txt_usuario)
        card_layout.addWidget(self.txt_password)
        card_layout.addWidget(self.btn_login)

        layout.addStretch()
        layout.addWidget(self.card)
        layout.addStretch()