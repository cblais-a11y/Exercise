import matplotlib.pyplot as plt
fhand = open('StudentExercise.csv')
next(fhand)
hours=[]
for line in fhand:
    s=line.split(',')
    h=s[0]
    if len(h)<1:
        continue
    hours.append(h)
    
    
plt.hist(hours, bins=10)
plt.ylabel("hours")
plt.title("hours of exercise")
plt.show()
