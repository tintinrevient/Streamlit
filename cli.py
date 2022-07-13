from jsonargparse import CLI


def main(name: str, year: int = 2022):
    """Print the basic info
    Args:
        name: Name of the conference
        year: Year of the conference
    """
    print(f"{name} {year} is the best!")


if __name__  == '__main__':
    CLI(env_prefix='PYCON', default_env=True)

    # python cli.py PYCON --year 2020
    # python cli.py --print_config > config/config.yaml
    # python cli.py --config config/config.yaml
    # PYCON_NAME=PYCON PYCON_YEAR=2024 python cli.py
    