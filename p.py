import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import seaborn as sns
import matplotlib.pyplot as plt
from ast import literal_eval
import operator


# Epoch = date_added in epoch time
superfund = pd.read_csv("withstates.csv")

"""
# Distribution by Count
# Count all of the superfund sites per state
c = superfund[['state', 'site_score']]
count = c.groupby('state', as_index=False, sort=False).agg('count')
mostCount = count.sort_values(by='site_score', ascending=False)[:10]
leastCount = count.sort_values(by='site_score', ascending=True)[:10]

# Plot most count by state
sns.set_style("darkgrid")
mostCount_plot = sns.barplot(x=mostCount['state'], y=mostCount['site_score'],
                        palette='muted')

for p in mostCount_plot.patches:
    mostCount_plot.annotate(str(p.get_height()), (p.get_x() * 1.005, p.get_height() * 1.005))

plt.title('Most Superfund Sites by State')
plt.xlabel('State')
plt.ylabel('Score')
plt.savefig('mostSuperfundPerState.png')

plt.clf()

# Plot least count by state
leastCount = sns.barplot(x=leastCount['state'], y=leastCount['site_score'],
                        palette='muted')

for p in leastCount.patches:
    leastCount.annotate(str(p.get_height()), (p.get_x() * 1.005, p.get_height() * 1.005))

plt.title('Least Superfund Sites by State')
plt.xlabel('State')
plt.ylabel('Score')
plt.savefig('leastSuperfundPerState.png')
plt.clf()

count = c.groupby('state').agg('count')
count.to_csv('stateCount.csv')
print(count)

print('\n')

#-----------------------------------------------------------------------------------------------------#

# Distribution by Score
# 1. Average score per state
avgPerState = c.groupby('state').mean()
avgPerState.to_csv('averagePerState.csv')
print(avgPerState)

# Plot the averages

avgPlotState = c.groupby('state', as_index=False, sort=False).mean().round(2)
mostAvg = avgPlotState.sort_values(by='site_score', ascending=False)[:10]

# Plot highest average per state
mostAvg_plot = sns.barplot(x=mostAvg['state'], y=mostAvg['site_score'],
                        palette='muted')

for p in mostAvg_plot.patches:
    mostAvg_plot.annotate(str(p.get_height()), (p.get_x() * 1.005, p.get_height() * 1.005))

plt.title('Highest Average Superfund Scores by State')
plt.xlabel('State')
plt.ylabel('Score')
plt.savefig('highAvgPerState.png')

plt.clf()



leastAvg = avgPlotState.sort_values(by='site_score', ascending=True)[:10]

# Plot lowest average per state
lowAvg_plot = sns.barplot(x=leastAvg['state'], y=leastAvg['site_score'],
                        palette='muted')

for p in lowAvg_plot.patches:
    lowAvg_plot.annotate(str(p.get_height()), (p.get_x() * 1.005, p.get_height() * 1.005))

plt.title('Lowest Average Superfund Scores by State')
plt.xlabel('State')
plt.ylabel('Score')
plt.savefig('lowAvgSuperfundPerState.png')

plt.clf()


# Contaminents
contams = pd.read_csv("withcontams.csv")


listsOfContams = contams.contaminants

freqOfContam = dict()

tempList1 = []
filteredContamList = []

for x in listsOfContams:
    a = literal_eval(x)
    if a is None:
        continue
    else:
        for i in a:
            filteredContamList.append(i[0])

for i in filteredContamList:
    if i not in freqOfContam:
        freqOfContam[i] = 1
    else:
        freqOfContam[i] += 1

count = 0
for x in freqOfContam:
    #print(x, ':', freqOfContam[x])
    count += freqOfContam[x]

print("List Length:", len(filteredContamList))
print("Dictionary:", count, "\n")

topTwentyContam = sorted(freqOfContam, key=freqOfContam.get, reverse=True)[:20]
twentyDict = dict()


for i in topTwentyContam:
    print(i, freqOfContam[i])
    twentyDict[i] = freqOfContam[i]


# plt.bar(range(len(twentyDict)), list(twentyDict.values()), align='center')
# plt.xticks(range(len(twentyDict)), list(twentyDict.keys()))
# plt.show()


plt.barh(range(len(twentyDict)), list(twentyDict.values()), align='edge')
plt.yticks(range(len(twentyDict)), list(twentyDict.keys()))

plt.title('Most Frequent Contaminants')
plt.xlabel('Frequency')
plt.ylabel('Contaminant')
plt.tight_layout()
plt.savefig('mostFreqContam.png')

#plt.show()

plt.clf()
"""

