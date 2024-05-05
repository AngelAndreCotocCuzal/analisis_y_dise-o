from PyQt5.uic import loadUiType
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem
from modelos.control_cocina import ModeloCocina
from modelos.control_usuario import ModeloUsuario
from modelos.control_TipoUsuario import ModeloTipoUsuario
from modelos.control_huesped import ModeloHuesped
import bcrypt

Ui_MainWindow, QMainWindow = loadUiType('view/interfaz.ui')

class Main_menuPrincipal(QMainWindow, Ui_MainWindow):
    def __init__(self, user, main_login) -> None:
        self.ModeloCocina = ModeloCocina()
        self.ModeloUsuario = ModeloUsuario()
        self.ModeloTipoUsuario = ModeloTipoUsuario()
        self.ModeloHuesped = ModeloHuesped()
        # self.model = Modelo_pro()
        super().__init__()
        self.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        # -------------------------- Conectar Botones con Pagina  ---------------------------
        self.btn_habitacion.clicked.connect(self.mostrar_pagina_habitacion)
        self.btn_cocina.clicked.connect(self.mostrar_pagina_cocina)
        self.btn_registro.clicked.connect(self.mostrar_pagina_registro)
        self.btn_usuario.clicked.connect(self.mostrar_pagina_usuario)
        # -------------------------- Botones Cocina ------------------------------------------

        self.btn_listar.clicked.connect(lambda: self.ModeloCocina.listarAlimento(self.tabla_cocina))
        self.btn_eliminar_c.clicked.connect(lambda: self.ModeloCocina.eliminarAlimento(self.tabla_cocina))
        self.btn_actualizar_c.clicked.connect(lambda: self.ModeloCocina.actualizarAlimento(self.tabla_cocina))
        self.btn_agregar_c.clicked.connect(lambda: self.ModeloCocina.CrearAlimento(self.lnl_producto.text(),
                                                                                        self.lnl_entrada.text(),
                                                                                        self.lnl_vencimiento.text(), 
                                                                                        self.tabla_cocina))

        # --------------------------------- Botones Usuario ----------------------------------

        self.btn_register_6.clicked.connect(self.registrar)
        self.btn_register_6.clicked.connect(self.limpiar_labels_register)
        self.btn_listar_u.clicked.connect(lambda: self.ModeloUsuario.listarUsuario(self.tabla_usuario))
        self.btn_eliminar_u.clicked.connect(lambda: self.ModeloUsuario.eliminarUsuario(self.tabla_usuario))
        self.btn_actualizar_u.clicked.connect(lambda: self.ModeloUsuario.actualizarUsuario(self.tabla_usuario))
        self.btn_tipoUsuario.clicked.connect(self.mostrar_pagina_tipoUsuario)
        
        # ----------------------------------- Botones Tipo Usuario ----------------------------
        
        self.btn_volver.clicked.connect(self.mostrar_pagina_usuario)
        self.btn_listar_Tipo.clicked.connect(lambda: self.ModeloTipoUsuario.listarTipoUsuario(self.tabla_tipo_usuario))
        self.btn_eliminarTipo.clicked.connect(lambda: self.ModeloTipoUsuario.eliminarTipoUsuario(self.tabla_tipo_usuario))
        self.btn_actualizarTipo.clicked.connect(lambda: self.ModeloTipoUsuario.actualizarTipoUsuario(self.tabla_tipo_usuario))
        self.btn_crear_tipo.clicked.connect(lambda: self.ModeloTipoUsuario.CrearTipoUsuario(self.lnx_tipoUsusario.text(),
                                                                                            self.tabla_tipo_usuario))
    
        # ------------------------------------------- Botones huesped ------------------------------
        self.btn_listarH.clicked.connect(lambda: self.ModeloHuesped.listarHuesped(self.tablaHuesped))
        self.btn_eliminarH.clicked.connect(lambda: self.ModeloHuesped.eliminarHueped(self.tablaHuesped))
        self.btn_actualizarH.clicked.connect(lambda: self.ModeloHuesped.actuaizarHuesped(self.tablaHuesped))
        self.btn_ingresarH.clicked.connect(lambda: self.ModeloHuesped.CrearHuesped(self.lnl_nombreH.text(),
                                                                                    self.lnl_dpiH.text(),
                                                                                    float(self.lnl_anticipo.text()),
                                                                                    self.lnl_entradaH.text(),
                                                                                    self.lnl_salidaH.text(),
                                                                                            self.tablaHuesped))
    
    def mostrar_pagina_habitacion(self):
        self.stackedWidget.setCurrentWidget(self.pg_habitacion)
    
    def mostrar_pagina_cocina(self):
        # Cambiamos a la página de la cocina
        self.stackedWidget.setCurrentWidget(self.pg_cocina)
        
    def mostrar_pagina_registro(self):
        self.stackedWidget.setCurrentWidget(self.pg_registro)
        
    def mostrar_pagina_usuario(self):
        self.stackedWidget.setCurrentWidget(self.pg_usuario)
        
    def mostrar_pagina_tipoUsuario(self):
        self.stackedWidget.setCurrentWidget(self.page_tipoUsuario)
    
    def registrar(self):
        nombre = self.lnx_1nombre_2.text()
        user = self.lnx_usuario_2.text()
        cargo = self.cb_min_2.currentText()
        pw = self.lnx_password_3.text()
        pw_confirm = self.lnx_confirm_password_2.text()

        if pw == pw_confirm:
            pw = str(pw)

            salt = bcrypt.gensalt()

            # Encripta la contraseña del usuario
            hashed_password = bcrypt.hashpw(pw.encode('utf-8'), salt)
            if cargo == "Gerente":
                self.ModeloUsuario.CrearUsuario(nombre, user, hashed_password, 1, self.tabla_usuario)
            elif cargo == "Empleado":
                self.ModeloUsuario.CrearUsuario(nombre, user, hashed_password, 2, self.tabla_usuario)
            # Insertar la contraseña segura como una cadena de texto en la base de datos


        else:
            print("las contraseñas no coinciden")

    def limpiar_labels_register(self):
        self.lnx_1nombre_2.clear()
        self.lnx_confirm_password_2.clear()
        self.lnx_password_3.clear()
        self.lnx_usuario_2.clear()


        