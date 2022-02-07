def fixed_weight(row: pd.Series, availability_row: pd.Series, allow_short: bool):
    """No docstring here yet."""
    pass


def limit_weight(row: pd.Series):
    """No docstring here yet."""
    pass


def only_top_bottom_2(row: pd.Series):
    """No docstring here yet."""
    pass


def equal_weight(row: pd.Series, availability: pd.Series):
    """No docstring here yet."""
    pass


def create_naive_portfolio_weights(
    predictions: pd.DataFrame, availability: pd.DataFrame, allow_short: bool
):
    """No docstring here yet."""
    pass


def create_quantile_weights(
    predictions: pd.DataFrame, availability: pd.DataFrame, allow_short: bool
):
    """No docstring here yet."""
    pass


def report_alphalens():
    """No docstring here yet."""
    pass


def report_backtest():
    """No docstring here yet."""
    pass
