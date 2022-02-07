class Blockchain:
    def __init__(self, glassnode_client: GlassnodeClient):
        """No docstring here yet."""
        pass

    def utxos_total(self):
        """
        The total number of UTXOs in the network.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=blockchain.UtxoCount>`_

        :return: DataFrame
        """
        pass

    def utxos_created(self):
        """
        The number of created unspent transaction outputs.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=blockchain.UtxoCreatedCount>`_

        :return: DataFrame
        """
        pass

    def utxos_spent(self):
        """
        The number of spent transaction outputs.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=blockchain.UtxoSpentCount>`_

        :return: DataFrame
        """
        pass

    def utxo_value_created_total(self):
        """
        The total amount of coins in newly created UTXOs.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=blockchain.UtxoCreatedValueSum>`_

        :return: DataFrame
        """
        pass

    def utxo_value_spent_total(self):
        """
        The total amount of coins in spent transaction outputs.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=blockchain.UtxoSpentValueSum>`_

        :return: DataFrame
        """
        pass

    def utxo_value_created_mean(self):
        """
        The mean amount of coins in newly created UTXOs.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=blockchain.UtxoCreatedValueMean>`_

        :return: DataFrame
        """
        pass

    def utxo_value_spent_mean(self):
        """
        The mean amount of coins in spent transaction outputs.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=blockchain.UtxoSpentValueMean>`_

        :return: DataFrame
        """
        pass

    def utxo_value_created_median(self):
        """
        The median amount of coins in newly created UTXOs.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=blockchain.UtxoCreatedValueMedian>`_

        :return: DataFrame
        """
        pass

    def utxo_value_spent_median(self):
        """
        The median amount of coins in spent transaction outputs.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=blockchain.UtxoSpentValueMedian>`_

        :return: DataFrame
        """
        pass

    def utxos_in_profit(self):
        """
        The number of unspent transaction outputs whose price at creation time was lower than the current price.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=blockchain.UtxoProfitCount>`_

        :return: DataFrame
        """
        pass

    def utxos_in_loss(self):
        """
        The number of unspent transaction outputs whose price at creation time was higher than the current price.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=blockchain.UtxoLossCount>`_

        :return: DataFrame
        """
        pass

    def percent_utxos_in_profit(self):
        """
        The percentage of unspent transaction outputs whose price at creation time was lower than the current price.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=blockchain.UtxoProfitRelative>`_

        :return: DataFrame
        """
        pass

    def block_heights(self):
        """
        The block height, i.e. the total number of blocks ever created and included in the main blockchain.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=blockchain.BlockHeight>`_

        :return: DataFrame
        """
        pass

    def blocks_mined(self):
        """
        The number of blocks created and included in the main blockchain in that time period.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=blockchain.BlockCount>`_

        :return: DataFrame
        """
        pass

    def block_interval_mean(self):
        """
        The mean time (in seconds) between mined blocks.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=blockchain.BlockIntervalMean>`_

        :return: DataFrame
        """
        pass

    def block_interval_median(self):
        """
        The median time (in seconds) between mined blocks.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=blockchain.BlockIntervalMedian>`_

        :return: DataFrame
        """
        pass

    def block_size_mean(self):
        """
        The mean size of all blocks created within the time period (in bytes).
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=blockchain.BlockSizeMean>`_

        :return: DataFrame
        """
        pass

    def block_size_total(self):
        """
        The total size of all blocks created within the time period (in bytes).
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=blockchain.BlockSizeSum>`_

        :return: DataFrame
        """
        pass
