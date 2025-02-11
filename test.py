import base64
import json

# 讀取 JSON 文件
with open('myconfig.txt', 'r', encoding="UTF-8") as enc:
    encryptdata=enc.read()
    print(encryptdata)
    decoded_bytes = base64.b64decode(encryptdata)
    decoded_data = json.loads(decoded_bytes.decode('utf-8'))  # 解碼後重新轉換為 JSON
    print("\nDecoded Data:")
    print(decoded_data)