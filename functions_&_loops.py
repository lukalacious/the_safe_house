# create lists of categorical and numerical variables

# import data
df = pd.read_csv("data.csv")

# set data types
df_dtypes = pd.DataFrame(df.dtypes, columns=['data_type']).reset_index(names='variable')

# set lists
num_cols2 = []
cat_cols2 = []

# create loop
for index, row in df_dtypes.iterrows():
  variable = row['variable']
  if row.data_type == 'int64':
    num_cols2.append(variable)
  else:
    cat_cols2.append(variable)

print(num_cols2)
print(cat_cols2)
