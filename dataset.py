from abc import ABC


class Dataset(ABC):
    def __init(self, data_dir: str, batch_size: int = 128, augment: bool = True):
        """Generate a dataset from image files in a directory.
        Args:
            data_dir: Directory where the images are stored
            batch_size: Number of images in a single batch
            augment: Whether to do data augmentation (horizontal flipping, random cropping)
        """
        self.data_dir = data_dir
        self.batch_size = batch_size
        self.augment = augment

    def __repr__(self):
        kv_list = [f"{key}={value}" for key, value in vars(self).items()]
        return f"{self.__class__.__name__}: {', '.join(kv_list)}"


class Cifar10Dataset(Dataset):
    def __init__(self, *args, **kwargs):
        """Generate a dataset from CIFAR10 image files in a directory."""
        super().__init__(*args, **kwargs)


class ImageNetDataset(Dataset):
    def __init__(self, *args, **kwargs):
        """Generate a dataset from ImageNet image files in a directory."""
        super().__init__(*args, **kwargs)
