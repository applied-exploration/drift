class Entities:
    def __init__(self, glassnode_client: GlassnodeClient):
        """No docstring here yet."""
        pass

    def sending_entities(self):
        """
        The number of unique entities that were active as a sender.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=entities.SendingCount>`_
        """
        pass

    def receiving_entities(self):
        """
        The number of unique entities that were active as a receiver.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=entities.ReceivingCount>`_
        """
        pass

    def active_entities(self):
        """
        The number of unique entities that were active either as a sender or receiver.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=entities.ActiveCount>`_
        """
        pass

    def new_entities(self):
        """
        The number of unique entities that appeared for the first time
        in a transaction of the native coin in the network.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=entities.NewCount>`_
        """
        pass

    def entities_net_growth(self):
        """
        The net growth of unique entities in the network.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=entities.NetGrowthCount>`_
        """
        pass

    def number_of_whales(self):
        """
        The number of unique entities holding at least 1k coins.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=entities.Min1KCount>`_
        """
        pass

    def supply_balance_less_0001(self):
        """
        The total circulating supply held by entities with a balance lower than 0.001 coins.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=entities.SupplyBalanceLess0001>`_
        """
        pass

    def supply_balance_0001_001(self):
        """
        The total circulating supply held by entities with a balance between 0.001 and 0.01 coins.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=entities.SupplyBalance0001001>`_
        """
        pass

    def supply_balance_001_01(self):
        """
        The total circulating supply held by entities with a balance between 0.01 and 0.1 coins.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=entities.SupplyBalance00101>`_
        """
        pass

    def supply_balance_01_1(self):
        """
        The total circulating supply held by entities with a balance between 0.1 and 1 coins.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=entities.SupplyBalance011>`_
        """
        pass

    def supply_balance_1_10(self):
        """
        The total circulating supply held by entities with a balance between 1 and 10 coins.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=entities.SupplyBalance110>`_
        """
        pass

    def supply_balance_10_100(self):
        """
        The total circulating supply held by entities with a balance between 10 and 100 coins.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=entities.SupplyBalance10100>`_
        """
        pass

    def supply_balance_100_1k(self):
        """
        The total circulating supply held by entities with a balance between 100 and 1,000 coins.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=entities.SupplyBalance1001K>`_
        """
        pass

    def supply_balance_1k_10k(self):
        """
        The total circulating supply held by entities with a balance between 1,000 and 10,000 coins.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=entities.SupplyBalance1K10K>`_
        """
        pass

    def supply_balance_10k_100k(self):
        """
        The total circulating supply held by entities with a balance between 10,000 and 100,000 coins.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=entities.SupplyBalance10K100K>`_
        """
        pass

    def supply_balance_more_100k(self):
        """
        The total circulating supply held by entities with a balance of at least 100,000 coins.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=entities.SupplyBalanceMore100K>`_
        """
        pass

    def entities_supply_distribution(self):
        """
        Relative distribution of the circulating supply held by entities with specific balance bands.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=entities.SupplyDistributionRelative>`_
        """
        pass

    def percent_entities_in_profit(self):
        """
        The percentage of entities in the network that are currently in profit.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=entities.ProfitRelative>`_
        """
        pass
