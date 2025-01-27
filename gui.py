from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QLineEdit,
    QPushButton,
    QComboBox,
    QFileDialog,
    QVBoxLayout,
    QWidget,
    QHBoxLayout
)

class SubtitleTranslatorGUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Subtitle Translator")
        self.setGeometry(100, 100, 600, 250)

        # Main widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Layouts
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        # File selection
        file_layout = QHBoxLayout()
        self.file_label = QLabel("Select Subtitle File:")
        self.file_input = QLineEdit()
        self.file_browse_button = QPushButton("Browse")
        file_layout.addWidget(self.file_label)
        file_layout.addWidget(self.file_input)
        file_layout.addWidget(self.file_browse_button)
        main_layout.addLayout(file_layout)

        # Target directory
        dir_layout = QHBoxLayout()
        self.dir_label = QLabel("Select Target Directory:")
        self.dir_input = QLineEdit()
        self.dir_browse_button = QPushButton("Browse")
        dir_layout.addWidget(self.dir_label)
        dir_layout.addWidget(self.dir_input)
        dir_layout.addWidget(self.dir_browse_button)
        main_layout.addLayout(dir_layout)

        # Language selection
        lang_layout = QHBoxLayout()
        self.source_label = QLabel("Source Language:")
        self.source_dropdown = QComboBox()
        self.source_dropdown.addItems(["English", "Serbian", "German", "Hungarian"])
        self.target_label = QLabel("Target Language:")
        self.target_dropdown = QComboBox()
        self.target_dropdown.addItems(["English", "Српски", "Deutch", "Magyar"])
        lang_layout.addWidget(self.source_label)
        lang_layout.addWidget(self.source_dropdown)
        lang_layout.addWidget(self.target_label)
        lang_layout.addWidget(self.target_dropdown)
        main_layout.addLayout(lang_layout)

        # Translate button
        self.translate_button = QPushButton("Translate")
        main_layout.addWidget(self.translate_button)

    @staticmethod
    def run():
        import sys
        app = QApplication(sys.argv)
        window = SubtitleTranslatorGUI()
        window.show()
        sys.exit(app.exec_())