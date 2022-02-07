def backtest(returns: pd.Series, signal: pd.Series, transaction_cost=0.002):
    """No docstring here yet."""
    pass


def __preprocess(
    forward_returns: ForwardReturnSeries,
    y_pred: pd.Series,
    y_true: pd.Series,
    no_of_classes: Literal["two", "three-balanced", "three-imbalanced"],
    discretize: bool,
):
    """No docstring here yet."""
    pass


def evaluate_predictions(
    forward_returns: ForwardReturnSeries,
    y_pred: WeightsSeries,
    y_true: ySeries,
    no_of_classes: Literal["two", "three-balanced", "three-imbalanced"],
    discretize: bool = False,
):
    """No docstring here yet."""
    pass


def __discretize_binary(x):
    """No docstring here yet."""
    pass


def __discretize_threeway(x):
    """No docstring here yet."""
    pass


def discretize_threeway_threshold(threshold: float):
    """No docstring here yet."""
    pass


def get_discretize_function(
    no_of_classes: Literal["two", "three-balanced", "three-imbalanced"]
):
    """No docstring here yet."""
    pass
