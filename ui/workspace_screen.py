from PyQt6.QtWidgets import (
    QWidget, QLabel, QVBoxLayout, QGroupBox, QHBoxLayout, QListWidget, QTextEdit
)

class WorkspaceScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        welcome = QLabel("👋 Welcome to your Workflow Workspace")
        welcome.setStyleSheet("font-size: 20px; font-weight: bold;")
        layout.addWidget(welcome)

        overview = QGroupBox("Recent Activity")
        overview_layout = QHBoxLayout()

        self.activity_list = QListWidget()
        self.activity_list.addItems([
            "✅ Agent 'FileReaderBot' completed job at 10:12 AM",
            "🔁 Tool 'GitFetcher' synced repository",
            "🧠 Chat session saved with 'LLM Assistant'",
        ])
        overview_layout.addWidget(self.activity_list)

        self.summary_box = QTextEdit()
        self.summary_box.setPlaceholderText("Daily notes, agent results, or status logs...")
        overview_layout.addWidget(self.summary_box)

        overview.setLayout(overview_layout)
        layout.addWidget(overview)

        self.setLayout(layout)
