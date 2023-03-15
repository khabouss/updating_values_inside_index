from elasticlib.elasticlib import Elasticlib
import utils.conf as conf
import explorer
import json
import utils.queries as queries
import helpers

es = Elasticlib(conf.MARCH_INDEX_URL, conf.MARCH_INDEX_AUTHORIZATION)

current_prog = 0
for doc in es.next_scroll(queries.get_scroll_query(), conf.MARCH_INDEX_NAME, scroll_time="10m", timeout=30):  # 22m
    helpers.update_ui(current_prog)
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

print("\n   Done")
