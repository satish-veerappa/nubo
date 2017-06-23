import ConfigParser

Config = ConfigParser.ConfigParser()
Config.read('my.config')
section_list = Config.sections()
print section_list

for section in section_list:
        if section == "Frameworks":
                print "Section is",section

