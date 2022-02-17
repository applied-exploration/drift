# RawConfig is needed to ensure we can declare config presets here with static typing, we then convert it to Config
class RawConfig(BaseModel):
    pass


@dataclass
class Config:
    def check_model(cls, v):
        """No docstring here yet."""
        pass

    def check_event_filter(cls, v):
        """No docstring here yet."""
        pass

    def check_labeling(cls, v):
        """No docstring here yet."""
        pass
