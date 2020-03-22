

class Config:

    FILEPATH_CONFIG = "config/config.txt"
    config = {}

    @staticmethod
    def initialize():
        Config.read()

    @staticmethod
    def get_key(key):
        if key not in Config.config:
            raise Exception('Key doesn\'t exist for config ' + key)

        return Config.config[key]

    @staticmethod
    def get_config():
        return Config.config

    @staticmethod
    def read():
        with open(Config.FILEPATH_CONFIG) as f:
            for line in f:
                line = line.strip()

                if len(line) == 0:
                    continue

                parts = line.split('=')

                if len(parts) != 2:
                    raise Exception("Bad config values")

                Config.config[parts[0]] = parts[1]
