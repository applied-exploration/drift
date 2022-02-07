def unix_timestamp(date_str):
    """
    Returns a unix timestamp to a given date string.

    :param date_str: Date in string format (ex. '2021-01-01').
    :return: Int Unix-timestamp.
    """
    pass


def is_supported_by_endpoint(glassnode_client, url):
    """No docstring here yet."""
    pass


def response_to_dataframe(response):
    """
    Returns DataFrame from a response objects (ex. {"t":1604361600,"v":0.002}).

    :param response: Response from API.
    :return: DataFrame.
    """
    pass


def dataframe_with_inner_object(func):
    """No docstring here yet."""
    pass


def fetch(endpoint, params=None):
    """
    Returns an object of time, value pairs for a metric from the Glassnode API.

    :param params:
    :param endpoint: Endpoint url corresponding to some metric (ex. '/v1/metrics/market/price_usd')
    :return: DataFrame of {'t' : datetime, 'v' : 'metric-value'} pairs
    """
    pass
