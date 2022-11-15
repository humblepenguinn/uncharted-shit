import random
import pandas as pd

def remove_dup(csv_file, output_file):
    df = pd.read_csv(csv_file, sep="\t or ,")

    df.drop_duplicates(subset=None, inplace=True)
    df.to_csv(output_file, index=False)

def listToString(s):
    str1 = ""

    for indx, ele in enumerate(s, start=1):
        if not (indx == len(s)):
            str1 += str(ele) + ','
        else:
            str1 += str(ele)

    return str1

def generate_random_path(MAX=15):
    path = [i for i in range(1, MAX+1)]

    random.shuffle(path)

    return listToString(path)


