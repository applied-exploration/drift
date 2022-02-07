@dataclass
class TrainingOutcome:
    pass


@dataclass
class EnsembleOutcome:
    pass


@dataclass
class BetSizingWithMetaOutcome:
    pass


@dataclass
class DirectionalTrainingOutcome:
    pass


@dataclass
class PipelineOutcome:
    def get_output_weights(self):
        """No docstring here yet."""
        pass

    def get_output_stats(self):
        """No docstring here yet."""
        pass
