class Indicators:
    def __init__(self, glassnode_client: GlassnodeClient):
        """No docstring here yet."""
        pass

    def rhodl_ratio(self):
        """
        The Realized HODL Ratio is a market indicator that uses a ratio of the Realized Cap HODL Waves.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=indicators.RhodlRatio>`_
        """
        pass

    def cvdd(self):
        """
        Cumulative Value-Days Destroyed (CVDD) is the ratio of the cumulative USD value of Coin Days Destroyed and
        the market age (in days). Historically, CVDD has been an accurate indicator for global Bitcoin market bottoms.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=indicators.Cvdd>`_
        """
        pass

    def hash_ribbon(self):
        """
        The Hash Ribbon is a market indicator that assumes that Bitcoin tends to reach a bottom when miners capitulate,
        i.e. when Bitcoin becomes too expensive to mine relative to the cost of mining. The Hash Ribbon indicates that
        the worst of the miner capitulation is over when the 30d MA of the hash rate crosses above the 60d MA.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=indicators.HashRibbon>`_
        """
        pass

    def difficulty_ribbon(self):
        """
        The Difficulty Ribbon is an indicator that uses simple moving averages
         of the Bitcoin mining difficulty to create the ribbon.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=indicators.DifficultyRibbon>`_
        """
        pass

    def difficulty_ribbon_compression(self):
        """
        Difficulty Ribbon Compression is a market indicator that uses a normalized
        standard deviation to quantify compression of the Difficulty Ribbon.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=indicators.DifficultyRibbonCompression>`_
        """
        pass

    def nvt_ratio(self):
        """
        The Network Value to Transactions (NVT) Ratio is computed by dividing
        the market cap by the transferred on-chain volume measured in USD.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=indicators.Nvt>`_
        """
        pass

    def nvt_signal(self):
        """
        The NVT Signal (NVTS) is a modified version of the original NVT Ratio.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=indicators.Nvts>`_
        """
        pass

    def velocity(self):
        """
        Velocity is a measure of how quickly units are circulating in the network and is calculated
        by dividing the on-chain transaction volume (in USD) by the market cap, i.e. the inverse of the NVT ratio.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=indicators.Velocity>`_
        """
        pass

    def supply_adjusted_cdd(self):
        """
        Adjusted Coin Days Destroyed simply divides CDD by the circulating supply.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=indicators.CddSupplyAdjusted>`_
        """
        pass

    def binary_cdd(self):
        """
        Binary Coin Days Destroyed is computed by thresholding Adjusted CDD by its average over time.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=indicators.CddSupplyAdjustedBinary>`_
        """
        pass

    def supply_adjusted_dormancy(self):
        """
        Dormancy is the average number of days destroyed per coin transacted,
        and is defined as the ratio of coin days destroyed and total transfer volume.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=indicators.AverageDormancySupplyAdjusted>`_
        """
        pass

    def sopd_ath_partitioned(self):
        """
        UTXO Realized Price Distribution (URPD) shows at which prices UTXOs were spent that day.
        ATH-partitioned means that the price buckets are defined by dividing the range between
        0 and the current ATH in 100 equally-spaced partitions.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=indicators.SpentOutputPriceDistributionAth>`_
        """
        pass

    def sopd_percent_partitioned(self):
        """
        UTXO Realized Price Distribution (URPD) shows at which prices UTXOs were spent that day.
        %-partitioned means that the price buckets are defined by taking the day's closing price
        and creating 50 equally-spaced bucket each above and below the current price in steps of +/- 2%.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=indicators.SpentOutputPriceDistributionPercent>`_
        """
        pass

    def puell_multiple(self):
        """
        The Puell Multiple is calculated by dividing the daily issuance value of bitcoins (in USD)
        by the 365-day moving average of daily issuance value.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=indicators.PuellMultiple>`_
        """
        pass

    def asopr(self):
        """
        Adjusted SOPR is SOPR ignoring all outputs with a lifespan of less than 1 hour.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=indicators.SoprAdjusted>`_
        """
        pass

    def reserve_risk(self):
        """
        When confidence is high and price is low, there is an attractive risk/reward to invest (Reserve Risk is low).
        When confidence is low and price is high then risk/reward is unattractive at that time (Reserve Risk is high).
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=indicators.ReserveRisk>`_
        """
        pass

    def sth_sopr(self):
        """
        Short Term Holder SOPR (STH-SOPR) is SOPR that takes into account only spent outputs
        younger than 155 days and serves as an indicator to assess the behaviour of short term investors.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=indicators.SoprLess155>`_
        """
        pass

    def lth_sopr(self):
        """
        Long Term Holder SOPR (LTH-SOPR) is SOPR that takes into account only spent outputs with a lifespan
        of at least 155 days and serves as an indicator to assess the behaviour of long term investors.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=indicators.SoprMore155>`_
        """
        pass

    def hodler_net_position_change(self):
        """
        HODLer Net Position Change shows the monthly position change of long term investors.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=indicators.HodlerNetPositionChange>`_
        """
        pass

    def hodled_or_lost_coins(self):
        """
        Lost or HODLed Bitcoins indicates moves of large and old stashes.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=indicators.HodledLostCoins>`_
        """
        pass

    def sopr(self):
        """
        The Spent Output Profit Ratio (SOPR) is computed by dividing the realized value (in USD)
        divided by the value at creation (USD) of a spent output. Or simply: price sold / price paid.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=indicators.Sopr>`_
        """
        pass

    def cdd(self):
        """
        Coin Days Destroyed (CDD) for any given transaction is calculated by taking the number of coins
        in a transaction and multiplying it by the number of days it has been since those coins were last spent.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=indicators.Cdd>`_
        """
        pass

    def asol(self):
        """
        Average Spent Output Lifespan (ASOL) is the average age (in days) of spent transaction outputs.
        Outputs with a lifespan of less than 1h are discarded.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=indicators.Asol>`_
        """
        pass

    def msol(self):
        """
        Median Spent Output Lifespan (MSOL) is the median age (in days) of spent transaction outputs.
        Outputs with a lifespan of less than 1h are discarded.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=indicators.Msol>`_
        """
        pass

    def dormancy(self):
        """
        Dormancy is the average number of days destroyed per coin transacted,
        and is defined as the ratio of coin days destroyed and total transfer volume.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=indicators.AverageDormancy>`_
        """
        pass

    def liveliness(self):
        """
        Liveliness is defined as the ratio of the sum of Coin Days Destroyed and the sum of all coin days ever created.
        Liveliness increases as long term holder liquidate positions and decreases while they accumulate to HODL.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=indicators.Liveliness>`_
        """
        pass

    def relative_unrealized_profit(self):
        """
        Relative Unrealized Profit is defined as the total profit in USD of all coins in existence
        whose price at realisation time was lower than the current price normalised by the market cap.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=indicators.UnrealizedProfit>`_
        """
        pass

    def relative_unrealized_loss(self):
        """
        Relative Unrealized Loss is defined as the total loss in USD of all coins in existence
        whose price at realisation time was higher than the current price normalised by the market cap.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=indicators.UnrealizedLoss>`_
        """
        pass

    def nupl(self):
        """
        Net Unrealized Profit/Loss (NUPL) is the difference between Relative Unrealized Profit/Loss.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=indicators.NetUnrealizedProfitLoss>`_
        """
        pass

    def sth_nupl(self):
        """
        Short Term Holder NUPL (STH-NUPL) is Net Unrealized Profit/Loss that takes into account only UTXOs
        younger than 155 days and serves as an indicator to assess the behaviour of short term investors.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=indicators.NuplLess155>`_
        """
        pass

    def lth_nupl(self):
        """
        Long Term Holder NUPL (LTH-NUPL) is Net Unrealized Profit/Loss that takes into account only UTXOs
        with a lifespan of at least 155 days and serves as an indicator to assess the behaviour of long term investors.
        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=indicators.NuplMore155>`_
        """
        pass

    def ssr(self):
        """
        The Stablecoin Supply Ratio (SSR) is the ratio between Bitcoin supply and the supply of stablecoins denoted
        in BTC, or: Bitcoin Marketcap / Stablecoin Marketcap. We use the following stablecoins for the supply: USDT,
        TUSD, USDC, PAX, GUSD, DAI, SAI, and BUSD. When the SSR is low, the current stablecoin supply has more "buying power"
        to purchase BTC. It serves as a proxy for the supply/demand mechanics between BTC and USD. For more information see
        this article (https://medium.com/@glassnode/stablecoins-buying-power-over-bitcoin-3475c0d8779d).

        `View in Studio <https://studio.glassnode.com/metrics?a=BTC&m=indicators.Ssr>`_
        """
        pass

    def bvin(self):
        """
        The Bitcoin Volatility Index (BVIN) is an implied volatility index that also represents the fair value of a bitcoin variance swap. The index is calculated by CryptoCompare using options data from Deribit and has been developed in collaboration with Carol Alexander and Arben Imeraj at the University of Sussex Business School. The index is suitable for use as a settlement price for bitcoin volatility futures. For more information on the methodology please see Alexander and Imeraj (2020).
        """
        pass
