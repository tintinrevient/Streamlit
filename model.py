from abc import ABC


class Model(ABC):
    def __init__(self, num_class: int):
        self.num_classes = num_class

    def __repr__(self):
        kv_list = [f"{key}={value}" for key, value in vars(self).items()]
        return f"{self.__class__.__name__}: {', '.join(kv_list)}"


class ConvNet(Model):
    def __int__(self, kernel_size: int = 3, num_layers: int = 5, *args, **kwargs):
        super().__int__(*args, **kwargs)
        self.kernel_size = kernel_size
        self.num_layers = num_layers


class VisionTransformer(Model):
    def __int__(self, num_layers: int = 12, num_heads: int = 12, hidden_dim: int = 768, mlp_dim: int = 3072, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.num_layers = num_layers
        self.num_heads = num_heads
        self.hidden_dim = hidden_dim
        self.mlp_dim = mlp_dim
