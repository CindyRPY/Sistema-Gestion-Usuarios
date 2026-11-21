STYLE_MAIN = """
QMainWindow {
    background-color: #111827;
}

QMdiArea {
    background-color: #111827;
    border: none;
}

QToolBar {
    background-color: #1F2937;
    border: none;
    spacing: 8px;
    padding: 10px;
}

QToolBar QToolButton {
    background-color: transparent;
    color: white;
    border-radius: 8px;
    padding: 8px 14px;
    font-weight: bold;
}

QToolBar QToolButton:hover {
    background-color: #55B590;
}

QStatusBar {
    background-color: #1F2937;
    color: #9CA3AF;
    border-top: 1px solid #374151;
}
"""
  
STYLE_CRUD = """ 
QWidget#CrudWidget { 
    background-color: #1a1d27; 
    border-radius: 10px; 
} 
  
/* ── Etiquetas ── */ 
QLabel { 
    color: #a0aec0; 
    font-size: 12px; 
} 
QLabel#titulo { 
    color: #55B590; 
    font-size: 18px; 
    font-weight: bold; 
} 
QLabel#seccion { 
    color: #6b7280; 
    font-size: 11px; 
    font-weight: bold; 
    letter-spacing: 1px; 
} 
  
/* ── Inputs ── */ 
QLineEdit, QDoubleSpinBox, QSpinBox, QComboBox { 
    background-color: #252836; 
    border: 1px solid #2a2d3e; 
    border-radius: 6px; 
    color: #e0e0e0; 
    padding: 6px 10px; 
    font-size: 13px; 
    selection-background-color: #55B590; 
} 
QLineEdit:focus, QDoubleSpinBox:focus, QSpinBox:focus, QComboBox:focus { 
    border: 1px solid #55B590; 
    background-color: #2a2d3e; 
} 
QComboBox::drop-down { 
    border: none; 
    width: 24px; 
} 
QComboBox QAbstractItemView { 
    background-color: #252836; 
    border: 1px solid #2a2d3e; 
    color: #e0e0e0; 
    selection-background-color: #55B590; 
} 
  
/* ── Tabla ── */ 
QTableWidget { 
    background-color: #1e2130; 
    border: 1px solid #2a2d3e; 
    border-radius: 8px; 
    gridline-color: #2a2d3e; 
    color: #e0e0e0; 
    font-size: 13px; 
    selection-background-color: #2d3154; 
    outline: none; 
} 
QTableWidget::item { 
    padding: 6px 10px; 
    border-bottom: 1px solid #2a2d3e; 
} 
QTableWidget::item:selected { 
    background-color: #2d3154; 
    color: #c0c8ff; 
} 
QHeaderView::section { 
    background-color: #13151f; 
    color: #55B590; 
    font-weight: bold; 
    font-size: 12px; 
    padding: 8px 10px; 
    border: none; 
    border-bottom: 2px solid #55B590; 
    letter-spacing: 0.5px; 
} 
  
/* ── Botones principales ── */ 
QPushButton#btnGuardar { 
    background-color: #55B590; 
    color: #ffffff; 
    border: none; 
    border-radius: 7px; 
    padding: 9px 20px; 
    font-size: 13px; 
    font-weight: bold; 
} 
QPushButton#btnGuardar:hover { 
    background-color: #6DCCA7; 
} 
QPushButton#btnGuardar:pressed { 
    background-color: #3F9976; 
} 
  
QPushButton#btnNuevo { 
    background-color: #252836; 
    color: #a0aec0; 
    border: 1px solid #2a2d3e; 
    border-radius: 7px; 
    padding: 9px 20px; 
    font-size: 13px; 
} 
QPushButton#btnNuevo:hover { 
    background-color: #2a2d3e; 
    color: #e0e0e0; 
} 
  
QPushButton#btnEliminar { 
    background-color: transparent; 
    color: #f87171; 
    border: 1px solid #3d2020; 
    border-radius: 7px; 
    padding: 9px 20px; 
    font-size: 13px; 
} 
QPushButton#btnEliminar:hover { 
    background-color: #3d2020; 
} 
QPushButton#btnEliminar:disabled { 
    color: #4a3030; 
    border-color: #2a2020; 
} 
  
QPushButton#btnRefresh { 
    background-color: transparent; 
    color: #6b7280; 
    border: 1px solid #2a2d3e; 
    border-radius: 7px; 
    padding: 9px 16px; 
    font-size: 13px; 
} 
QPushButton#btnRefresh:hover { 
    color: #e0e0e0; 
    border-color: #4a4d5e; 
} 
  
/* ── Separador ── */ 
QFrame#separador { 
    background-color: #2a2d3e; 
    max-height: 1px; 
} 
  
/* ── Scrollbar ── */ 
QScrollBar:vertical { 
    background: #1a1d27; 
    width: 8px; 
    border-radius: 4px; 
} 
QScrollBar::handle:vertical { 
    background: #2a2d3e; 
    border-radius: 4px; 
    min-height: 30px; 
} 
QScrollBar::handle:vertical:hover { 
    background: #6DCCA7; 
} 
QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical { 
    height: 0px; 
} 
""" 
STYLE_LOGIN = """
QWidget{
    background-color:#111827;
}

QFrame#cardLogin{
    background-color:#1F2937;
    border-radius:18px;
    padding:20px;
}

QLabel{
    color:white;
}

QLineEdit{
    background-color:#273446;
    color:white;
    border:2px solid transparent;
    border-radius:10px;
    padding:10px;
    font-size:14px;
}

QLineEdit:focus{
    border:2px solid #55B590;
}

QPushButton{
    background-color:#55B590;
    color:white;
    border:none;
    border-radius:10px;
    padding:12px;
    font-weight:bold;
}

QPushButton:hover{
    background-color:#6DCCA7;
}
"""