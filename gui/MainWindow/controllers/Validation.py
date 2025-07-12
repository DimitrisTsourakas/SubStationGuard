import ast, math

def setup_live_validation(self, line_edit, error_label, validator_func, error_message):
        def validate():
            if not line_edit.isVisible():
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

def is_valid_number(text: str) -> bool:
    try:
        float(text)
        return True
    except ValueError:
        return False

def is_valid_function(text: str) -> bool:
    try:
        node = ast.parse(text, mode="eval")
    except SyntaxError:
        return False

    allowed = (
        ast.Expression, ast.BinOp, ast.UnaryOp, ast.Call,
        ast.Name, ast.Load, ast.Constant,
        ast.Add, ast.Sub, ast.Mult, ast.Div, ast.Pow,
        ast.USub, ast.UAdd,
    )
    safe_names = {"x"} | {
        name for name in dir(math) if not name.startswith("_")
    }

    for sub in ast.walk(node):
        if not isinstance(sub, allowed):
            return False
        if isinstance(sub, ast.Name) and sub.id not in safe_names:
            return False

    return True