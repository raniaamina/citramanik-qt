class BaseCitramanikException(Exception):
    pass

class CitraManikCancelException(BaseCitramanikException):
    def __init__(self, export_format, id_process):
        self.message = f"Process canceled, {id_process} - {export_format}"
        super().__init__(self.message)

    def __str__(self):
        return self.message
