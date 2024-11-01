import os 


OPENSEARCH_HOST = os.environ.get("OPENSEARCH_HOST", "0.0.0.0")
OPEN_SEARCH_HTTP_PORT = os.environ.get("OPEN_SEARCH_HTTP_PORT", "9200")
OPENSEARCH_DSL_AUTOSYNC = os.environ.get('OPENSEARCH_DSL_AUTOSYNC', 'True') == 'True' 

OPENSEARCH_DSL = {
    'default': {
        'hosts': f"{OPENSEARCH_HOST}:{OPEN_SEARCH_HTTP_PORT}",
        'http_auth': (
            f"{os.environ.get('OPENSEARCH_ADMIN')}",
            f"{os.environ.get('OPENSEARCH_PASSWORD')}"
        ),
        'timeout': 120,
    }
}
