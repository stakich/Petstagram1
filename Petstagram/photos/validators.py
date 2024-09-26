from django.core.exceptions import ValidationError
from django.core.validators import BaseValidator


class FileSizeValidator(BaseValidator):
    def __init__(self, limit_value):
        super().__init__(limit_value * 1048567)

    def compare(self, file_size, limit_value):
        return file_size > limit_value

    def clean(self, file):
        return file_size

    def deconstruct(self):
        path, args, kwargs = super().deconstruct()
        kwargs['limit_value'] = self.limit_value / 1048576  # Convert bytes back to MB
        return path, args, kwargs
