import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Read the data
CSV_FILE_PATH = "./data/train_V2.csv"
data = pd.read_csv(CSV_FILE_PATH)

# ------------------------------------------------------
# -              Basic info of the data                -
# ------------------------------------------------------
# # Check the basic info of training dataset
# data.info()
#
# # Check the missing value of the dataset
# print(data.isnull().sum())
# print(data[data['winPlacePerc'].isnull()])
#
# # Drop row with NaN 'winPlacePerc' value
# data.drop(2744604, inplace=True)
#
# # # Check the first 5 rows
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
# # Collect the type of game less than 1.7 thousand
# Total = 0
# for count in match_types["Count"][6:]:
#     Total += count
# new_rows = ["Others", Total]
# match_types.loc[6] = new_rows
# # print(match_types)
#
# # The plot of match types count
# plt.figure(figsize=(15, 8))
# sns.barplot(x="Type", y="Count", data=match_types[:7])
# plt.title("Match types Counts")
# plt.savefig('./image/Match types Counts.png')
# plt.show()

# ------------------------------------------------------
# -                    DATA Analysis                   -
# ------------------------------------------------------
# # correlation matrix
# plt.subplots(figsize=(15, 15))
# sns.heatmap(data.corr(), square=True, annot=True, fmt='.3f', annot_kws={"size": 8}, cmap="RdBu_r", center=0)
# plt.savefig('./image/correlation matrix.png')
# plt.show()
#

# ------------------------------------------------------
# -                    Funny truth                     -
# ------------------------------------------------------
# print(data['teamKills'].describe())
# print('The maximum of team kills is {number1}.'.format(number1=data['teamKills'].max()))
# print('The average of team kills is {number2}.'.format(number2=data['teamKills'].mean()))
# print('The minimum of team kills is {number3}.'.format(number3=data['teamKills'].min()))
# print("The longest kill distance {}".format(data["longestKill"].max()))
# print("The average kill distance {}".format(data["longestKill"].mean()))
# walk_distance = data.copy()
# walk_distance = walk_distance[walk_distance["kills"] > 0]
# print(len(walk_distance))

# One type of cheater
# Create new col call totalDistance
# new_data = data.copy()
# new_data['totalDistance'] = new_data['rideDistance'] + new_data['walkDistance'] + new_data['swimDistance']
# # Create col call killsWithoutMoving
# new_data['killsWithoutMoving'] = ((new_data['kills'] > 0) & (new_data['totalDistance'] == 0))
# print("The total number of kill without moving is {}"
#       .format(len(new_data[new_data['killsWithoutMoving'] == True])))
#
# sns.distplot(data['winPlacePerc'], kde=False)
# plt.show()

# ------------------------------------------------------
# -                    Kill Analysis                   -
# ------------------------------------------------------
# # Basic info of killer
# data['kills'].describe()
# print("The average of each team kills {:.4f} players, "
#       "99% of people have {} kills, the most kills number is {}."
#       .format(data['kills'].mean(), data['kills'].quantile(0.99), data['kills'].max()))
#
#
# # Plot of kill count
# kill_data = data.copy()
# kill_data.loc[kill_data['kills'] > kill_data['kills'].quantile(0.99)] = '7+'
# sns.countplot(kill_data['kills'].astype('str').sort_values())
# plt.title("Kills Count")
# plt.savefig('./image/kills count.png')
# plt.show()


# # Lucky boy
# kill_data2 = data.copy()
# kill_data2 = kill_data2[kill_data2['kills'] == 0]
# counts = len(kill_data2[kill_data2['winPlacePerc'] == 1])
# per = counts/len(kill_data2)
# print("There are {} players win the chicken without kill anyone, the percentage is {:.4f}% \n "
#       "(Total people who win the game without kill anyone / Total people who kill zero people in the game)"
#       .format(counts, 100*per))

# # Plot of Damage by 0 killers
# plt.figure(figsize=(15, 10))
# plt.title("Damage Dealt by 0 killers")
# sns.displot(kill_data2['damageDealt'])
# plt.show()

# # Plot of kill vs win
# sns.scatterplot(x="winPlacePerc", y="kills", data=data)
# plt.title("Kills Count")
# plt.show()
#
# # Plot of DBNOs vs ratio
# plt.figure(figsize=(15, 5))
# sns.pointplot(x='DBNOs', y='winPlacePerc', data=data, alpha=0.8)
# plt.title('DBNOs / Win Ratio')
# plt.grid()
# plt.show()
#
# # Plot of DBNOs count
# plt.figure(figsize=(15, 8))
# kill_data = data.copy()
# kill_data = kill_data[kill_data['kills'] == 0]
# kill_data.loc[kill_data['DBNOs'] > 7] = '7+'
# sns.countplot(kill_data['DBNOs'].astype('str').sort_values())
# plt.title("DBNOs Count")
# plt.show()

# The plot of damagedealt  vs win ratio
kill_data2 = data.copy()
kill_data2['damageDealt_rank'] = pd.cut(kill_data2['damageDealt'],
                                        [-1, 500, 1000, 1500, 2000, 2500, 60000],
                                        labels=['0-500', '500-1000', '1000-1500',
                                        '1500-2000', '2000-2500', '2500+'])

sns.pointplot(x='damageDealt_rank', y='winPlacePerc', data=kill_data2)
plt.xticks(rotation=45)
plt.title('damageDealt VS. Win Ratio')
plt.show()

# ------------------------------------------------------
# -                    Run Analysis                    -
# ------------------------------------------------------
# Basic info of runner

# Some facts about walking distance
# print(data['walkDistance'].describe())
#
# print("The average of each team walk for {:.2f} m, "
#       "99% of people have walk {} m, the most walking distance is {}m."
#       .format(data['walkDistance'].mean(), data['walkDistance'].quantile(0.99), data['walkDistance'].max()))
#
# # The plot of the distribution of walking
# walk_data = data.copy()
# walk_data = walk_data[walk_data['walkDistance'] < data['walkDistance'].quantile(0.99)]
# plt.title("Walking Distance Distribution")
# sns.distplot(walk_data['walkDistance'], kde=False)
# plt.show()
#
#
# # Plot of walk vs win
# sns.scatterplot(x="winPlacePerc", y="walkDistance", data=data)
# plt.title("walkDistance Count")
# plt.show()


# ------------------------------------------------------
# -                    Drive Analysis                  -
# ------------------------------------------------------
# print(data['rideDistance'].describe())
#
# print("The average of each team drive for {:.2f} m, "
#       "99% of people have drive {} m, the most driving distance is {}m."
#       .format(data['rideDistance'].mean(), data['rideDistance'].quantile(0.99), data['rideDistance'].max()))
#
# # The plot of the distribution of driving
# drive_data = data.copy()
# drive_data = drive_data[drive_data['rideDistance'] < data['rideDistance'].quantile(0.99)]
# plt.title("Drive Distance Distribution")
# sns.distplot(drive_data['rideDistance'], kde=False)
# plt.show()
#
#
# # Plot of drive vs win
# sns.scatterplot(x="winPlacePerc", y="rideDistance", data=data)
# plt.title("rideDistance Count")
# plt.show()
