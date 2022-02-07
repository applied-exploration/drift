def create_endpoints_dict(endpoints):
    """No docstring here yet."""
    pass


class MetaEndpoints(type):
    def __call__(cls, *args, **kwargs):
        """No docstring here yet."""
        pass


class Endpoints(metaclass=MetaEndpoints):
    def endpoints(self):
        """No docstring here yet."""
        pass

    def endpoints(self, api_key):
        """No docstring here yet."""
        pass

    def query(self, path):
        """No docstring here yet."""
        pass
