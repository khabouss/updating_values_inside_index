import utils.explorer_conf as explorer_conf
import utils.conf as conf
from elasticlib.elasticlib import Elasticlib

es = Elasticlib(conf.MARCH_INDEX_URL, conf.MARCH_INDEX_AUTHORIZATION)

def get_company_regon(nip):
    query = {
        "query": {
            "bool": {
                "must": {
                    "term": {
                        "NIP": {
                            "value": nip
                        }
                    }
                }
            }
        }
    }
    return es.search(query, explorer_conf.MARCH_INDEX_NAME)[0]['_source']['REGON']
