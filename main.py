import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
def age_group(age: int):
    if age == 18:
        return "18"
    elif 18 > age and age <= 24:
        return "18-24"
    elif 25 >= age and age <= 34:
        return "25-34"
    elif 35 >= age and age <= 44:
        return "35-44"
    elif 45 >= age and age <= 54:
        return "45-54"
    elif 55 >= age and age <= 64:
        return "55-64"
    elif age >= 65:
        return "65+"
    return None;

data = pd.read_csv("dateset/nyt/nyt1.csv")
data_filter_noNullAge = data[data.Age > 0]
data_filter_noNullAge.insert(1, "AG", [age_group(age) for age in data_filter_noNullAge.Age.to_list()])
data_by_gender_age = data_filter_noNullAge.groupby(["AG", "Gender"],as_index=False).count()
data_by_signedIn_age = data_filter_noNullAge.groupby(["AG", "Signed_In"],as_index=False).count()

# Age

# sns.barplot(data=data_by_signedIn_age,
#             x=data_by_signedIn_age.AG,
#             y=data_by_signedIn_age.Clicks)

# Gender + Age

# ax=sns.barplot(data=data_by_gender_age,
#             x=data_by_gender_age.AG,
#             y=data_by_gender_age.Clicks,
#             hue=data_by_gender_age.Gender)
# ax.set(xlabel='Age Groups',ylabel='User clics')
# data_by_gender_age[data_by_gender_age.AG =='0-18'].Impressions


data_by_impression_age = data_filter_noNullAge.groupby(["AG", "Impressions"],as_index=False).count()
sns.barplot(data=data_by_impression_age,
            x=data_by_impression_age.AG,
            y=data_by_impression_age.Clicks,
            hue=data_by_impression_age.Impressions)
Age_valueGroup=["18","18-24","25-34","35-44","45-54","55-64","65+"]
[data_filter_noNullAge[data_filter_noNullAge.AG==value].Impressions.mean() for value in Age_valueGroup]

fig, axs = plt.subplots(5, 6)
for i in range(0, 5):
    for j in range(0, 6):
        data = pd.read_csv("dateset/nyt/nyt" + str(i + j + 1) + ".csv")
        data_no_null_age = data[data.Age > 0]
        data_no_null_age.insert(1, "Age_Group", [age_group(age) for age in data_no_null_age.Age.to_list()])
        data = data_no_null_age.groupby(["Age_Group", "Gender"], as_index=False).count()
        axs[i, j].bar(data.Age_Group, data.Signed_In)
for ax in axs.flat:
    ax.set(xlabel='x-label', ylabel='y-label')

for ax in axs.flat:
    ax.label_outer()
plt.show()