class ETH2:
    def __init__(self, glassnode_client):
        """No docstring here yet."""
        pass

    def new_deposits(self):
        """
        The number transactions depositing 32 ETH to the ETH2 deposit contract.
        `View in Studio <https://studio.glassnode.com/metrics?a=ETH&m=eth2.StakingDepositsCount>`_

        :return: A DataFrame with ETH2 deposit data.
        :rtype: DataFrame
        """
        pass

    def new_value_staked(self):
        """
        The amount of ETH transferred to the ETH2 deposit contract.
        `View in Studio <https://studio.glassnode.com/metrics?a=ETH&m=eth2.StakingVolumeSum>`_

        :return: A DataFrame with staked value data.
        :rtype: DataFrame
        """
        pass

    def new_validators(self):
        """
        The number of new validators (accounts) depositing 32 ETH to the ETH2 deposit contract.
        `View in Studio <https://studio.glassnode.com/metrics?a=ETH&m=eth2.StakingValidatorsCount>`_

        :return: A DataFrame with new validators data.
        :rtype: DataFrame
        """
        pass

    def total_number_of_deposits(self):
        """
        The total number of transactions to the ETH2 deposit contract.
        `View in Studio <https://studio.glassnode.com/metrics?a=ETH&m=eth2.StakingTotalDepositsCount>`_

        :return: A DataFrame with ETH2 deposit data.
        :rtype: DataFrame
        """
        pass

    def total_value_staked(self):
        """
        The amount of ETH that has been deposited to the ETH2 deposit contract,
        the current ETH balance on the ETH2 deposit contract.
        `View in Studio <https://studio.glassnode.com/metrics?a=ETH&m=eth2.StakingTotalVolumeSum>`_

        :return: A DataFrame with ETH2 deposit data.
        :rtype: DataFrame
        """
        pass

    def total_number_of_validators(self):
        """
        The total number of unique validators (accounts) that have deposited 32 ETH to the ETH2 deposit contract.
        `View in Studio <https://studio.glassnode.com/metrics?a=ETH&m=eth2.StakingTotalValidatorsCount>`_

        :return: A DataFrame with ETH2 deposit data.
        :rtype: DataFrame
        """
        pass

    def phase_zero_staking_goal(self):
        """
        The percentage of the Phase 0 staking goal.
        `View in Studio <https://studio.glassnode.com/metrics?a=ETH&m=eth2.StakingPhase0GoalPercent>`_

        :return: A DataFrame with staking goal data.
        :rtype: DataFrame
        """
        pass
