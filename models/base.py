class Model(ABC):
    def fit(self, X: np.ndarray, y: np.ndarray):
        """No docstring here yet."""
        pass

    def predict(self, X: np.ndarray):
        """No docstring here yet."""
        pass

    def clone(self):
        """No docstring here yet."""
        pass

    def initialize_network(self, input_dim: int, output_dim: int):
        """No docstring here yet."""
        pass
