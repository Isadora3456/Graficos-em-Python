import matplotlib.pyplot as plt
labels = 'Miyamasuzaka Girls Academy','Kamiyama High School','Online High School'
sizes = [11, 8, 1]
colors = [ 'lightpink', 'lightgrey', 'coral']
patches, texts, autotexts = plt.pie(sizes, colors=colors, autopct='%1.1f%%',
startangle=90)
plt.legend(patches, labels, loc="lower right")
plt.axis('equal')
plt.show() 