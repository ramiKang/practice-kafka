import pandas as pd

DATA_ROOT_PATH = "./data"
csv_path = f"{DATA_ROOT_PATH}/shop_clothing_2008.csv"
json_path = f"{DATA_ROOT_PATH}/shop_clothing_2008.json"

data = pd.read_csv(csv_path, delimiter=';')

data.to_json(json_path, orient='records', lines=True)

print("csv 저장 완료")
