for index, section_name in enumerate(sections[framework_start_index:]):
             output = util.ConfigSectionMap(Config,section_name)
             username = output['username'].decode('base64').strip()
             password = output['password'].decode('base64').strip()
