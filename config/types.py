# RawConfig is needed to ensure we can declare config presets here with static typing, we then convert it to Config
class RawConfig(BaseModel):
    pass


class Config(BaseModel):
    pass
