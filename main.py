from elasticlib.elasticlib import Elasticlib
from utils.conf import MARCH_INDEX_URL
from utils.conf import MARCH_INDEX_AUTHORIZATION
from utils.conf import MARCH_INDEX_NAME
from utils.conf import REQUEST_SIZE
from utils.conf import DISCOVERY_VALID
from utils.queries import get_scroll_query
from helpers import get_company_regon
from helpers import update_ui
import json

def main():
    es = Elasticlib(MARCH_INDEX_URL, MARCH_INDEX_AUTHORIZATION)

    current_prog = 0
    payload_size = 0
    search_payload = get_scroll_query()
    for doc in es.next_scroll(search_payload, MARCH_INDEX_NAME, scroll_time="10m", timeout=30):
        update_ui(current_prog)
        for data in doc:
            payload = ""
            # get company id in this case (>9) NIP
            nip = data['_source']['official_id'][0]
            id = data['_id']
            # search for it in aleo_raw_zone & get REGON
            regon = get_company_regon(nip)
            # if found: add it to payload
            if regon is not None:
                payload += json.dumps({"update": {"_index": MARCH_INDEX_NAME, "_id": id}}) + \
                    "\n" + json.dumps({"doc": {"official_id": [regon], "discovery_status": DISCOVERY_VALID}}) + "\n"
                payload_size += 1
            # if payload has enough
            if payload_size > REQUEST_SIZE:
                es.bulk_update(payload)
                payload=""
        es.bulk_update(payload)
        current_prog += 1
    print("\n   Done")

if __name__ == "__main__":
    main()