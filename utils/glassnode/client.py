class GlassnodeClient:
    def __init__(
        self,
        api_key=None,
        asset="BTC",
        resolution="24h",
        currency="native",
        since=None,
        until=None,
    ):
        """
        Glassnode API client.

        :param asset: Asset to which the metric refers. (ex. BTC)
        :param resolution: Temporal resolution of the data received. Can be '10m', '1h', '24h', '1w' or '1month'.
        :param currency: NATIVE, USD
        :param since: Start date as a string (ex. 2015-11-27)
        :param until: Start date as a string (ex. 2018-05-03)
        """
        pass

    def asset(self):
        """No docstring here yet."""
        pass

    def resolution(self):
        """No docstring here yet."""
        pass

    def get(self, endpoint, params=None):
        """No docstring here yet."""
        pass

    def __prepare_request_params(self, params):
        """No docstring here yet."""
        pass
