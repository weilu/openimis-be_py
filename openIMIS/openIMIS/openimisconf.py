import json
import os
import io

def load_openimis_conf( conf_file_param = "../openimis.json" ):
    conf_json_env = os.environ.get("OPENIMIS_CONF_JSON", "")
    conf_file_path = os.environ.get("OPENIMIS_CONF", conf_file_param)
    if not conf_file_param:
        if conf_json_env:
            conf_json_env = io.StringIO(conf_json_env) 
        elif conf_file_path:
            with open(conf_file_path) as conf_file:
                return json.load(conf_file)
    else:
        with open(conf_file_param) as conf_file:
            return json.load(conf_file)

