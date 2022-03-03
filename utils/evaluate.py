def backtest(returns: pd.Series, signal: pd.Series, transaction_cost: float):
    """No docstring here yet."""
    pass


def __preprocess(
    forward_returns: ForwardReturnSeries,
    y_pred: pd.Series,
    y_true: pd.Series,
    discretize_func: Callable,
    transaction_costs: float,
):
    """No docstring here yet."""
    pass


def evaluate_predictions(
    forward_returns: ForwardReturnSeries,
    y_pred: WeightsSeries,
    y_true: ySeries,
    discretize_func: Callable,
    labels: list[int],
    transaction_costs: float,
):
    """No docstring here yet."""
    pass
