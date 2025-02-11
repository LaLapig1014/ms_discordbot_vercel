import os
import json
import base64
import tempfile
def base64convert():
  with open('myconfig.txt', 'r', encoding="UTF-8") as enc:
        encryptdata = enc.read()
        decoded_bytes = base64.b64decode(encryptdata)
        decoded_data = json.loads(decoded_bytes.decode('utf-8'))  # 轉回 JSON
    
  temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".json")
  with open(temp_file.name, "w", encoding="utf-8") as f:
      json.dump(decoded_data, f)
    
  return temp_file.name # 將 JSON 寫入臨時文件

# Load configs for local hosting
path = 'myconfig.json'
if os.path.isfile(base64convert()): # <-- file won't exist in production
  with open(path) as f: 
    config = json.loads(f.read())
  for key, value in config.items():
    os.environ[key] = value
  os.environ['test'] = '1'
  print('Using test bot configs!')


from src.bot import run

print("""
  ____            _      ____        _   _ 
 |  _ \          (_)    |  _ \      | | | |
 | |_) | __ _ ___ _  ___| |_) | ___ | |_| |
 |  _ < / _` / __| |/ __|  _ < / _ \| __| |
 | |_) | (_| \__ \ | (__| |_) | (_) | |_|_|
 |____/ \__,_|___/_|\___|____/ \___/ \__(_)                                                                                                         
""")

# Run the bot
app = run()