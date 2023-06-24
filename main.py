import sys
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QCalendarWidget


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

        # Set the minimum and maximum dates to display only June 2020 and July 2020
        min_date = QDate(2020, 6, 1)
        max_date = QDate(2020, 7, 31)
        calendar.setMinimumDate(min_date)
        calendar.setMaximumDate(max_date)

        # Set the initial selected date to June 1, 2020
        calendar.setSelectedDate(min_date)

        layout.addWidget(calendar)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
