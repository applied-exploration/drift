#%%
class FullyConnectedModule(nn.Module):
    def __init__(
        self, input_size: int, output_size: int, hidden_size: int, n_hidden_layers: int
    ):
        """No docstring here yet."""
        pass

    def forward(self, x: torch.Tensor):
        """No docstring here yet."""
        pass


#%%
class FullyConnectedModel(BaseModel):
    def __init__(
        self,
        input_size: int,
        output_size: int,
        hidden_size: int,
        n_hidden_layers: int,
        **kwargs
    ):
        """No docstring here yet."""
        pass

    def forward(self, x: Dict[str, torch.Tensor]):
        """No docstring here yet."""
        pass

    def from_dataset(cls, dataset: TimeSeriesDataSet, **kwargs):
        """No docstring here yet."""
        pass

    def calculate_prediction_actual_by_variable(x, train):
        """No docstring here yet."""
        pass


def create_FullyConnectedModel(training_dataset, kwargs):
    """No docstring here yet."""
    pass
