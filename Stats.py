


import matplotlib.pyplot as plt

def average(sorted_list):
    total = 0
    for element in sorted_list:
        total = total + element
    average = total/len(hours)
    return average

fhand = open('StudentExercise.csv')
next(fhand)
hours=[]
for line in fhand:
    s=line.split(',')
    h=s[0]
    if len(h)<1:
        continue
    hours.append(float(h))
    
print(average(hours))
plt.hist(hours, bins=10)
plt.ylabel("hours")
plt.title("hours of exercise")
plt.show()

