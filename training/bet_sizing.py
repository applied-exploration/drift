def bet_sizing_with_meta_models(
    X: XDataFrame,
    input_predictions: pd.Series,
    y: ySeries,
    forward_returns: ForwardReturnSeries,
    models: list[Model],
    config: Config,
    model_suffix: str,
    from_index: Optional[pd.Timestamp],
    transformations_over_time: Optional[TransformationsOverTime] = None,
    preloaded_models: Optional[list[ModelOverTime]] = None,
):
    """No docstring here yet."""
    pass
