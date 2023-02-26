import pandas as pd

ori = pd.read_csv("label_30s_5.csv")["label"]
test = pd.read_csv("label_30s_5_test.csv")["label"]
for x in range(len(ori)):
    if ori[x]!=test[x]:
        print("false")
