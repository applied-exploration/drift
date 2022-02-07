class Distribution:
    def __init__(self, glassnode_client):
        """No docstring here yet."""
        pass

    def exchange_balance_total(self, exchange=None):
        """
        The total amount of coins held on exchange addresses.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=distribution.BalanceExchanges>`_

        :return: A DataFrame with exchange balance data.
        :rtype: DataFrame
        """
        pass

    def exchange_balance_percent(self, exchange=None):
        """
        The percent supply held on exchange addresses.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=distribution.BalanceExchangesRelative>`_

        :return: A DataFrame with exchange balance data.
        :rtype: DataFrame
        """
        pass

    def exchange_balance_stacked(self):
        """
        The total amount of coins held on exchange addresses.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=distribution.BalanceExchangesAll>`_

        :return: A DataFrame with stacked exchange balance data.
        :rtype: DataFrame
        """
        pass

    def miner_balance(self):
        """
        The total supply held in miner addresses.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=distribution.BalanceMinersSum>`_

        :return: A DataFrame miner balance data.
        :rtype: DataFrame
        """
        pass

    def miner_balance_stacked(self):
        """
        The total supply held in miner addresses.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=distribution.BalanceMinersAll>`_

        :return: A DataFrame with stacked miner balance data.
        :rtype: DataFrame
        """
        pass

    def balance_miners_change(self):
        """
        The 30d change of the supply held in miner addresses.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=distribution.BalanceMinersChange>`_

        :return: A DataFrame with 30d change of the supply held in miner addresses.
        :rtype: DataFrame
        """
        pass

    def supply_top_one_pct_addresses(self):
        """
        The percentage of supply held by the top 1% addresses.
        `View in Studio <https://studio.glassnode.com/metrics?a=ETH&m=distribution.Balance1PctHolders>`_

        :return: A DataFrame with top 1% supply data.
        :rtype: DataFrame
        """
        pass

    def gini_coefficient(self):
        """
        The gini coefficient for the distribution of coins over addresses.
        `View in Studio <https://studio.glassnode.com/metrics?a=ETH&m=distribution.Gini>`_

        :return: A DataFrame Gini Coefficient data.
        :rtype: DataFrame
        """
        pass

    def herfindahl_index(self):
        """
        A metric for decentralization.
        `View in Studio <https://studio.glassnode.com/metrics?a=ETH&m=distribution.Herfindahl>`_

        :return: A DataFrame Herfindahl index data.
        :rtype: DataFrame
        """
        pass

    def supply_in_smart_contracts(self):
        """
        The percent of total supply of the token that is held in smart contracts.
        `View in Studio <https://studio.glassnode.com/metrics?a=ETH&m=distribution.SupplyContracts>`_

        :return: A DataFrame smart contracts supply data.
        :rtype: DataFrame
        """
        pass
