import pandas as pd

with open('yelp_dataset_challenge_round9.json', 'rb') as f:
    data = f.readlines()

data = map(lambda x: x.rstrip(), data)

data_json_str = "[" + ','.join(data) + "]"

data_df = pd.read_json(data_json_str);
