# This Python file uses the following encoding: utf-8

import sys



from PySide6.QtWidgets import QApplication, QMainWindow



# Important:

# You need to run the following command to generate the ui_form.py file

#     pyside6-uic form.ui -o ui_form.py, or

#     pyside2-uic form.ui -o ui_form.py

from ui_form import Ui_MainWindow



class MainWindow(QMainWindow):

    def __init__(self, parent=None):

        super().__init__(parent)

        self.ui = Ui_MainWindow()

        self.ui.setupUi(self)

        # Calculate Decrement Factor according to IEEE Std 80
        self.setup_toggle_behavior(
            self.ui.comboBox_16,
            show_on_yes = [
                self.ui.label_74, self.ui.label_75, self.ui.lineEdit_45, self.ui.toolButton_60,
                self.ui.label_76, self.ui.label_77, self.ui.lineEdit_46, self.ui.toolButton_61
            ],
            show_on_no = [
                self.ui.label_78, self.ui.label_79, self.ui.lineEdit_38, self.ui.toolButton_62,
            ]
        )

        # Calculate Soil Resistivity through Ground Resistance
        self.setup_toggle_behavior(
            self.ui.comboBox_7,
            show_on_yes = [
                self.ui.label_48, self.ui.label_49, self.ui.lineEdit_22, self.ui.toolButton_48
            ],
            show_on_no = [
                self.ui.label_51, self.ui.label_52, self.ui.lineEdit_23, self.ui.toolButton_49
            ]
        )

        # Calculate Maximum Grid Current according to IEEE Std 80
        self.setup_toggle_behavior(
            self.ui.comboBox_6,
            show_on_yes = [
                self.ui.label_41, self.ui.label_42, self.ui.lineEdit_20, self.ui.toolButton_44,
                self.ui.label_43, self.ui.label_44, self.ui.lineEdit_21, self.ui.toolButton_45
            ],
            show_on_no = [
                self.ui.label_45, self.ui.label_46, self.ui.lineEdit_28, self.ui.toolButton_46
            ]
        )
        
        # Safety Standard
        self.setup_toggle_behavior(
            self.ui.comboBox_8,
            show_on_yes = [
                self.ui.label_54, self.ui.label_55, self.ui.lineEdit_13, self.ui.toolButton_51,
                self.ui.label_56, self.ui.label_57, self.ui.lineEdit_14, self.ui.toolButton_52
            ],
            show_on_no = [
                self.ui.label_58, self.ui.label_59, self.ui.lineEdit_24, self.ui.toolButton_53,
                self.ui.label_63, self.ui.label_64, self.ui.lineEdit_25, self.ui.toolButton_54,
                self.ui.label_65, self.ui.label_66, self.ui.lineEdit_26, self.ui.toolButton_55,
                self.ui.label_67, self.ui.label_68, self.ui.lineEdit_29, self.ui.toolButton_56,
                self.ui.label_69, self.ui.label_70, self.ui.lineEdit_30, self.ui.toolButton_57,
                self.ui.label_71, self.ui.label_72, self.ui.lineEdit_31, self.ui.toolButton_58
            ]
        )

        self.ui.comboBox_9.currentTextChanged.connect(self.update_safety_standard_options)

    def setenabled_combo_item(self, combo_box, index, enabled):
        """ Function that enables or disables an item of a combo box

        Arguments:
            combo_box (QComboBox): ComboBox to be advised for toggle on or off widgets
            index (int): The index of the target item of the combo box
            enabled (boolean): True to enable item and False to disable item
        """
        model = combo_box.model()
        item = model.item(index)
        if item:
            item.setEnabled(enabled)

    def update_safety_standard_options(self, system_type):
        """ Function that updates safety standard combo box based on the selected system type, TN or TT

        Arguments:
            system_type (string): System Type of MV/LV Substation (TN or TT)
        """
        if system_type == "TT":
            self.setenabled_combo_item(self.ui.comboBox_8, 0, False)
            self.setenabled_combo_item(self.ui.comboBox_8, 1, True)
            self.ui.comboBox_8.setCurrentIndex(1)
        elif system_type == "TN":
            self.setenabled_combo_item(self.ui.comboBox_8, 0, True)
            self.setenabled_combo_item(self.ui.comboBox_8, 1, True)

    def setup_toggle_behavior(self, combo_box, show_on_yes=None, show_on_no=None):
        """ Function that shows or hides widgets based on the option of a comboBox

        Arguments:
            combo_box (QComboBox): ComboBox to be advised for toggle on or off widgets
            show_on_yes (1d array): List of the widgets to show on yes
            show_on_no (1d array): List of the widgets to show on no
        """
        show_on_yes = show_on_yes or []
        show_on_no = show_on_no or []

        def toggle_widgets():
            if combo_box.currentIndex() == 1:
                for widget in show_on_no:
                    widget.show()
                for widget in show_on_yes:
                    widget.hide()
            else:
                for widget in show_on_yes:
                    widget.show()
                for widget in show_on_no:
                    widget.hide()

        combo_box.currentIndexChanged.connect(toggle_widgets)
        toggle_widgets()  # Apply at startup





if __name__ == "__main__":

    app = QApplication(sys.argv)

    widget = MainWindow()

    widget.show()

    sys.exit(app.exec())

