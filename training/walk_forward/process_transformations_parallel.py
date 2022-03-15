def walk_forward_process_transformations(
    X: XDataFrame,
    y: ySeries,
    forward_returns: ForwardReturnSeries,
    window_size: int,
    retrain_every: int,
    from_index: Optional[pd.Timestamp],
    transformations: list[Transformation],
):
    """No docstring here yet."""
    pass


def preprocess_transformations_window(
    X: XDataFrame,
    y: ySeries,
    transformations: list[Transformation],
    first_nonzero_return: int,
    index: int,
):
    """No docstring here yet."""
    pass
