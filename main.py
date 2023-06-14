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
        self.distance_line_edit = QLineEdit()

        self.combo = QComboBox()
        self.combo.addItems(['Meters(Km)', 'Miles'])

        time_hours_label = QLabel('Time(hours)')
        self.time_hours_line_edit = QLineEdit()

        calculate_button = QPushButton('Calculate')
        calculate_button.clicked.connect(self.calculate_speed)
        self.output_label = QLabel('')

        grid.addWidget(distance_label, 0, 0)
        grid.addWidget(self.distance_line_edit, 0, 1)
        grid.addWidget(time_hours_label, 1, 0)
        grid.addWidget(self.time_hours_line_edit, 1, 1)
        grid.addWidget(calculate_button, 3, 0, 1, 2, )
        grid.addWidget(self.combo,  2, 0, 1, 2)
        grid.addWidget(self.output_label, 4, 0, 1, 2)

        self.setLayout(grid)

    def calculate_speed(self):
        distance = float(self.distance_line_edit.text())
        time = float(self.time_hours_line_edit.text())
        if self.combo == 'Meters(Km)':
            result = distance / time
            self.output_label.setText(f'Speed: {result} m/s')
        elif self.combo == 'Miles':
            result = distance / (time * 0.621371)
            self.output_label.setText(f'Speed: {result} mph')


app = QApplication(sys.argv)
speed_calculator = SpeedCalculator()
speed_calculator.show()
sys.exit(app.exec())