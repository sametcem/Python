import pandas as pd

soccer = pd.read_csv("mls-salaries-2017.csv.csv")
print(soccer.head(10))
print(len(soccer.index))

avg_sal = soccer["base_salary"].mean()
print(avg_sal)

max_sal = soccer["base_salary"].max()
print(max_sal)

max_gcompen = soccer["guaranteed_compensation"].max()
print(max_gcompen)

player = soccer[soccer["guaranteed_compensation"] == soccer["guaranteed_compensation"].max()]["last_name"].iloc[0]
print(player)

# Gonzalez Pirez position
gonzalo = soccer[soccer["last_name"] == "Gonzalez Pirez"]["position"].iloc[0]
print(gonzalo)

# Avg sals for positions
avgp = soccer.groupby("position").mean()
print(avgp)

# How many positions are there?
pss  = soccer["position"].nunique()
print(pss)

# Hangi mevkide kaç kişi?
pssv = soccer["position"].value_counts()
print(pssv)

print(soccer["club"].value_counts())

def son_find(last_name):
    if "son" in last_name.lower():
        return True
    return False

# Name ends with "son"
son_player = soccer[soccer["last_name"].apply(son_find)]
print(son_player)

