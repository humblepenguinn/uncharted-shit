# import pandas as pd


# df = pd.read_csv("data-nodup.csv", usecols = ['HC ID'])
# #print(df['HC ID'].to_list())

# for i in df['HC ID'].to_list():
#     print(i)
import pandas as pd


df_state=pd.read_csv("data.csv")

Dup_Rows = df_state[df_state.duplicated()]

print("\n\nDuplicate Rows : \n {}".format(Dup_Rows))
