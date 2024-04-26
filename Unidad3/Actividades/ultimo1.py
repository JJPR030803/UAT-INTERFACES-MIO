import sys
import matplotlib as plt
from matplotlib.backends.backend_qt6agg import FigureCanvasQTAgg as FigureCanvas
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel,QTextEdit,QGraphicsLayout,QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Graficacion")
        self.setGeometry(100, 100, 800, 800)

        self.color_linea_label = QLabel("Color de la linea", self)
        self.color_linea_label.move(50, 50)
        ######POLINOMIO######
        self.polinomio_label = QLabel("Polinomio",self)
        self.polinomio_label.move(100,100)
        self.polinomio_edit = QTextEdit(self)
        self.polinomio_edit.move(160,100)
        
        ##### TITULO #######
        self.titulo_label = QLabel("Titulo",self)
        self.titulo_label.move(100,150)
        self.titulo_edit = QTextEdit(self)
        self.titulo_edit.move(160,150)
        
        #### BOTON GRAFICAR #####
        self.boton_graficar = QPushButton(self,text="Graficar",)
        self.boton_graficar.move(280,100)
        
        
         #### BOTON ESTABLECER #####
        self.boton_graficar = QPushButton(self,text="Establecer",)
        self.boton_graficar.move(280,150)
        
        
         #### BOTON LIMPIAR GRAFICO #####
        self.boton_graficar = QPushButton(self,text="Limpiar Grafico",)
        self.boton_graficar.move(280,200)
        
        
        ###X MINIMO#####
        self.label_xmin = QLabel("Xmin:",self)
        self.label_xmin.move(450,50)
        self.xmin_textedit = QTextEdit(self,)
        self.xmin_textedit.move(490,50)
        ###X MAXIMO##
        self.label_xmax = QLabel("Xmax:",self)
        self.label_xmax.move(600,50)
        self.xmax_textedit = QTextEdit(self,)
        self.xmax_textedit.move(650,50)
        ###X DIVISIONES  ##
        self.label_xmax = QLabel("Xdivisiones:",self)
        self.label_xmax.move(450,150)
        self.xmax_textedit = QTextEdit(self,)
        self.xmax_textedit.move(490,150)
        ####Y MINIMO######
        self.label_ymin = QLabel("Ymin:",self)
        self.label_ymin.move(450,100)
        self.ymin_textedit = QTextEdit(self,)
        self.ymin_textedit.move(490,100)
        ####Y Maximo######
        self.label_ymax = QLabel("Ymax:",self)
        self.label_ymax.move(600,100)
        self.ymax_textedit = QTextEdit(self,)
        self.ymax_textedit.move(650,100)
        
         ####Y DIVISIONES  ######
        self.label_ymax = QLabel("YDivisiones:",self)
        self.label_ymax.move(600,150)
        self.ymax_textedit = QTextEdit(self,)
        self.ymax_textedit.move(650,150)
        
        #####   GRAFICA #####
        self.plot_widget = QWidget(self)
        self.plot_widget.move(400,400)
    
    
        #####BOTON##

       # self.button = QPushButton("Button", self)
        #self.button.move(200, 150)
        
    def plot_graph(self):
        # Get data for the plot from text fields or other sources
        x_values = [1, 2, 3, 4, 5]
        y_values = [2, 3, 4, 5, 6]

        # Generate the plot using Matplotlib
        plt.figure()
        plt.plot(x_values, y_values)
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Graph Title')

        # Create a Matplotlib canvas
        canvas = FigureCanvas(plt.gcf())

        # Clear the plot widget and add the canvas
        layout = QVBoxLayout(self.plot_widget)
        layout.addWidget(canvas)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        




if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())
