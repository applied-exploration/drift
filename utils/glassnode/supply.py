class Supply:
    def __init__(self, glassnode_client: GlassnodeClient):
        """No docstring here yet."""
        pass

    def liquid_illiquid_supply(self):
        """
        The total supply held by illiquid, liquid, and highly liquid entities.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=supply.LiquidIlliquidSum>`_

        :rtype: DataFrame
        """
        pass

    def liquid_supply_change(self):
        """
        The monthly (30d) net change of supply held by liquid and highly liquid entities.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=supply.LiquidChange>`_

        :rtype: DataFrame
        """
        pass

    def illiquid_supply_change(self):
        """
        The monthly (30d) net change of supply held by illiquid entities.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=supply.IlliquidChange>`_

        :rtype: DataFrame
        """
        pass

    def circulating_supply(self):
        """
        The total amount of all coins ever created/issued, i.e. the circulating supply.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=supply.Current>`_

        :rtype: DataFrame
        """
        pass

    def issuance(self):
        """
        The total amount of new coins added to the current supply,
        i.e. minted coins or new coins released to the network.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=supply.Issued>`_

        :rtype: DataFrame
        """
        pass

    def inflation_rate(self):
        """
        The yearly inflation rate, i.e. the percentage of new coins issued,
        divided by the current supply (annualized).
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=supply.InflationRate>`_

        :rtype: DataFrame
        """
        pass

    def supply_last_active_less_24h(self):
        """
        The amount of circulating supply last moved in the last 24 hours.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=supply.Active24H>`_

        :rtype: DataFrame
        """
        pass

    def supply_last_active_1d_1w(self):
        """
        The amount of circulating supply last moved between 1 day and 1 week ago.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=supply.Active1D1W>`_

        :rtype: DataFrame
        """
        pass

    def supply_last_active_1w_1m(self):
        """
        The amount of circulating supply last moved between 1 week and 1 month ago.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=supply.Active1W1M>`_

        :rtype: DataFrame
        """
        pass

    def supply_last_active_1m_3m(self):
        """
        The amount of circulating supply last moved between 1 month and 3 months ago.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=supply.Active1M3M>`_

        :rtype: DataFrame
        """
        pass

    def supply_last_active_3m_6m(self):
        """
        The amount of circulating supply last moved between 3 months and 6 months ago.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=supply.Active3M6M>`_

        :rtype: DataFrame
        """
        pass

    def supply_last_active_6m_12m(self):
        """
        The amount of circulating supply last moved between 6 months and 12 months ago.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=supply.Active6M12M>`_

        :rtype: DataFrame
        """
        pass

    def supply_last_active_1y_2y(self):
        """
        The amount of circulating supply last moved between 1 year and 2 years ago.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=supply.Active1Y2Y>`_

        :rtype: DataFrame
        """
        pass

    def supply_last_active_2y_3y(self):
        """
        The amount of circulating supply last moved between 2 years and 3 years ago.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=supply.Active1Y2Y>`_

        :rtype: DataFrame
        """
        pass

    def supply_last_active_3y_5y(self):
        """
        The amount of circulating supply last moved between 3 years and 5 years ago.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=supply.Active3Y5Y>`_

        :rtype: DataFrame
        """
        pass

    def supply_last_active_5y_7y(self):
        """
        The amount of circulating supply last moved between 5 years and 7 years ago.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=supply.Active5Y7Y>`_

        :rtype: DataFrame
        """
        pass

    def supply_last_active_7y_10y(self):
        """
        The amount of circulating supply last moved between 7 years and 10 years ago.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=supply.Active7Y10Y>`_

        :rtype: DataFrame
        """
        pass

    def supply_last_active_more_10y(self):
        """
        The amount of circulating supply last moved more than 10 years ago.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=supply.ActiveMore10Y>`_

        :rtype: DataFrame
        """
        pass

    def hodl_waves(self):
        """
        Bundle of all active supply age bands, aka HODL waves.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=supply.HodlWaves>`_

        :rtype: DataFrame
        """
        pass

    def supply_last_active_more_1y_ago(self):
        """
        The percent of circulating supply that has not moved in at least 1 year.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=supply.ActiveMore1YPercent>`_

        :rtype: DataFrame
        """
        pass

    def supply_last_active_more_2y_ago(self):
        """
        The percent of circulating supply that has not moved in at least 2 years.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=supply.ActiveMore2YPercent>`_

        :rtype: DataFrame
        """
        pass

    def supply_last_active_more_3y_ago(self):
        """
        The percent of circulating supply that has not moved in at least 3 years.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=supply.ActiveMore3YPercent>`_

        :rtype: DataFrame
        """
        pass

    def supply_last_active_more_5y_ago(self):
        """
        The percent of circulating supply that has not moved in at least 5 years.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=supply.ActiveMore5YPercent>`_

        :rtype: DataFrame
        """
        pass

    def realized_cap_hodl_waves(self):
        """
        HODL Waves weighted by Realized Price.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=supply.RcapHodlWaves>`_

        :rtype: DataFrame
        """
        pass

    def adjusted_supply(self):
        """
        The circulating supply adjusted by accounting for lost coins.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=supply.CurrentAdjusted>`_

        :rtype: DataFrame
        """
        pass

    def supply_in_profit(self):
        """
        The circulating supply in profit,
        i.e. the amount of coins whose price at the time they last moved was lower than the current price.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=supply.ProfitSum>`_

        :rtype: DataFrame
        """
        pass

    def supply_in_loss(self):
        """
        The circulating supply in loss,
        i.e. the amount of coins whose price at the time they last moved was higher than the current price.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=supply.LossSum>`_

        :rtype: DataFrame
        """
        pass

    def supply_in_profit_relative(self):
        """
        The percentage of circulating supply in profit.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=supply.ProfitRelative>`_

        :rtype: DataFrame
        """
        pass

    def short_term_holder_supply(self):
        """
        The total amount of circulating supply held by short-term holders.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=supply.SthSum>`_

        :rtype: DataFrame
        """
        pass

    def long_term_holder_supply(self):
        """
        The total amount of circulating supply held by long-term holders.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=supply.LthSum>`_

        :rtype: DataFrame
        """
        pass

    def short_term_holder_supply_in_loss(self):
        """
        The total amount of circulating supply that is currently at loss and held by short-term holders.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=supply.SthLossSum>`_

        :rtype: DataFrame
        """
        pass

    def long_term_holder_supply_in_loss(self):
        """
        The total amount of circulating supply that is currently at loss and held by long-term holders.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=supply.LthLossSum>`_

        :rtype: DataFrame
        """
        pass

    def short_term_holder_supply_in_profit(self):
        """
        The total amount of circulating supply that is currently in profit and held by short-term holders.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=supply.SthProfitSum>`_

        :rtype: DataFrame
        """
        pass

    def long_term_holder_supply_in_profit(self):
        """
        The total amount of circulating supply that is currently in profit and held by long-term holders.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=supply.LthProfitSum>`_

        :rtype: DataFrame
        """
        pass

    def relative_long_short_term_holder_supply(self):
        """
        The relative amount of circulating supply of held by long- and short-term holders in profit/loss.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=supply.LthSthProfitLossRelative>`_

        :rtype: DataFrame
        """
        pass

    def long_term_holder_position_change(self):
        """
        The monthly net position change of long-term holders,
        i.e. the 30 day change in supply held by long-term holders.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=supply.LthNetChange>`_

        :rtype: DataFrame
        """
        pass
