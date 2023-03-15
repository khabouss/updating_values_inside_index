def get_scroll_query():
    """
        return the scroll query
    """
    return {
        "size": 10000,
        "_source": ["official_id"],
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


def get_regon_query(nip):
    """
        return the regon query
    """
    return {
        "_source": ["REGON"],
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
