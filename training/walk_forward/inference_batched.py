def walk_forward_inference_batched(
    model_name: str,
    model_over_time: ModelOverTime,
    transformations_over_time: TransformationsOverTime,
    X: XDataFrame,
    expanding_window: bool,
    window_size: int,
    retrain_every: int,
    class_labels: list[int],
    from_index: Optional[pd.Timestamp],
):
    """No docstring here yet."""
    pass


def __inference_from_window(
    index_start: int,
    index_end: int,
    X: XDataFrame,
    model_over_time: ModelOverTime,
    transformations_over_time: TransformationsOverTime,
    expanding_window: bool,
    window_size: int,
):
    """No docstring here yet."""
    pass
