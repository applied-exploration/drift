class Derivatives:
    def __init__(self, glassnode_client: GlassnodeClient):
        """No docstring here yet."""
        pass

    def futures_perpetual_funding_rate(self, exchange: str = None):
        """
        The average funding rate (in %) set by exchanges for perpetual futures contracts.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=derivatives.FuturesFundingRatePerpetual>`_
        """
        pass

    def futures_perpetual_funding_rate_all(self):
        """
        The average funding rate (in %) set by exchanges for perpetual futures contracts.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=derivatives.FuturesFundingRatePerpetualAll>`_
        """
        pass

    def futures_volume(self, exchange: str = None):
        """
        The total volume traded in futures contracts in the last 24 hours.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=derivatives.FuturesVolumeDailySum>`_
        """
        pass

    def futures_volume_latest_24h(self):
        """
        The total volume traded in futures contracts per exchange over the last 24 hours.
        Values are updated every 10 min.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=derivatives.FuturesVolumeDailyLatest>`_
        """
        pass

    def futures_volume_stacked(self):
        """
        The total volume traded in futures contracts in the last 24 hours.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=derivatives.FuturesVolumeDailySumAll>`_
        """
        pass

    def futures_volume_perpetual(self, exchange: str = None):
        """
        The total volume traded in perpetual (non-expiring) futures contracts in the last 24 hours.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=derivatives.FuturesVolumeDailyPerpetualSum>`_
        """
        pass

    def futures_volume_perpetual_stacked(self):
        """
        The total volume traded in perpetual (non-expiring) futures contracts in the last 24 hours.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=derivatives.FuturesVolumeDailyPerpetualSumAll>`_
        """
        pass

    def futures_open_interest(self, exchange: str = None):
        """
        The total amount of funds allocated in open futures contracts.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=derivatives.FuturesOpenInterestSum>`_
        """
        pass

    def futures_open_interest_current(self):
        """
        The current amount of allocated funds in futures contracts per exchange.Values are updated every 10 min.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=derivatives.FuturesOpenInterestLatest>`_
        """
        pass

    def futures_open_interest_perpetual(self, exchange: str = None):
        """
        The total amount of funds allocated in open perpetual (non-expiring) futures contracts.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=derivatives.FuturesOpenInterestPerpetualSum>`_
        """
        pass

    def futures_open_interest_perpetual_stacked(self):
        """
        The total amount of funds allocated in open perpetual (non-expiring) futures contracts.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=derivatives.FuturesOpenInterestPerpetualSumAll>`_
        """
        pass

    def futures_open_interest_stacked(self):
        """
        The total amount of funds allocated in open futures contracts.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=derivatives.FuturesOpenInterestSumAll>`_
        """
        pass

    def futures_long_liquidations(self, exchange: str = None):
        """
        The sum liquidated volume from long positions in futures contracts.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=derivatives.FuturesLiquidatedVolumeLongSum>`_
        """
        pass

    def futures_long_liquidations_mean(self, exchange: str = None):
        """
        The mean liquidated volume from long positions in futures contracts.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=derivatives.FuturesLiquidatedVolumeLongMean>`_
        """
        pass

    def futures_short_liquidations(self, exchange: str = None):
        """
        The sum liquidated volume from short positions in futures contracts.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=derivatives.FuturesLiquidatedVolumeShortSum>`_
        """
        pass

    def futures_short_liquidations_mean(self, exchange: str = None):
        """
        The mean liquidated volume from short positions in futures contracts.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=derivatives.FuturesLiquidatedVolumeShortMean>`_
        """
        pass

    def futures_estimated_leverage_ratio(self, exchange: str = None):
        """No docstring here yet."""
        pass
