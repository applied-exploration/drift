def train_model(
    ticker_to_predict: str,
    X: pd.DataFrame,
    y: pd.Series,
    forward_returns: pd.Series,
    model: Model,
    initial_window_size: int,
    retrain_every: int,
    from_index: Optional[pd.Timestamp],
    level: str,
    class_labels: list[int],
    transformations_over_time: TransformationsOverTime,
    model_over_time: Optional[ModelOverTime],
):
    """No docstring here yet."""
    pass
