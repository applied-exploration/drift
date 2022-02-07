class Protocols:
    def __init__(self, glassnode_client):
        """No docstring here yet."""
        pass

    def uniswap_transactions(self):
        """
        The total number of transactions that contains an interaction within Uniswap contracts.
        Includes Mint, Burn, and Swap events on the Uniswap core contracts.
        `View in Studio <https://studio.glassnode.com/metrics?a=ETH&m=protocols.UniswapTransactionCount>`_

        :return: A DataFrame containing Uniswap transactions data.
        :rtype: DataFrame
        """
        pass

    def uniswap_liquidity(self):
        """
        The current liquidity on Uniswap.
        `View in Studio <https://studio.glassnode.com/metrics?a=ETH&m=protocols.UniswapLiquidityLatest>`_

        :return: A DataFrame containing Uniswap liquidity data.
        :rtype: DataFrame
        """
        pass

    def uniswap_volume(self):
        """
        The total volume traded on Uniswap.
        `View in Studio <https://studio.glassnode.com/metrics?a=ETH&m=protocols.UniswapVolumeSum>`_

        :return: A DataFrame containing Uniswap volume data.
        :rtype: DataFrame
        """
        pass
