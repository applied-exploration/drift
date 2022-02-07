class MultiLayerPerceptron(pl.LightningModule):
    def __init__(
        self,
        hidden_layers_ratio: list[float] = [2.0, 2.0],
        probabilities: bool = False,
        loss_function=F.mse_loss,
    ):
        """No docstring here yet."""
        pass

    def initialize_network(self, input_dim: int, output_dim: int):
        """No docstring here yet."""
        pass

    def forward(self, x: torch.Tensor):
        """No docstring here yet."""
        pass

    def training_step(self, batch: torch.Tensor, batch_idx):
        """No docstring here yet."""
        pass

    def configure_optimizers(self):
        """No docstring here yet."""
        pass
