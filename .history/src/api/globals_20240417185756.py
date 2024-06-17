from os import environ, getenv

import yaml
from deta import Deta

# Constants
with open("api/constants.yml", "r") as f:
    CONSTANTS_YML = yaml.safe_load(f)

# Environment
if getenv("ENV", "production") == "development":
    from dotenv import load_dotenv

    load_dotenv(".env")
ENVIRON = environ
