import configparser

parser = configparser.ConfigParser()
parser.read("conf.ini")
print(parser.get("config", "option3"))