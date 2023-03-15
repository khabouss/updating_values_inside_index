import base64
from dotenv import load_dotenv
import os
from colorama import Fore

load_dotenv()

REQUEST_SIZE = 10
MARCH_USER=os.getenv('MARCH_USER')
MARCH_PASSWORD=os.getenv('MARCH_PASSWORD')
if MARCH_USER is None or MARCH_PASSWORD is None:
    print(Fore.RED + "Add Credentials to .env file or directly to conf.py"+ Fore.RESET)
    exit(1)
MARCH_INDEX_URL="http://172.16.84.68:9200"
MARCH_INDEX_NAME="march_bot_dev"
p = f"{MARCH_USER}:{MARCH_PASSWORD}".encode()
MARCH_INDEX_AUTHORIZATION=f"Basic { base64.b64encode(p).decode() }"
TRUST_ZONE_INDEX_NAME="aleo_raw_zone"
DISCOVERY_VALID="valid"