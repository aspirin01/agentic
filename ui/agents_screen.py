from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QPushButton, QListWidget, QLineEdit, QHBoxLayout, QMessageBox
)

class AgentsScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.installed_agents = ["SummarizerBot", "CodeRefactorBot"]
        self.available_agents = {
            "SummarizerBot": "Summarizes large documents or transcripts",
            "CodeRefactorBot": "Refactors and improves your Python code",
            "DataExtractorBot": "Extracts structured data from unstructured text"
        }
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        layout.addWidget(QLabel("🤖 Installed Agents"))
        self.agent_list = QListWidget()
        self.agent_list.addItems(self.installed_agents)
        layout.addWidget(self.agent_list)

        layout.addWidget(QLabel("🛒 Agent Marketplace"))

        self.marketplace_list = QListWidget()
        for name, desc in self.available_agents.items():
            self.marketplace_list.addItem(f"{name} - {desc}")
        layout.addWidget(self.marketplace_list)

        input_layout = QHBoxLayout()
        self.param_input = QLineEdit()
        self.param_input.setPlaceholderText("Enter agent-specific config param")
        self.install_button = QPushButton("Install Selected Agent")
        self.install_button.clicked.connect(self.install_agent)
        input_layout.addWidget(self.param_input)
        input_layout.addWidget(self.install_button)

        layout.addLayout(input_layout)
        self.setLayout(layout)

    def install_agent(self):
        selected = self.marketplace_list.currentItem()
        param = self.param_input.text()
        if selected and param:
            agent_name = selected.text().split(" - ")[0]
            if agent_name not in self.installed_agents:
                self.installed_agents.append(agent_name)
                self.agent_list.addItem(agent_name)
                QMessageBox.information(self, "Success", f"Agent '{agent_name}' installed with param '{param}'")
        else:
            QMessageBox.warning(self, "Warning", "Select agent and enter configuration.")
