# create lists of categorical and numerical variables
# be aware of numerical data that is actually categorical (like yes/no 1/0)

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
_________________________________________________________________________________
# define function to call hisogram & boxplots
def box_histo(data, feature, figsize = (12, 7), kde = False, bins = None):

    f2, (ax_box2, ax_hist2) = plt.subplots(
        nrows = 2,      # set number of rows
        sharex = True,  # share x-axis for both plots
        gridspec_kw = {"height_ratios": (0.25, 0.75)},
        figsize = figsize,
    )                   

    # box and histo plots
    sns.boxplot(
        data = data, x = feature, ax = ax_box2, showmeans = True, color = "violet"
    )                  
    sns.histplot(
        data = data, x = feature, kde = kde, ax = ax_hist2, bins = bins, palette = "winter"
    ) if bins else sns.histplot(
        data = data, x = feature, kde = kde, ax = ax_hist2
    )                  

    # set average lines
    ax_hist2.axvline(
        data[feature].mean(), color = "green", linestyle = "--"
    )                   
    ax_hist2.axvline(
        data[feature].median(), color = "black", linestyle = "-"
    )                  

_________________

# create histograms of all numerical columns (define num_cols first)
df[num_cols].hist(figsize = (14, 14))

plt.show()
