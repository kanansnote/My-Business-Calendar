import sys
from PyQt5.QtCore import QDate, Qt
from PyQt5.QtGui import QPixmap, QPalette
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QCalendarWidget, QDesktopWidget, QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Business Calendar")

        # Create a central widget and set it as the main window's central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Create a vertical layout for the central widget
        layout = QVBoxLayout(central_widget)

        # Create a QLabel for June image and add it to the layout
        self.june_image_label = QLabel()
        june_pixmap = QPixmap("media/for_june_image.jpg").scaledToWidth(800)
        self.june_image_label.setPixmap(june_pixmap)
        self.june_image_label.setAlignment(Qt.AlignHCenter)

        # Create a QLabel for July image and add it to the layout
        self.july_image_label = QLabel()
        july_pixmap = QPixmap("media/for_july_image.jpg").scaledToWidth(800)
        self.july_image_label.setPixmap(july_pixmap)
        self.july_image_label.setAlignment(Qt.AlignHCenter)
        self.july_image_label.hide()  # Initially hide the July image

        # Create a nested vertical layout for the images and calendar
        nested_layout = QVBoxLayout()

        nested_layout.addWidget(self.june_image_label)
        nested_layout.addWidget(self.july_image_label)

        # Create a calendar widget and add it to the nested layout
        self.calendar = QCalendarWidget()
        self.calendar.setGridVisible(True)

        # Set the minimum and maximum dates to display only June 2020 and July 2020
        min_date = QDate(2020, 6, 1)
        max_date = QDate(2020, 7, 31)
        self.calendar.setMinimumDate(min_date)
        self.calendar.setMaximumDate(max_date)

        # Set the initial selected date to June 1, 2020
        self.calendar.setSelectedDate(min_date)

        nested_layout.addWidget(self.calendar)

        # Add the nested layout to the main layout
        layout.addLayout(nested_layout)

        # Set the layout margins and spacing
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        # Connect the calendar's selectionChanged signal to a custom slot to handle image updates
        self.calendar.selectionChanged.connect(self.update_displayed_image)

        # Connect the calendar's currentPageChanged signal to a custom slot
        self.calendar.currentPageChanged.connect(self.handle_month_change)

        # Get the screen's geometry and calculate the center position
        screen_geometry = QDesktopWidget().screenGeometry()
        center_point = screen_geometry.center()

        # Set the desired size of the main window
        window_width = 800
        window_height = 600
        self.resize(window_width, window_height)

        # Move the main window to the center position
        self.move(center_point.x() - window_width // 2, center_point.y() - window_height // 2)

    def update_displayed_image(self):
        selected_date = self.calendar.selectedDate()
        if selected_date.month() == 7:
            self.june_image_label.hide()
            self.july_image_label.show()
        else:
            self.july_image_label.hide()
            self.june_image_label.show()

    def handle_month_change(self):
        current_month = self.calendar.monthShown()
        current_year = self.calendar.yearShown()
        if current_month == 7:  # July
            first_day_july = QDate(current_year, 7, 1)
            self.calendar.setSelectedDate(first_day_july)
        else:
            first_day_june = QDate(current_year, 6, 1)
            self.calendar.setSelectedDate(first_day_june)

        pal = self.calendar.palette()
        pal.setColor(QPalette.WindowText, pal.color(QPalette.Window))
        self.calendar.setPalette(pal)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
