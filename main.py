import sys
from datetime import datetime

from PyQt6.QtWidgets import QApplication, QVBoxLayout, QLabel, QWidget, QGridLayout, QLineEdit, QPushButton, QComboBox

class SpeedCalculator(QWidget):  #inherit from qwidget, because it creates windows
    def __init__(self):
        super().__init__()   #returns parent of a class being called
        self.setWindowTitle('Age Calculator')
        grid = QGridLayout()

        # creates widgets
        distance_label = QLabel('Distance')
        distance_line_edit = QLineEdit()

        combo = QComboBox()
        combo.addItems(['Meters(Km)', 'Miles'])

        time_hours_label = QLabel('Time(hours)')
        time_hours_line_edit = QLineEdit()

        calculate_button = QPushButton('Calculate')
        self.output_label = QLabel('')

        grid.addWidget(distance_label, 0, 0)
        grid.addWidget(distance_line_edit, 0, 1)
        grid.addWidget(time_hours_label, 1, 0)
        grid.addWidget(time_hours_line_edit, 1, 1)
        grid.addWidget(calculate_button, 3, 0, 1, 2, )
        grid.addWidget(combo,  2, 0, 1, 2)

        self.setLayout(grid)


app = QApplication(sys.argv)
age_calculator = SpeedCalculator()
age_calculator.show()
sys.exit(app.exec())