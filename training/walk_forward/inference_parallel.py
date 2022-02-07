def walk_forward_inference(
    model_name: str,
    model_over_time: ModelOverTime,
    transformations_over_time: TransformationsOverTime,
    X: XDataFrame,
    expanding_window: bool,
    window_size: int,
    retrain_every: int,
    from_index: Optional[pd.Timestamp],
):
    """No docstring here yet."""
    pass


def __inference_from_window(
    index: int,
    inference_from: int,
    retrain_every: int,
    X: XDataFrame,
    model_over_time: ModelOverTime,
    transformations_over_time: TransformationsOverTime,
    expanding_window: bool,
    window_size: int,
):
    """No docstring here yet."""
    pass
