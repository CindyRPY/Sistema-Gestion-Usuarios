# -*- coding: utf-8 -*- 
# UI del módulo de Gráficos. Solo construye los widgets y el layout; 
# la lógica (consultas a Mongo, dibujado) vive en Controllers/GraficosController.py 
  
from PySide6.QtCore import Qt 
from PySide6.QtWidgets import ( 
    QWidget, QVBoxLayout, QHBoxLayout, 
    QLabel, QPushButton, QComboBox, QFrame, 
) 
  
from View.estilos import STYLE_CRUD 
  
  
class Ui_Graficos(object): 
    def setupUi(self, Graficos): 
        if not Graficos.objectName(): 
            Graficos.setObjectName(u"CrudWidget") 
        Graficos.setStyleSheet(STYLE_CRUD) 
  
        root = QVBoxLayout(Graficos) 
        root.setContentsMargins(20, 18, 20, 18) 
        root.setSpacing(14) 
  
        # ── Cabecera ────────────────────────────────────── 
        cab = QHBoxLayout() 
        self.titulo = QLabel() 
        self.titulo.setObjectName("titulo") 
        cab.addWidget(self.titulo) 
        cab.addStretch() 
  
        self.btn_refresh = QPushButton() 
        self.btn_refresh.setObjectName("btnRefresh") 
        self.btn_refresh.setCursor(Qt.PointingHandCursor) 
        cab.addWidget(self.btn_refresh) 
        root.addLayout(cab) 
  
        # ── Selector de gráfico ───────────────────────────── 
        self.sec_selector = QLabel() 
        self.sec_selector.setObjectName("seccion") 
        root.addWidget(self.sec_selector) 
  
        sel_row = QHBoxLayout() 
        sel_row.setSpacing(10) 
  
        self.lbl_tipo = QLabel() 
        self.combo_grafico = QComboBox() 
        self.combo_grafico.setMinimumWidth(320) 
  
        sel_row.addWidget(self.lbl_tipo) 
        sel_row.addWidget(self.combo_grafico) 
        sel_row.addStretch() 
        root.addLayout(sel_row) 
  
        # ── Separador ───────────────────────────────────── 
        sep = QFrame() 
        sep.setObjectName("separador") 
        sep.setFrameShape(QFrame.HLine) 
        root.addWidget(sep) 
  
        # ── Contenedor del gráfico (el canvas se agrega desde el controlador) ── 
        self.sec_grafico = QLabel() 
        self.sec_grafico.setObjectName("seccion") 
        root.addWidget(self.sec_grafico) 
  
        self.frame_canvas = QFrame() 
        self.frame_canvas.setObjectName("frameCanvas") 
        self.frame_canvas.setStyleSheet( 
            "QFrame#frameCanvas { background-color: #1e2130; border: 1px solid #2a2d3e; border-radius: 8px; }" 
        ) 
        self.layout_canvas = QVBoxLayout(self.frame_canvas) 
        self.layout_canvas.setContentsMargins(10, 10, 10, 10) 
        root.addWidget(self.frame_canvas, stretch=1) 
  
        self.retranslateUi(Graficos) 
  
    def retranslateUi(self, Graficos): 
        self.titulo.setText("Reportes e Indicadores Viales") 
        self.btn_refresh.setText("↻  Actualizar datos") 
        self.sec_selector.setText("SELECCIONE EL GRÁFICO") 
        self.lbl_tipo.setText("Tipo de gráfico:") 
        self.sec_grafico.setText("VISUALIZACIÓN")