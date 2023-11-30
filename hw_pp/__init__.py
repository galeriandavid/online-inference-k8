from ruamel.yaml import YAML

config_file = "params.yaml"

with open(config_file, encoding="utf-8") as f:
    yaml = YAML(typ="safe")
    PARAMS = yaml.load(f)