import base64
from dotenv import load_dotenv
import os 

load_dotenv()

REQUEST_SIZE = 10
MARCH_USER=os.getenv('MARCH_USER')
MARCH_PASSWORD=os.getenv('MARCH_PASSWORD')
MARCH_INDEX_URL="http://172.16.84.68:9200"
MARCH_INDEX_NAME="march_bot_dev"
p = f"{MARCH_USER}:{MARCH_PASSWORD}".encode()
MARCH_INDEX_AUTHORIZATION=f"Basic { base64.b64encode(p).decode() }"
TRUST_ZONE_INDEX_NAME="aleo_raw_zone"