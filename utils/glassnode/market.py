class Market:
    def __init__(self, glassnode_client):
        """No docstring here yet."""
        pass

    def price(self):
        """
        The asset's price in USD.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=market.PriceUsd>`_

        :return: A DataFrame containing the asset's price data.
        :rtype: DataFrame
        """
        pass

    def price_ohlc(self):
        """
        OHLC candlestick chart of the asset's price in USD.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=market.PriceUsdOhlc>`_

        :return: A DataFrame containing OHLC candlestick data.
        :rtype: DataFrame
        """
        pass

    def price_drawdown_from_ath(self):
        """
        The percent drawdown of the asset's price from the previous all-time high.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=market.PriceDrawdownRelative>`_

        :return: A DataFrame containing the percent drawdown data.
        :rtype: DataFrame
        """
        pass

    def marketcap(self):
        """
        The market capitalization (or network value) is defined as
        the product of the current supply by the current USD price.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=market.MarketcapUsd>`_

        :return: DataFrame
        """
        pass

    def mvrv_ratio(self):
        """
        MVRV is the ratio between market cap and realised cap.
        It gives an indication of when the traded price is below a “fair value”.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=market.Mvrv>`_

        :return: DataFrame
        """
        pass

    def realized_cap(self):
        """
        Realized Cap values different part of the supplies at different prices (instead of using current daily close).
        Specifically, it is computed by valuing each UTXO by the price when it was last moved.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=market.MarketcapRealizedUsd>`_

        :return: DataFrame
        """
        pass

    def mvrv_z_score(self):
        """
        The MVRV Z-Score is used to assess when Bitcoin is over/undervalued relative to its "fair value".
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=market.MvrvZScore>`_

        :return: DataFrame
        """
        pass

    def sth_mvrv(self):
        """
        Short Term Holder MVRV (STH-MVRV) is MVRV that takes into account only UTXOs younger than 155 days and
        serves as an indicator to assess the behaviour of short term investors.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=market.MvrvLess155>`_

        :return: DataFrame
        """
        pass

    def lth_mvrv(self):
        """
        Long Term Holder MVRV (LTH-MVRV) is MVRV that takes into account only UTXOs with a lifespan of at least 155 days
        and serves as an indicator to assess the behaviour of long term investors
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=market.MvrvMore155>`_

        :return: DataFrame
        """
        pass

    def realized_price(self):
        """
        Realized Price is the Realized Cap divided by the current supply.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=market.PriceRealizedUsd>`_

        :return: DataFrame
        """
        pass
