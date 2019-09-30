import numpy as np
import pandas as pd
from pandas import Series,DataFrame
import json
from pandas.io.json import json_normalize

with open('posts_and_comments-su.json', 'r') as f:
    fbdata = json.load(f)

message = json_normalize(data = fbdata["reactions"],record_path = "data" ,
                          meta = ["title"])

diff_emo = message["reaction.reaction"].unique()

dtframe = message.groupby("reaction.reaction").count()