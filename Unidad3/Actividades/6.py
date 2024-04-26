import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QPushButton, QTextEdit

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Reporte de Kilómetros Recorridos")
        self.setGeometry(100, 100, 500, 500)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.label = QLabel("Ingrese los datos de los choferes:")
        self.layout.addWidget(self.label)

        self.text_edit = QTextEdit()
        self.layout.addWidget(self.text_edit)

        self.button = QPushButton("Generar Reporte")
        self.button.clicked.connect(self.generar_reporte)
        self.layout.addWidget(self.button)

        self.result_label = QLabel("")
        self.layout.addWidget(self.result_label)

    def generar_reporte(self):
        datos = self.text_edit.toPlainText()
        choferes = datos.strip().split('\n')

        reporte = {}

        for chofer in choferes:
            nombre, *kilometros = chofer.split()
            if len(kilometros) >= 7:  # Verificar que haya suficientes elementos en la lista de kilómetros
                kilometros = list(map(int, kilometros))
                total_semana = sum(kilometros)
                reporte[nombre] = {
                    'Lunes': kilometros[0],
                    'Martes': kilometros[1],
                    'Miércoles': kilometros[2],
                    'Jueves': kilometros[3],
                    'Viernes': kilometros[4],
                    'Sábado': kilometros[5],
                    'Domingo': kilometros[6],
                    'Total Semanal': total_semana
                }
            else:
                print(f"Error en los datos de {nombre}: No se proporcionaron suficientes datos para los 7 días.")

        resultado = "Reporte de Kilómetros Recorridos:\n\n"
        for nombre, datos in reporte.items():
            resultado += f"{nombre}:\n"
            for dia, km in datos.items():
                resultado += f"{dia}: {km} km\n"
            resultado += f"Total Semanal: {datos['Total Semanal']} km\n\n"

        self.result_label.setText(resultado)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
