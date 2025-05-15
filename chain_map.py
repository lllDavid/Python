from collections import ChainMap

defaults = {'theme': 'light', 'language': 'en', 'show_help': True}
user_settings = {'theme': 'dark', 'show_help': False}

config = ChainMap(user_settings, defaults)

print(config['theme'])      
print(config['language'])    
print(config['show_help'])   

print(list(config.keys()))   
print(dict(config))          
