class Mining:
    def __init__(self, glassnode_client):
        """No docstring here yet."""
        pass

    def difficulty(self):
        """
        The current estimated number of hashes required to mine a block. Values are denoted in raw hashes.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=mining.DifficultyLatest>`_

        :return: A DataFrame with the latest difficulty data.
        :rtype: DataFrame
        """
        pass

    def hash_rate(self):
        """
        The average estimated number of hashes per second produced by the miners in the network.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=mining.HashRateMean>`_

        :return: A DataFrame with hash rate data.
        :rtype: DataFrame
        """
        pass

    def miner_revenue_total(self, miner=None):
        """
        The total miner revenue, i.e. fees plus newly minted coins.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=mining.RevenueSum>`_

        :return: A DataFrame with total revenue data.
        :rtype: DataFrame
        """
        pass

    def miner_revenue_fees(self):
        """
        The percentage of miner revenue derived from fees, i.e. fees divided by fees plus minted coins.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=mining.RevenueFromFees>`_

        :return: A DataFrame with revenue fees data.
        :rtype: DataFrame
        """
        pass

    def miner_revenue_block_rewards(self, miner=None):
        """
        The total amount of newly minted coins, i.e. block rewards.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=mining.VolumeMinedSum>`_

        :return: A DataFrame with revenue block rewards data.
        :rtype: DataFrame
        """
        pass

    def miner_outflow_multiple(self, miner=None):
        """
        The Miner Outflow Multiple indicates periods where the amount of bitcoins flowing out of
        miner addresses is high with respect to its historical average.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=mining.MinersOutflowMultiple>`_

        :return: A DataFrame MOM data.
        :rtype: DataFrame
        """
        pass

    def thermocap(self):
        """
        "Thermocap" is the aggregated amount of coins paid to miners and serves as a proxy to mining resources spent.
        It serves a measure of the true capital flow into Bitcoin.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=mining.Thermocap>`_

        :return: A DataFrame with thermocap data.
        :rtype: DataFrame
        """
        pass

    def market_cap_to_thermocap_ratio(self):
        """
        The Marketcap to Thermocap Ratio can be used to assess if the asset's price is currently trading
        at a premium with respect to total security spend by miners.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=mining.MarketcapThermocapRatio>`_

        :return: A DataFrame with M/T ratio data.
        :rtype: DataFrame
        """
        pass

    def miner_unspent_supply(self):
        """
        The total mount of coins in coinbase transactions that have never been moved.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=mining.MinersUnspentSupply>`_

        :return: A DataFrame with unspent miner supply data.
        :rtype: DataFrame
        """
        pass

    def miner_names(self, endpoint="revenue_sum"):
        """
        Returns a list of miner names for a mining endpoint.

        :param endpoint: Available endpoints: revenue_sum, volume_mined_sum, miners_outflow_multiple
        :return: A List with miner names.
        :rtype: List
        """
        pass
