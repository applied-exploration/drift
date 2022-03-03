@dataclass
class BaseTrainingOutcome:
    pass


@dataclass
class TrainingOutcome(BaseTrainingOutcome):
    pass


@dataclass
class BetSizingWithMetaOutcome(TrainingOutcome):
    pass


@dataclass
class PipelineOutcome:
    def get_output_weights(self):
        """No docstring here yet."""
        pass

    def get_output_stats(self):
        """No docstring here yet."""
        pass
