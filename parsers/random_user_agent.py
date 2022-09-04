import json
import random
from pathlib import Path


def rand():
    path = Path(__file__).with_name("user_agents.json")
    with open(path) as f:
        agents = json.loads(f.read())
        return random.choice(agents['agents'])
