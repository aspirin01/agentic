from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QTextEdit, QPushButton, QHBoxLayout, QListWidget, QLabel
)

class NewChatScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        layout.addWidget(QLabel("💬 New Chat with AI Agent"))

        self.chat_history = QListWidget()
        layout.addWidget(self.chat_history)

        input_layout = QHBoxLayout()
        self.input_box = QTextEdit()
        self.input_box.setPlaceholderText("Type your prompt...")
        self.send_button = QPushButton("Send")
        self.send_button.clicked.connect(self.send_message)

        input_layout.addWidget(self.input_box)
        input_layout.addWidget(self.send_button)

        layout.addLayout(input_layout)
        self.setLayout(layout)

    def send_message(self):
        message = self.input_box.toPlainText().strip()
        if message:
            self.chat_history.addItem(f"👤: {message}")
            self.chat_history.addItem(f"🤖: [Dummy AI response to: '{message}']")
            self.input_box.clear()
