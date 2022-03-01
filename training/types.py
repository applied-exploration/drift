@dataclass
class TrainingOutcomeWithoutTransformations:
    pass


@dataclass
class TrainingOutcome(TrainingOutcomeWithoutTransformations):
    pass


@dataclass
class BetSizingWithMetaOutcome:
    pass


@dataclass
class PipelineOutcome:
    def get_output_weights(self):
        """No docstring here yet."""
        pass

    def get_output_stats(self):
        """No docstring here yet."""
        pass
