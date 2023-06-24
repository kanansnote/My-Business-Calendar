import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QCalendarWidget, QLabel, QLineEdit


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Business Calendar")

        # Create a central widget and set it as the main window's central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Create a vertical layout for the central widget
        layout = QVBoxLayout(central_widget)

        # Create a calendar widget and add it to the layout
        calendar = QCalendarWidget()
        calendar.setGridVisible(True)
        calendar.setMinimumDate(calendar.minimumDate().addMonths(-1))  # Show previous month
        calendar.setMaximumDate(calendar.maximumDate().addMonths(1))  # Show next month
        layout.addWidget(calendar)

        # Create fill-in-the-blank entries for June 2020 and July 2020
        entries_label = QLabel("Fill-in-the-blank Entries:")
        layout.addWidget(entries_label)

        june_label = QLabel("June 2020:")
        layout.addWidget(june_label)
        june_entry = QLineEdit()
        layout.addWidget(june_entry)

        july_label = QLabel("July 2020:")
        layout.addWidget(july_label)
        july_entry = QLineEdit()
        layout.addWidget(july_entry)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
