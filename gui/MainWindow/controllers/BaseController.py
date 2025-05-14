from PySide6.QtCore import QObject
from PySide6.QtCore import QEvent

class BaseController(QObject):
    def __init__(self, parent=None):
        super().__init__(parent)

    def show_widgets(self, widgets):
        """ Function that shows specific widgets

        Arguments:
            widgets (1d array): List of the widgets to show
        """
        for w in widgets:
            w.setVisible(True)

    def hide_widgets(self, widgets):
        """ Function that hides specific widgets

        Arguments:
            widgets (1d array): List of the widgets to hide
        """
        for w in widgets:
            w.setVisible(False)

    def toggle_widgets(self, condition, widgets_show, widgets_hide):
        if condition:
            self.show_widgets(widgets_show)
            self.hide_widgets(widgets_hide)
        else:
            self.show_widgets(widgets_hide)
            self.hide_widgets(widgets_show)

    def enable_combo_item(self, combo_box, index, enabled):
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

    def emit_index_changed_on_show(self, combo_box):
        """ Function that triggers a fake signal for changed index to be used when a combo box
        changes to shown.

        Arguments:
            combo_box (QComboBox): ComboBox to be used to create the fake signal
        """
        combo_box.currentIndexChanged.emit(combo_box.currentIndex())

    def hide_widgets_on_combo_hide(self, widgets):
        """ Function that hides specific widgets when a combo box changes to hidden

        Arguments:
            widgets (1d array): List of the widgets to hide
        """
        for widget in widgets: 
            widget.hide()

    def emit_index_changed_on_show(self, combo_box):
        """ Function that triggers a fake signal for changed index to be used when a combo box
        changes to shown.

        Arguments:
            combo_box (QComboBox): ComboBox to be used to create the fake signal
        """
        combo_box.currentIndexChanged.emit(combo_box.currentIndex())

    def hide_widgets_on_combo_hide(self, widgets):
        """ Function that hides specific widgets when a combo box changes to hidden

        Arguments:
            widgets (1d array): List of the widgets to hide
        """
        for widget in widgets: 
            widget.hide()

    def eventFilter(self, watched, event):
        """ Function that intercepts show and hide events in order to run a custom functionality.
        The current fuction will trigger emit_index_changed_on_show and hide_widgets_on_combo_hide 
        functions for combo box comboBox_16 on Show and Hide events respectively

        Arguments:
            combo_box (QComboBox): ComboBox to be used to create the fake signal
        """
        if watched == self.ui.comboBox_16:
            if event.type() == QEvent.Show:
                self.emit_index_changed_on_show(self.ui.comboBox_16)
            elif event.type() == QEvent.Hide:
                widgets = [
                    self.ui.label_74, self.ui.label_75, self.ui.lineEdit_45, self.ui.toolButton_60,
                    self.ui.label_76, self.ui.label_77, self.ui.lineEdit_46, self.ui.toolButton_61,
                    self.ui.label_78, self.ui.label_79, self.ui.lineEdit_38, self.ui.toolButton_62
                ]
                self.hide_widgets_on_combo_hide(widgets)
        if hasattr(self, "_validation_targets") and watched in self._validation_targets:
            validate, error_label = self._validation_targets[watched]

            if event.type() == QEvent.Show:
                validate()
            elif event.type() == QEvent.Hide:
                watched.setStyleSheet("")
                error_label.clear()
                error_label.setVisible(False)
        return super().eventFilter(watched, event)