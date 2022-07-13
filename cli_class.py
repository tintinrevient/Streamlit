from jsonargparse import CLI
from dataset import Dataset
from model import Model


def train(dataset: Dataset, model: Model):
    """Trains a model on the given dataset.

    Args:
        dataset: Image dataset
        model: Neural network
    """
    print(f"Train using:")
    print(f"  {dataset}")
    print(f"  {model}")


if __name__ == '__main__':
    CLI(as_positional=False)

    # python cli_class.py --help

    # python cli_class.py --dataset ImageNetDataset --model ConvNet --print_config
    # python cli_class.py --dataset ImageNetDataset --model ConvNet --print_config > config/all.yaml

    # python cli_class.py --config config/all.yaml
    # python cli_class.py --dataset config/dataset.yaml --model config/model.yaml
    # python cli_class.py --config config/all_subconfig.yaml
