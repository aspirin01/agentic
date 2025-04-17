from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QPushButton, QListWidget, QHBoxLayout, QLineEdit, QMessageBox
)

class ToolsScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.installed_tools = ["File System", "Git Manager"]
        self.available_tools = {
            "File System": "Provides file operations like read/edit/info",
            "Git Manager": "Clones and manages Git repositories",
            "CSV Analyzer": "Reads and analyzes CSV datasets"
        }
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        layout.addWidget(QLabel("🧰 Installed Tools"))
        self.tools_list = QListWidget()
        self.tools_list.addItems(self.installed_tools)
        layout.addWidget(self.tools_list)

        # Marketplace section
        layout.addWidget(QLabel("🛒 Tool Marketplace"))

        self.marketplace_list = QListWidget()
        for name, desc in self.available_tools.items():
            self.marketplace_list.addItem(f"{name} - {desc}")
        layout.addWidget(self.marketplace_list)

        param_layout = QHBoxLayout()
        self.param_input = QLineEdit()
        self.param_input.setPlaceholderText("Enter dynamic param (e.g. Git repo URL)")
        self.install_button = QPushButton("Install Selected Tool")
        self.install_button.clicked.connect(self.install_tool)
        param_layout.addWidget(self.param_input)
        param_layout.addWidget(self.install_button)

        layout.addLayout(param_layout)
        self.setLayout(layout)

    def install_tool(self):
        selected = self.marketplace_list.currentItem()
        param = self.param_input.text()
        if selected and param:
            tool_name = selected.text().split(" - ")[0]
            if tool_name not in self.installed_tools:
                self.installed_tools.append(tool_name)
                self.tools_list.addItem(tool_name)
                QMessageBox.information(self, "Success", f"Tool '{tool_name}' installed with param '{param}'")
        else:
            QMessageBox.warning(self, "Warning", "Select tool and enter dynamic parameter.")
