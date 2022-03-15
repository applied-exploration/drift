def load_data(**kwargs):
    """No docstring here yet."""
    pass


def __load_data(
    assets: DataCollection,
    other_assets: DataCollection,
    exogenous_data: DataCollection,
    target_asset: DataSource,
    load_non_target_asset: bool,
    own_features: list[tuple[str, FeatureExtractor, list[int]]],
    other_features: list[tuple[str, FeatureExtractor, list[int]]],
    exogenous_features: list[tuple[str, FeatureExtractor, list[int]]],
    start_date: Optional[str],
):
    """
    Loads asset data from the specified path.
    Returns:
        - DataFrame `X` with all the training data
        - Series `returns` with only the returns
        - Series `forward_returns` with the target asset returns shifted by 1 day
    """
    pass


def __load_df(
    data_source: DataSource,
    prefix: str,
    returns: Literal["none", "price", "returns", "log_returns"],
    feature_extractors: list[tuple[str, FeatureExtractor, list[int]]],
    resample_to_freq: Optional[Literal["5m", "1h", "1d"]] = None,
):
    """No docstring here yet."""
    pass


def __apply_feature_extractors(
    df: pd.DataFrame, feature_extractors: list[tuple[str, FeatureExtractor, list[int]]]
):
    """No docstring here yet."""
    pass


def load_only_returns(assets: DataCollection, returns: Literal["price", "returns"]):
    """No docstring here yet."""
    pass
