class Fees:
    def __init__(self, glassnode_client: GlassnodeClient):
        """No docstring here yet."""
        pass

    def fee_ratio_multiple(self):
        """
        The Fee Ratio Multiple (FRM) is a measure of a blockchain's security
        and gives an assessment how secure a chain is once block rewards disappear.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=fees.FeeRatioMultiple>`_
        """
        pass

    def fees_total(self):
        """
        The total amount of fees paid to miners. Issued (minted) coins are not included.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=fees.VolumeSum>`_
        """
        pass

    def fees_mean(self):
        """
        The mean fee per transaction. Issued (minted) coins are not included.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=fees.VolumeMean>`_
        """
        pass

    def fees_median(self):
        """
        The median fee per transaction. Issued (minted) coins are not included.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=fees.VolumeMedian>`_
        """
        pass

    def gas_used_total(self):
        """
        The total amount of gas used in all transactions.
        `View in Studio <https://studio.glassnode.com/metrics?a=ETH&m=fees.GasUsedSum>`_
        """
        pass

    def gas_used_mean(self):
        """
        The mean amount of gas used per transaction.
        `View in Studio <https://studio.glassnode.com/metrics?a=ETH&m=fees.GasUsedMean>`_
        """
        pass

    def gas_used_median(self):
        """
        The median amount of gas used per transaction.
        `View in Studio <https://studio.glassnode.com/metrics?a=ETH&m=fees.GasUsedMedian>`_
        """
        pass

    def gas_price_mean(self):
        """
        The mean gas price paid per transaction.
        `View in Studio <https://studio.glassnode.com/metrics?a=ETH&m=fees.GasPriceMean>`_
        """
        pass

    def gas_price_median(self):
        """
        The median gas price paid per transaction.
        `View in Studio <https://studio.glassnode.com/metrics?a=ETH&m=fees.GasPriceMedian>`_
        """
        pass

    def transaction_gas_limit_mean(self):
        """
        The mean gas limit per transaction.
        `View in Studio <https://studio.glassnode.com/metrics?a=ETH&m=fees.GasLimitTxMean>`_
        """
        pass

    def transaction_gas_limit_median(self):
        """
        The median gas limit per transaction.
        `View in Studio <https://studio.glassnode.com/metrics?a=ETH&m=fees.GasLimitTxMedian>`_
        """
        pass

    def exchange_fees_total(self):
        """
        The total amount of fees paid in transactions related to on-chain exchange activity.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=fees.ExchangesSum>`_
        """
        pass

    def exchange_fees_mean(self):
        """
        The mean amount of fees paid in transactions related to on-chain exchange activity.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=fees.ExchangesMean>`_
        """
        pass

    def exchange_fees_dominance(self):
        """
        The Exchange Fee Dominance metric is defined as the percent amount of total fees
        paid in transactions related to on-chain exchange activity.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=fees.ExchangesRelative>`_
        """
        pass