performance = pd.read_csv("withperformances.csv")
labels = ["Yes", "No", "Insufficient Data"]

file = open("piecharts.txt","w") 

# Human Exposure
humanExposure = performance.HumanExposureUnderControl

yes = 0
no = 0
insufficient = 0
for i in humanExposure:
    if i == 'Yes':
        yes += 1
    elif i == 'No':
        no += 1
    else:
        insufficient += 1

print("Human Exposure")
print("Yes:", yes)
print("No:", no)
print("Insufficient Data:", insufficient)
print("-----------------------------------\n")

file.write("Human Exposure\n\n")
file.write("Yes: {}\n".format(yes))
file.write("No: {}\n".format(no))
file.write("Insufficient Data: {}\n\n".format(insufficient))
file.write("-----------------------------------\n\n")

hePie = [yes, no, insufficient]
plt.pie(hePie, labels=labels, autopct='%1.1f%%', startangle=140)

plt.title("Human Exposure")
plt.axis('equal')
#plt.show()
plt.savefig("humanExposure.png")
plt.clf()

# Ground Water Under Control
groundWater = performance.GroundwaterMigrationUnderControl
labels = ["Yes", "No", "Insufficient Data", "Not a Ground Water Site"]

yes = 0
no = 0
insufficient = 0
ngws = 0
for i in groundWater:
    if i == 'Yes':
        yes += 1
    elif i == 'No':
        no += 1
    elif i == 'Not a Ground Water Site':
        ngws += 1
    else:
        insufficient += 1

print("Groundwater under control?")
print("Yes:", yes)
print("No:", no)
print("Insufficient Data:", insufficient)
print("Not a Ground Water Site", ngws)
print("-----------------------------------\n")

file.write("Groundwater under control?\n\n")
file.write("Yes: {}\n".format(yes))
file.write("No: {}\n".format(no))
file.write("Insufficient Data: {}\n".format(insufficient))
file.write("Not a Ground Water Site: {}\n\n".format(ngws))
file.write("-----------------------------------\n\n")

gwPie = [yes, no, insufficient, ngws]
plt.pie(gwPie, labels=labels, autopct='%1.1f%%', startangle=140)

plt.title("GroundWater Exposure")
plt.axis('equal')
#plt.show()
plt.savefig("gwExposure.png")
plt.clf()

# Clean up complete?
cleanUp = performance.ConstructionComplete

yes = 0
no = 0
insufficient = 0
for i in cleanUp:
    if i == 'Yes':
        yes += 1
    elif i == 'No':
        no += 1
    else:
        insufficient += 1

print("Clean up complete?")
print("Yes:", yes)
print("No:", no)
print("Insufficient Data:", insufficient)
print("-----------------------------------\n")

file.write("Clean up complete?\n\n")
file.write("Yes: {}\n".format(yes))
file.write("No: {}\n".format(no))
file.write("Insufficient Data: {}\n\n".format(insufficient))
file.write("-----------------------------------\n\n")

cuPie = [yes, no]
labels = ["Yes", "No"]
plt.pie(cuPie, labels=labels, autopct='%1.1f%%', startangle=140)

plt.title("Are these sites cleaned up?")
plt.axis('equal')
#plt.show()
plt.savefig("cleanedUp.png")
plt.clf()

# Ready for use?
ready = performance.SitewideReadyforAnticipatedUse

yes = 0
no = 0
insufficient = 0
for i in ready:
    if i == 'Yes':
        yes += 1
    elif i == 'No':
        no += 1
    else:
        insufficient += 1

print("Site ready for use?")
print("Yes:", yes)
print("No:", no)
print("Insufficient Data:", insufficient)
print("-----------------------------------\n")

file.write("Site ready for use?\n\n")
file.write("Yes: {}\n".format(yes))
file.write("No: {}\n".format(no))
file.write("Insufficient Data: {}\n\n".format(insufficient))
file.write("-----------------------------------\n\n")

file.close()

labels = ["Yes", "No"]
srPie = [yes, no]
plt.pie(srPie, labels=labels, autopct='%1.1f%%', startangle=140)

plt.title("Are these sites ready to use?")
plt.axis('equal')
#plt.show()
plt.savefig("readyToUse.png")
plt.clf()

