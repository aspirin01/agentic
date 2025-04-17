from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QListWidget, QStackedWidget, QLabel, QListWidgetItem
)
from PyQt6.QtCore import Qt
from ui.workspace_screen import WorkspaceScreen
from ui.tools_screen import ToolsScreen
from ui.agents_screen import AgentsScreen
from ui.record_screen import RecordScreen
from ui.new_chat_screen import NewChatScreen

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Agentic Workflow Manager")
        self.setMinimumSize(1200, 800)
        self.init_ui()

    def init_ui(self):
        main_widget = QWidget()
        main_layout = QHBoxLayout()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

        # Left navigation
        self.nav = QListWidget()
        self.nav.setFixedWidth(200)
        self.nav.setStyleSheet("""
                QListWidget {
                    background-color: #f9f9f9;
                    border: none;
                    padding: 12px;
                    font-size: 15px;
                }
                
                QListWidget::item {
                    background-color: transparent;
                    padding: 12px 16px;
                    margin: 4px 0;
                    border-radius: 8px;
                    border: none;
                    color: #333333;
                }

                QListWidget::item:hover {
                    background-color: #e6f0ff;
                }

                QListWidget::item:selected {
                    background-color: #d2e4ff;
                    padding-left: 12px;
                    font-weight: bold;
                    color: #1a1a1a;
                }
            """)        
        for name in ["Workspace", "Tools", "Agents", "Record", "New Chat"]:
            item = QListWidgetItem(name)
            self.nav.addItem(item)
            # fix the item style
        


        # Pages
        self.pages = QStackedWidget()
        self.page_widgets = {
            "Workspace": WorkspaceScreen(),
            "Tools": ToolsScreen(),
            "Agents": AgentsScreen(),
            "Record": RecordScreen(),
            "New Chat": NewChatScreen(),
        }
        for screen in self.page_widgets.values():
            self.pages.addWidget(screen)

        self.nav.currentRowChanged.connect(self.pages.setCurrentIndex)
        self.nav.setCurrentRow(0)

        self.setStyleSheet("""
            QWidget {
                background-color: #f9f9f9;
                color: #2c2c2c;
                font-family: 'Segoe UI', sans-serif;
                font-size: 14px;
            }

            QLabel {
                font-size: 16px;
                font-weight: 500;
            }

            QPushButton {
                background-color: #ffffff;
                border: 1px solid #d0d0d0;
                padding: 8px 12px;
                border-radius: 6px;
            }

            QPushButton:hover {
                background-color: #f0f0f0;
            }

            QGroupBox {
                border: 1px solid #ccc;
                border-radius: 8px;
                margin-top: 10px;
                padding: 10px;
            }

            QGroupBox:title {
                subcontrol-origin: margin;
                subcontrol-position: top left;
                padding: 0 3px;
            }

            QListWidget, QTextEdit, QLineEdit {
                background-color: #fff;
                border: 1px solid #ddd;
                border-radius: 6px;
                padding: 6px;
            }

            QVBoxLayout, QHBoxLayout {
                margin: 12px;
            }
        """)


        main_layout.addWidget(self.nav)
        main_layout.addWidget(self.pages)
     
    def create_sidebar(self):
        sidebar = QFrame()
        sidebar.setFixedWidth(200)
        sidebar.setStyleSheet("background-color: #ffffff; border-right: 1px solid #dddddd;")

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        layout.setSpacing(8)

        title = QLabel("⚡ Agentic")
        title.setStyleSheet("font-size: 18px; font-weight: bold; padding: 16px;")
        layout.addWidget(title)

        self.buttons = []

        btn_names = [
            ("Workspace", self.show_workspace),
            ("Tools", self.show_tools),
            ("Agents", self.show_agents),
            ("Record", self.show_record),
            ("New Chat", self.show_chat),
        ]

        for idx, (label, handler) in enumerate(btn_names):
            btn = SidebarButton(label)
            btn.clicked.connect(lambda checked, i=idx, h=handler: self.switch_screen(i, h))
            layout.addWidget(btn)
            self.buttons.append(btn)

        self.buttons[0].setChecked(True)

        sidebar.setLayout(layout)
        return sidebar

    def switch_screen(self, index, handler):
        for i, b in enumerate(self.buttons):
            b.setChecked(i == index)
        self.stack.setCurrentIndex(index)
        handler()