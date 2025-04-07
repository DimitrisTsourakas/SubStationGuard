# This Python file uses the following encoding: utf-8

import sys



from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QEvent


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

        self.ui.label_60.setVisible(False)
        self.ui.label_61.setVisible(False)
        self.ui.label_62.setVisible(False)
        self.ui.label_87.setVisible(False)
        self.ui.label_88.setVisible(False)
        self.ui.label_89.setVisible(False)
        self.ui.label_90.setVisible(False)
        self.ui.label_91.setVisible(False)
        self.ui.label_92.setVisible(False)
        self.ui.label_93.setVisible(False)
        self.ui.label_94.setVisible(False)
        self.ui.label_95.setVisible(False)
        self.ui.label_96.setVisible(False)
        self.ui.label_97.setVisible(False)
        self.ui.label_98.setVisible(False)
        self.ui.label_99.setVisible(False)
        self.ui.label_100.setVisible(False)
        self.ui.label_101.setVisible(False)
        self.ui.label_102.setVisible(False)

        self.ui.comboBox_16.installEventFilter(self)

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
                self.ui.label_43, self.ui.label_44, self.ui.lineEdit_21, self.ui.toolButton_45,
                self.ui.label_73, self.ui.comboBox_16, self.ui.toolButton_59
            ],
            show_on_no = [
                self.ui.label_45, self.ui.label_46, self.ui.lineEdit_28, self.ui.toolButton_46
            ]
        )

        # Calculate Decrement Factor according to IEEE Std 80
        self.setup_toggle_behavior(
            self.ui.comboBox_16,
            show_on_yes = [
                self.ui.label_74, self.ui.label_75, self.ui.lineEdit_45, self.ui.toolButton_60,
                self.ui.label_76, self.ui.label_77, self.ui.lineEdit_46, self.ui.toolButton_61
            ],
            show_on_no = [
                self.ui.label_78, self.ui.label_79, self.ui.lineEdit_38, self.ui.toolButton_62
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

        self.setup_live_validation(
            line_edit=self.ui.lineEdit_32,
            error_label=self.ui.label_102,
            validator_func=self.is_valid_number,
            error_message="Enter a valid number"
        )

        self.setup_live_validation(
            line_edit=self.ui.lineEdit_33,
            error_label=self.ui.label_101,
            validator_func=self.is_valid_number,
            error_message="Enter a valid fuction"
        )

        self.setup_live_validation(
            line_edit=self.ui.lineEdit_34,
            error_label=self.ui.label_100,
            validator_func=self.is_valid_number,
            error_message="Enter a valid number"
        )

        self.setup_live_validation(
            line_edit=self.ui.lineEdit_22,
            error_label=self.ui.label_61,
            validator_func=self.is_valid_number,
            error_message="Enter a valid number"
        )

        self.setup_live_validation(
            line_edit=self.ui.lineEdit_23,
            error_label=self.ui.label_60,
            validator_func=self.is_valid_number,
            error_message="Enter a valid number"
        )

        self.setup_live_validation(
            line_edit=self.ui.lineEdit_20,
            error_label=self.ui.label_97,
            validator_func=self.is_valid_number,
            error_message="Enter a valid number"
        )

        self.setup_live_validation(
            line_edit=self.ui.lineEdit_21,
            error_label=self.ui.label_98,
            validator_func=self.is_valid_number,
            error_message="Enter a valid number"
        )

        self.setup_live_validation(
            line_edit=self.ui.lineEdit_28,
            error_label=self.ui.label_99,
            validator_func=self.is_valid_number,
            error_message="Enter a valid number"
        )

        self.setup_live_validation(
            line_edit=self.ui.lineEdit_45,
            error_label=self.ui.label_88,
            validator_func=self.is_valid_number,
            error_message="Enter a valid number"
        )

        self.setup_live_validation(
            line_edit=self.ui.lineEdit_46,
            error_label=self.ui.label_87,
            validator_func=self.is_valid_number,
            error_message="Enter a valid number"
        )

        self.setup_live_validation(
            line_edit=self.ui.lineEdit_38,
            error_label=self.ui.label_62,
            validator_func=self.is_valid_number,
            error_message="Enter a valid number"
        )

        self.setup_live_validation(
            line_edit=self.ui.lineEdit_13,
            error_label=self.ui.label_96,
            validator_func=self.is_valid_number,
            error_message="Enter a valid number"
        )

        self.setup_live_validation(
            line_edit=self.ui.lineEdit_14,
            error_label=self.ui.label_95,
            validator_func=self.is_valid_number,
            error_message="Enter a valid number"
        )

        self.setup_live_validation(
            line_edit=self.ui.lineEdit_24,
            error_label=self.ui.label_94,
            validator_func=self.is_valid_number,
            error_message="Enter a valid number"
        )

        self.setup_live_validation(
            line_edit=self.ui.lineEdit_25,
            error_label=self.ui.label_93,
            validator_func=self.is_valid_number,
            error_message="Enter a valid number"
        )

        self.setup_live_validation(
            line_edit=self.ui.lineEdit_26,
            error_label=self.ui.label_92,
            validator_func=self.is_valid_number,
            error_message="Enter a valid number"
        )

        self.setup_live_validation(
            line_edit=self.ui.lineEdit_29,
            error_label=self.ui.label_91,
            validator_func=self.is_valid_number,
            error_message="Enter a valid number"
        )

        self.setup_live_validation(
            line_edit=self.ui.lineEdit_30,
            error_label=self.ui.label_90,
            validator_func=self.is_valid_number,
            error_message="Enter a valid number"
        )

        self.setup_live_validation(
            line_edit=self.ui.lineEdit_31,
            error_label=self.ui.label_89,
            validator_func=self.is_valid_number,
            error_message="Enter a valid number"
        )

    
    def eventFilter(self, watched, event):
        """ Function that intercepts show and hide events in order to run a custom functionality.
        The current fuction will trigger on_combo_show and on_combo_hide functions for combo box
        comboBox_16

        Arguments:
            combo_box (QComboBox): ComboBox to be used to create the fake signal
        """
        if watched == self.ui.comboBox_16:
            if event.type() == QEvent.Show:
                self.on_combo_shown(self.ui.comboBox_16)
            elif event.type() == QEvent.Hide:
                widgets = [
                    self.ui.label_74, self.ui.label_75, self.ui.lineEdit_45, self.ui.toolButton_60,
                    self.ui.label_76, self.ui.label_77, self.ui.lineEdit_46, self.ui.toolButton_61,
                    self.ui.label_78, self.ui.label_79, self.ui.lineEdit_38, self.ui.toolButton_62
                ]
                self.on_combo_hidden(widgets)
        if hasattr(self, "_validation_targets") and watched in self._validation_targets:
            validate, error_label = self._validation_targets[watched]

            if event.type() == QEvent.Show:
                validate()
            elif event.type() == QEvent.Hide:
                watched.setStyleSheet("")
                error_label.clear()
                error_label.setVisible(False)
        return super().eventFilter(watched, event)

    def on_combo_shown(self, combo_box):
        """ Function that triggers a fake signal for changed index to be used when a combo box
        changes to shown.

        Arguments:
            combo_box (QComboBox): ComboBox to be used to create the fake signal
        """
        combo_box.currentIndexChanged.emit(combo_box.currentIndex())

    def on_combo_hidden(self, widgets):
        """ Function that hides specific widgets when a combo box changes to hidden

        Arguments:
            widgets (1d array): List of the widgets to hide
        """
        for widget in widgets: 
            widget.hide()

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

    def setup_live_validation(self, line_edit, error_label, validator_func, error_message):
        def validate():
            if not line_edit.isVisibleTo(self):
                return

            text = line_edit.text()
            if text == "" or validator_func(text):
                line_edit.setStyleSheet("")  # Reset border
                error_label.clear()
                error_label.setVisible(False)
            else:
                line_edit.setStyleSheet("border: 2px solid red;")
                error_label.setText(error_message)
                error_label.setVisible(True)

        # Connect text change
        line_edit.textChanged.connect(validate)

        # Install event filter to track visibility
        line_edit.installEventFilter(self)

        # Store both validator and error_label for use in eventFilter
        if not hasattr(self, "_validation_targets"):
            self._validation_targets = {}
        self._validation_targets[line_edit] = (validate, error_label)

        validate()


    def is_valid_number(self, text):
        try:
            float(text)
            return True
        except ValueError:
            return False


if __name__ == "__main__":

    app = QApplication(sys.argv)

    widget = MainWindow()

    widget.show()

    sys.exit(app.exec())

