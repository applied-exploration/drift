def walk_forward_train(
    model: Model,
    X: XDataFrame,
    y: ySeries,
    forward_returns: ForwardReturnSeries,
    window_size: int,
    retrain_every: int,
    from_index: Optional[pd.Timestamp],
    transformations_over_time: TransformationsOverTime,
):
    """No docstring here yet."""
    pass


def train_on_window(
    index: int,
    first_nonzero_return: int,
    X: XDataFrame,
    y: ySeries,
    model: Model,
    transformations_over_time: TransformationsOverTime,
):
    """No docstring here yet."""
    pass
