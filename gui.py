import os

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
    QHBoxLayout, QSizePolicy,
    QMessageBox
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
        self._file_label = QLabel("Select Subtitle File:")
        self._file_input = QLineEdit()
        self._file_input.setReadOnly(True)
        self._file_input.setStyleSheet("background-color: #f0f0f0;")
        self._file_input.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self._file_browse_button = QPushButton("Browse")
        self._file_browse_button.clicked.connect(self.on_file_browse_button_clicked)
        file_layout.addWidget(self._file_label)
        file_layout.addWidget(self._file_input)
        file_layout.addWidget(self._file_browse_button)
        main_layout.addLayout(file_layout)

        # Target directory
        dir_layout = QHBoxLayout()
        self._dir_label = QLabel("Select Target Directory:")
        self._dir_input = QLineEdit()
        self._dir_input.setReadOnly(True)
        self._dir_input.setStyleSheet("background-color: #f0f0f0;")

        self._dir_browse_button = QPushButton("Browse")
        self._dir_browse_button.clicked.connect(self.on_dir_browse_button_clicked)
        dir_layout.addWidget(self._dir_label)
        dir_layout.addWidget(self._dir_input)
        dir_layout.addWidget(self._dir_browse_button)
        main_layout.addLayout(dir_layout)

        # Language selection
        self._source_lang = ""
        self._target_lang = ""


        lang_layout = QHBoxLayout()
        self._source_label = QLabel("Source Language:")
        self._source_dropdown = QComboBox()
        self._source_dropdown.addItems(["(empty)", "English", "Serbian"])
        # Connecting dropdown signal
        self._source_dropdown.currentIndexChanged.connect(self.on_source_language_changed)

        self._target_label = QLabel("Target Language:")
        self._target_dropdown = QComboBox()
        self._target_dropdown.addItems(["(empty)", "English", "Српски"])
        # Connecting dropdown signal
        self._target_dropdown.currentIndexChanged.connect(self.on_target_language_changed)

        lang_layout.addWidget(self._source_label)
        lang_layout.addWidget(self._source_dropdown)
        lang_layout.addWidget(self._target_label)
        lang_layout.addWidget(self._target_dropdown)
        main_layout.addLayout(lang_layout)

        # Translate button
        self._translate_button = QPushButton("Translate")
        self._translate_button.clicked.connect(self.on_translate_button_clicked)
        main_layout.addWidget(self._translate_button)


    def on_file_browse_button_clicked(self):
        default_path = os.path.join(os.path.expanduser("~"), "Documents")
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Subtitle File", default_path)
        if file_path:
            self._file_input.setText(file_path)

    def on_dir_browse_button_clicked(self):
        default_path = os.path.join(os.path.expanduser("~"), "Documents")
        dir_path = QFileDialog.getExistingDirectory(self, "Select Directory", default_path)
        if dir_path:
            self._dir_input.setText(dir_path)

    def on_source_language_changed(self):
        self._source_lang = self._source_dropdown.currentText()

    def on_target_language_changed(self):
        self._target_lang = self._target_dropdown.currentText()

    def on_translate_button_clicked(self):
        file_input = self._file_input.text()
        dir_input = self._dir_input.text()
        source_lang = self._source_lang
        target_lang = self._target_lang

        if not (file_input and dir_input):
            self.show_message_box("You have to choose both file and directory.", title="Missing Input", message_type="warning")
        elif source_lang == "" or target_lang == "":
            self.show_message_box("You have to set both source and target language.", title="Missing Language", message_type="warning")
        elif source_lang == "(empty)" or target_lang == "(empty)":
            self.show_message_box("Source and target languages cannot be (empty).", title="Invalid Language", message_type="warning")
        else:
            self.show_message_box(
                f"File: {file_input}\nDir: {dir_input}\nSource lang: {source_lang}\nTarget lang: {target_lang}",
                title="Translation Info", message_type="information")

    def show_message_box(self, message, title="Message", message_type="information"):
        msg_box = QMessageBox(self)

        if message_type == "information":
            msg_box.setIcon(QMessageBox.Information)
        elif message_type == "warning":
            msg_box.setIcon(QMessageBox.Warning)
        elif message_type == "critical":
            msg_box.setIcon(QMessageBox.Critical)
        else:
            msg_box.setIcon(QMessageBox.NoIcon)

        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.exec_()

    @staticmethod
    def run():
        import sys
        app = QApplication(sys.argv)
        window = SubtitleTranslatorGUI()
        window.show()
        sys.exit(app.exec_())