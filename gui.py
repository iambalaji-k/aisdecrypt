import sys
import os
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
    QLabel, QLineEdit, QPushButton, QFileDialog, QMessageBox
)
from PyQt6.QtCore import Qt
from AIS_Decryptor import decrypt_ais

class AISDecryptorGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("AIS JSON Decryptor")
        self.setFixedWidth(500)

        # Central widget and main layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        layout.setSpacing(15)
        layout.setContentsMargins(20, 20, 20, 20)

        # Title
        title_label = QLabel("AIS JSON Decryptor")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setStyleSheet("font-size: 20px; font-weight: bold; margin-bottom: 10px;")
        layout.addWidget(title_label)

        # PAN Input
        pan_layout = QHBoxLayout()
        pan_label = QLabel("PAN:")
        pan_label.setFixedWidth(80)
        self.pan_input = QLineEdit()
        self.pan_input.setPlaceholderText("Enter your PAN (e.g., ABCDE1234F)")
        pan_layout.addWidget(pan_label)
        pan_layout.addWidget(self.pan_input)
        layout.addLayout(pan_layout)

        # DOB Input
        dob_layout = QHBoxLayout()
        dob_label = QLabel("DOB:")
        dob_label.setFixedWidth(80)
        self.dob_input = QLineEdit()
        self.dob_input.setPlaceholderText("DDMMYYYY (e.g., 01011990)")
        dob_layout.addWidget(dob_label)
        dob_layout.addWidget(self.dob_input)
        layout.addLayout(dob_layout)

        # Input File Selection
        file_layout = QHBoxLayout()
        file_label = QLabel("Encrypted File:")
        file_label.setFixedWidth(80)
        self.file_input = QLineEdit()
        self.file_input.setReadOnly(True)
        browse_btn = QPushButton("Browse")
        browse_btn.clicked.connect(self.browse_input_file)
        file_layout.addWidget(file_label)
        file_layout.addWidget(self.file_input)
        file_layout.addWidget(browse_btn)
        layout.addLayout(file_layout)

        # Output File Selection
        output_layout = QHBoxLayout()
        output_label = QLabel("Output File:")
        output_label.setFixedWidth(80)
        self.output_input = QLineEdit()
        self.output_input.setText("decrypted.json")
        output_btn = QPushButton("Save As")
        output_btn.clicked.connect(self.browse_output_file)
        output_layout.addWidget(output_label)
        output_layout.addWidget(self.output_input)
        output_layout.addWidget(output_btn)
        layout.addLayout(output_layout)

        # Decrypt Button
        self.decrypt_btn = QPushButton("Decrypt File")
        self.decrypt_btn.setStyleSheet("""
            QPushButton {
                background-color: #0078d4;
                color: white;
                font-size: 16px;
                font-weight: bold;
                padding: 10px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #106ebe;
            }
        """)
        self.decrypt_btn.clicked.connect(self.handle_decryption)
        layout.addWidget(self.decrypt_btn)

        # Status Label
        self.status_label = QLabel("Ready")
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.status_label)

    def browse_input_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Encrypted File", "", "All Files (*)")
        if file_path:
            self.file_input.setText(file_path)

    def browse_output_file(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Save Decrypted File", "decrypted.json", "JSON Files (*.json)")
        if file_path:
            self.output_input.setText(file_path)

    def handle_decryption(self):
        pan = self.pan_input.text().strip().lower()
        dob = self.dob_input.text().strip()
        file_path = self.file_input.text().strip()
        output_file = self.output_input.text().strip()

        if not pan or not dob or not file_path or not output_file:
            QMessageBox.warning(self, "Input Error", "Please fill in all fields.")
            return

        if not os.path.exists(file_path):
            QMessageBox.critical(self, "File Error", "Encrypted file not found.")
            return

        self.status_label.setText("Decrypting...")
        self.decrypt_btn.setEnabled(False)
        QApplication.processEvents()

        success, message = decrypt_ais(pan, dob, file_path, output_file)

        self.decrypt_btn.setEnabled(True)
        if success:
            self.status_label.setText("Success!")
            QMessageBox.information(self, "Success", message)
        else:
            self.status_label.setText("Failed")
            QMessageBox.critical(self, "Decryption Failed", f"Error: {message}\n\nPlease check your PAN, DOB, and file.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AISDecryptorGUI()
    window.show()
    sys.exit(app.exec())
