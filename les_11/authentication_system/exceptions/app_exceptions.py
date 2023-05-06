from les_11.authentication_system.app.messages import Messages


class UnidentifiedOperationSelected(Exception):
    def __init__(self):
        self.message = Messages.unidentified_operation.value
        super().__init__(self.message)
