import pandas as pd
import json
df = pd.read_excel('ru.xlsx')
json_data = df.to_json(orient="records", force_ascii=False)
with open("json_ru.json", "w", encoding='utf-8') as json_file:
    json_file.write(json_data)
with open('json_ru.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)
formatted_json = json.dumps(data, ensure_ascii=False, indent=4)
with open('formatted_output.json', 'w', encoding='utf-8') as json_file:
    json_file.write(formatted_json)
