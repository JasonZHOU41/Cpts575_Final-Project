import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Read the data
CSV_FILE_PATH = "./data/train_V2.csv"
data = pd.read_csv(CSV_FILE_PATH)

# Basic info of the data
# Check the basic info of training dataset
data.info()

# Check the first 5 rows
# print(data.head(5))

# Some information of the game
Group = ['Id', 'groupId', 'matchId']
for item in Group:
    print('unique [{}] count {}:'.format(item, data[item].nunique()))

match_types = data.loc[:, "matchType"].value_counts().to_frame().reset_index()
match_types.columns = ["Type", "Count"]
print(match_types)
Total = 0
for count in match_types["Count"][6:]:
    Total += count
new_rows = ["Others", Total]
match_types.loc[6] = new_rows
print(match_types)

# The plot of match types count
plt.figure(figsize=(15, 8))
sns.barplot(x="Type", y="Count", data=match_types[:7])
plt.title("Match types Counts")
plt.savefig('./image/Match types Counts.png')
plt.show()


# Data Analysis
# correlation matrix
plt.subplots(figsize=(15, 15))
sns.heatmap(data.corr(), square=True, annot=True, fmt='.3f', annot_kws={"size": 8}, cmap="RdBu_r", center=0)
plt.savefig('./image/correlation matrix.png')
plt.show()

# funny explore
print(data['teamKills'].describe())
print('The maximum of team kills is {number1}.'.format(number1=data['teamKills'].max()))
print('The minimum of team kills is {number2}.'.format(number2=data['teamKills'].min()))

# killer analysis
# Basic info of killer
print("The average kills {:.4f} players, "
      "99% of people have {} kills, the most kills number is {}."
      .format(data['kills'].mean(), data['kills'].quantile(0.99), data['kills'].max()))


# Plot of kill count
kill_data = data.copy()
kill_data.loc[kill_data['kills'] > kill_data['kills'].quantile(0.99)] = '7+'
sns.countplot(kill_data['kills'].astype('str').sort_values())
plt.title("Kills Count")
plt.savefig('./image/kills count.png')
plt.show()

