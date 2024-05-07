import os
import tomlkit

defaultConfig = R"""
[deepl]
apikey = ""
"""
#[danbooru]
#apikey = "" # optional

configFile = "config.toml"

def loadConfig():
    if os.path.exists(configFile):
        # Load configFile with TOMLKit
        with open(configFile, "r") as file:
            config = tomlkit.parse(file.read())
    else:
        # Parse defaultConfig with TOMLKit and write config.toml
        print("Created default config file. Please modify this to enable DeepL translations.")
        config = tomlkit.parse(defaultConfig)
        with open(configFile, "w") as file:
            file.write(tomlkit.dumps(config))
    
    return config

config = loadConfig()