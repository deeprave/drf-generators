CONVERTERS = """
class PkConverter:
    regex = '([0-9]+|[a-zA-Z0-9_]+)'

    def to_python(self, value):
        return int(value) if value.isnumeric() else value

    def to_url(self, value):
        return f'{value}'
"""