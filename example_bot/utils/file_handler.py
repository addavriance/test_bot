import json
import os
from typing import Any


def get_data(file: str) -> Any:
    dirname = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(dirname, file)
    with open(f'{filepath}.json', 'r') as f:
        return json.load(f)


def update_data(file: str, data: Any) -> None:
    dirname = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(dirname, file)
    with open(f'{filepath}.json', 'w') as f:
        json.dump(data, f)
