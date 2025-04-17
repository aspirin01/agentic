from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QListWidget, QPushButton, QTextEdit

class RecordScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        layout.addWidget(QLabel("📜 Records of Previous Chats & Workflows"))

        self.record_list = QListWidget()
        self.record_list.addItems([
            "Chat with SummarizerBot - 12 Apr 2025",
            "GitSync Operation - 10 Apr 2025",
            "Workflow: 'Generate Report' - 9 Apr 2025"
        ])
        layout.addWidget(self.record_list)

        self.record_preview = QTextEdit()
        self.record_preview.setReadOnly(True)
        self.record_preview.setPlaceholderText("Select a record to view its contents...")
        layout.addWidget(self.record_preview)

        self.record_list.itemClicked.connect(self.load_record)

        self.setLayout(layout)

    def load_record(self, item):
        self.record_preview.setPlainText(f"Preview of: {item.text()}\n\n[Dummy content here]")
