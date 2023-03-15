# import itertools

from elasticlib.elasticlib import Elasticlib
import utils.conf as conf
import explorer
import json
import sys

es = Elasticlib(conf.MARCH_INDEX_URL, conf.MARCH_INDEX_AUTHORIZATION)

query = {
    "query": {
        "bool": {
            "must": [
                {
                    "term": {
                        "discovery_status": {
                            "value": "processed_not_added"
                        }
                    }
                },
                {
                    "term": {
                        "official_country": {
                            "value": "PL"
                        }
                    }
                }
            ],
            "filter": {
                "script": {
                    "script": """
                        return doc['official_id'].value.length() > 9;
                    """
                }
            }
        }
    }
}

current_prog = 0
for doc in es.next_scroll(query, conf.MARCH_INDEX_NAME, scroll_time="10m", timeout=30):  # 22m
    sys.stdout.write("\r{0}>".format("="*2))
    sys.stdout.write("\033[92m CURRENT PROGRESS: \033[0m")
    sys.stdout.write(" "+str(current_prog)+"/316")
    sys.stdout.flush()
    for data in doc:
        payload_size = 0
        payload = ""
        # get company id in this case (>9) NIP
        nip = data['_source']['official_id'][0]
        id = data['_id']
        # search for it in aleo_raw_zone & get REGON
        regon = explorer.get_company_regon(nip)
        # if found: add it to payload
        if regon is not None:
            p = json.dumps({"update": {"_index": conf.MARCH_INDEX_NAME, "_id": id}}) + \
                "\n" + json.dumps({"doc": {"official_id": [regon]}}) + "\n"
            payload += p
            payload_size += 1
        # if payload has enough
        if payload_size > conf.REQUEST_SIZE:
            r = es.bulk_update(payload)
    current_prog += 1
print("\n")
