import sys
from utils.conf import TRUST_ZONE_INDEX_NAME
from utils.conf import MARCH_INDEX_URL
from utils.conf import MARCH_INDEX_AUTHORIZATION
from elasticlib.elasticlib import Elasticlib
from utils.queries import get_regon_query



es = Elasticlib(MARCH_INDEX_URL, MARCH_INDEX_AUTHORIZATION)



def get_company_regon(nip):
    """
        get the company through its nip

        :param nip: the nip or official_id
        :type nip: str
    """
    data = es.search(get_regon_query(nip), TRUST_ZONE_INDEX_NAME)
    return data[0]['_source']['REGON']



def update_ui(current_prog):
    """
        print the current progress to the terminal output

        :param current_prog: the current progress to print
        :type current_prog: number
    """
    sys.stdout.write("\r{0}>".format("="*2))
    sys.stdout.write("\033[92m CURRENT PROGRESS: \033[0m")
    sys.stdout.write(" "+str(current_prog))
    sys.stdout.flush()
