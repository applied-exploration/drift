class CUSUMVolatilityEventFilter(EventFilter):
    def __init__(self, vol_period: int, multiplier: float):
        """No docstring here yet."""
        pass

    def get_event_start_times(self, returns: ReturnSeries):
        """No docstring here yet."""
        pass


class CUSUMFixedEventFilter(EventFilter):
    def __init__(self, threshold: float):
        """No docstring here yet."""
        pass

    def get_event_start_times(self, returns: ReturnSeries):
        """No docstring here yet."""
        pass


def _process_fixed(diffed_returns: List, threshold: float32):
    """No docstring here yet."""
    pass


def _process_vol_based(diffed_returns: List, rolling_vol: List):
    """No docstring here yet."""
    pass
