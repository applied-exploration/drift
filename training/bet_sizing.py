def bet_sizing_with_meta_model(
    X: XDataFrame,
    input_predictions: pd.Series,
    y: ySeries,
    forward_returns: ForwardReturnSeries,
    model: Model,
    transformations: list[Transformation],
    config: Config,
    from_index: Optional[pd.Timestamp],
    transformations_over_time: Optional[TransformationsOverTime] = None,
    preloaded_models: Optional[ModelOverTime] = None,
):
    """No docstring here yet."""
    pass
