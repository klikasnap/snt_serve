from os import environ, getenv

import yaml

from .utils import dnrp

# Constants
with open(os.path.join(()"api/constants.yml")) as f:
    CONSTANTS_YML = yaml.safe_load(f)

# Environment
if getenv("ENV", "production") == "development":
    from dotenv import load_dotenv

    load_dotenv(".env")
ENVIRON = environ
