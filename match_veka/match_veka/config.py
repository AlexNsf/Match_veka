# -*- coding: utf-8 -*-
import json
import os

CUR_PATH = os.path.dirname(os.path.abspath(__file__))

GLOBAL_CONFIG_FILE = CUR_PATH + "/configs/config.json"


def load_config(filename):
    with open(filename, "r", encoding="utf-8") as configfile:
        res = json.loads(configfile.read())
        return res


PARAMS = load_config(GLOBAL_CONFIG_FILE)
SECRET = load_config(CUR_PATH + "/" + PARAMS["config_secret_path"])
