import json
from utils import log_step

@log_step
def save_to_json(data, filename):
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)
