# from PySide6.QtCore import Qt
# from ui_Sidebar_App import Ui_MainWindow
# from PySide6.QtWidgets import QApplication, QMainWindow,QPushButton, QWidget

# class MySideBar(QMainWindow,Ui_MainWindow):
#     def __init__(self, parent: QWidget | None = ..., flags: Qt.WindowType = ...) -> None:
#         super().__init__(self)
#         super().__init__()
#         self.setupUi(self)
#         self.setWindowTitle("SideBar Menu")

#         self.Icon_Name_Widget.setHidden(True)



#         self.Dashboard_B.connect(self.switch_to_Dashboard_Page)
#         self.Dashboard_S.connect(self.switch_to_Dashboard_Page)

#         self.Profile_B.connect(self.switch_to_Profile_Page)
#         self.Profile_S.connect(self.switch_to_Profile_Page)

#         self.Messages_B.connect(self.switch_to_Messages_Page)
#         self.Messages_S.connect(self.switch_to_Messages_Page)

#         self.Notifications_B.connect(self.switch_to_Notifications_Page)
#         self.Notifications_S.connect(self.switch_to_Notifications_Page)

#         self.Settings_B.connect(self.switch_to_Settings_Page)
#         self.Settings_S.connect(self.switch_to_Settings_Page)





#     def switch_to_Dashboard_Page(self):
#         self.stackedWidget.setCurrentIndex(0)

#     def switch_to_Profile_Page(self):
#         self.stackedWidget.setCurrentIndex(0)

#     def switch_to_Messages_Page(self):
#         self.stackedWidget.setCurrentIndex(0)

#     def switch_to_Notifications_Page(self):
#         self.stackedWidget.setCurrentIndex(0)

#     def switch_to_Settings_Page(self):
#         self.stackedWidget.setCurrentIndex(0)

from PySide6.QtCore import Qt
from ui_Sidebar_App import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget

class MySideBar(QMainWindow, Ui_MainWindow):
    def __init__(self, parent: QWidget | None = None, flags: Qt.WindowType = Qt.WindowFlags()) -> None:
        super().__init__(parent, flags)
        self.setupUi(self)
        self.setWindowTitle("SideBar Menu")

        self.Icon_Name_Widget.setHidden(True)

        self.Dashboard_B.clicked.connect(self.switch_to_Dashboard_Page)
        self.Dashboard_S.clicked.connect(self.switch_to_Dashboard_Page)

        self.Profile_B.clicked.connect(self.switch_to_Profile_Page)
        self.Profile_S.clicked.connect(self.switch_to_Profile_Page)

        self.Messages_B.clicked.connect(self.switch_to_Messages_Page)
        self.Messages_S.clicked.connect(self.switch_to_Messages_Page)

        self.Notifications_B.clicked.connect(self.switch_to_Notifications_Page)
        self.Notifications_S.clicked.connect(self.switch_to_Notifications_Page)

        self.Settings_B.clicked.connect(self.switch_to_Settings_Page)
        self.Settings_S.clicked.connect(self.switch_to_Settings_Page)

    def switch_to_Dashboard_Page(self):
        self.stackedWidget.setCurrentIndex(0)

    def switch_to_Profile_Page(self):
        self.stackedWidget.setCurrentIndex(1)

    def switch_to_Messages_Page(self):
        self.stackedWidget.setCurrentIndex(2)

    def switch_to_Notifications_Page(self):
        self.stackedWidget.setCurrentIndex(3)

    def switch_to_Settings_Page(self):
        self.stackedWidget.setCurrentIndex(4)
