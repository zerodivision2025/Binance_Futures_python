import json
import logging
import json.decoder
from binance_d.impl.utils.jsonwrapper import JsonWrapper


def parse_json_from_string(value):
    value = value.replace("False", "false")
    value = value.replace("True", "true")
    try:
        return JsonWrapper(json.loads(value))
    except json.decoder.JSONDecodeError:
        msg = f"json decode value failed: {value}"
        logging.info(msg)
        raise ValueError(msg)
