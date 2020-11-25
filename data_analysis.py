import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Read the data
CSV_FILE_PATH = "./data/train_V2.csv"
data = pd.read_csv(CSV_FILE_PATH)

# # Basic info of the data
# # Check the basic info of training dataset
# data.info()
#
# # Check the first 5 rows
# # print(data.head(5))
#
# # Some information of the game
# Group = ['Id', 'groupId', 'matchId']
# for item in Group:
#     print('unique [{}] count {}:'.format(item, data[item].nunique()))
#
# match_types = data.loc[:, "matchType"].value_counts().to_frame().reset_index()
# match_types.columns = ["Type", "Count"]
# print(match_types)
# Total = 0
# for count in match_types["Count"][6:]:
#     Total += count
# new_rows = ["Others", Total]
# match_types.loc[6] = new_rows
# print(match_types)
#
# # The plot of match types count
# plt.figure(figsize=(15, 8))
# sns.barplot(x="Type", y="Count", data=match_types[:7])
# plt.title("Match types Counts")
# plt.savefig('./image/Match types Counts.png')
# plt.show()


# # Data Analysis
# # correlation matrix
# plt.subplots(figsize=(15, 15))
# sns.heatmap(data.corr(), square=True, annot=True, fmt='.3f', annot_kws={"size": 8}, cmap="RdBu_r", center=0)
# plt.savefig('./image/correlation matrix.png')
# plt.show()
#
# # funny explore
# print(data['teamKills'].describe())
# print('The maximum of team kills is {number1}.'.format(number1=data['teamKills'].max()))
# print('The minimum of team kills is {number2}.'.format(number2=data['teamKills'].min()))
# print("The longest kill distance {}".format(data["longestKill"].max()))
# print("The average kill distance {}".format(data["longestKill"].mean()))
# walk_distance = data.copy()
# walk_distance = walk_distance[walk_distance["kills"] > 0]
# print(len(walk_distance))

# kill analysis
# Basic info of killer
print("The average of each team kills {:.4f} players, "
      "99% of people have {} kills, the most kills number is {}."
      .format(data['kills'].mean(), data['kills'].quantile(0.99), data['kills'].max()))


# Plot of kill count
kill_data = data.copy()
kill_data.loc[kill_data['kills'] > kill_data['kills'].quantile(0.99)] = '7+'
sns.countplot(kill_data['kills'].astype('str').sort_values())
plt.title("Kills Count")
plt.savefig('./image/kills count.png')
plt.show()


# # Lucky boy
# kill_data2 = data.copy()
# kill_data2 = kill_data2[kill_data2['kills'] == 0]
# counts = len(kill_data2[kill_data2['winPlacePerc'] == 1])
# per = counts/len(kill_data2)
# print("There are {} players win the chicken without kill anyone, the percentage is {:.4f}% \n "
#       "(Total people who win the game without kill anyone / Total people who kill zero people in the game)"
#       .format(counts, 100*per))

# plt.title("Damage Dealt by 0 killers")
# sns.countplot(data['winPlacePerc'])
# plt.show()

# # Plot of kill vs win
# sns.scatterplot(x="winPlacePerc", y="kills", data=data)
# plt.title("Kills Count")
# plt.show()

# # Plot of DBNOs count
# plt.figure(figsize=(15, 8))
# kill_data = data.copy()
# kill_data = kill_data[kill_data['kills'] == 0]
# kill_data.loc[kill_data['DBNOs'] > 7] = '7+'
# sns.countplot(kill_data['DBNOs'].astype('str').sort_values())
# plt.title("DBNOs Count")
# plt.show()
