import utils.explorer_conf as explorer_conf
import utils.conf as conf
from elasticlib.elasticlib import Elasticlib
import utils.queries as queries

es = Elasticlib(conf.MARCH_INDEX_URL, conf.MARCH_INDEX_AUTHORIZATION)

def get_company_regon(nip):
    data = es.search(queries.get_regon_query(nip), explorer_conf.MARCH_INDEX_NAME)
    return data[0]['_source']['REGON']
