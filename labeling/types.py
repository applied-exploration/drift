class EventFilter(ABC):
    def get_event_start_times(self, returns: ReturnSeries):
        """No docstring here yet."""
        pass


class EventSchema(pa.SchemaModel):
    pass


class EventLabeller(ABC):
    def label_events(
        self, event_start_times: pd.DatetimeIndex, forward_returns: ForwardReturnSeries
    ):
        """No docstring here yet."""
        pass
