import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

class MainApplication(QWidget):
    def __init__(self):
        super().__init__()

        # Create widgets
        self.input_label = QLabel('Enter your name:', self)
        self.input_field = QLineEdit(self)
        self.output_label = QLabel('Output:', self)
        self.output_field = QLabel(self)
        self.submit_button = QPushButton('Submit', self)
        self.submit_button.clicked.connect(self.on_submit)

        # Set layout
        layout = QVBoxLayout(self)
        layout.addWidget(self.input_label)
        layout.addWidget(self.input_field)
        layout.addWidget(self.output_label)
        layout.addWidget(self.output_field)
        layout.addWidget(self.submit_button)

        # Set window properties
        self.setWindowTitle('Input/Output App')
        self.setGeometry(100, 100, 400, 300)

    def on_submit(self):
        # Get input text and set output text
        input_text = self.input_field.text()
        self.output_field.setText(input_text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_app = MainApplication()
    my_app.show()
    sys.exit(app.exec())
