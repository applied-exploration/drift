class Model(ABC):
    def fit(self, X: np.ndarray, y: np.ndarray):
        """No docstring here yet."""
        pass

    def predict(self, X: np.ndarray):
        """No docstring here yet."""
        pass

    def predict_proba(self, X: np.ndarray):
        """No docstring here yet."""
        pass
