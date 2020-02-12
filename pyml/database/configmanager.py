import os
from configparser import SafeConfigParser

def config(filename='database.ini', section='postgresql'):
    filepath = os.path.dirname(os.path.realpath(__file__)) + "/" + filename
    if os.path.isfile(filepath):
        parser = SafeConfigParser()
        parser.read(filepath)

        db = {}
        if parser.has_section(section):
            params = parser.items(section)
            for param in params:
                db[param[0]] = param[1]
        else:
            raise Exception('Section {0} not found in the {1} file'.format(section, filepath))
        return db
    else:
        raise Exception("Could not find {0} file".format(filepath))
