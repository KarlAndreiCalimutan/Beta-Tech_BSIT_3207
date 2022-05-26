import matplotlib.pyplot as plt

labels = ['Apple', 'Samsung', 'Xiomi', 'BBk', 'others']
share = [10.85, 7, 6, 10, 15] # sales in million units
plt.pie(x=share, labels=labels, autopct='%.2f%%')

# explode = (0.1, 0, 0, 0, 0)  # only "explode" the 1st slice (i.e. 'Apple')
plt.style.use('ggplot')
plt.title('Share of Companies')
plt.pie(x=share, labels=labels, autopct='%.2f%%',
         startangle=90)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.legend(loc='upper left')

# donut
circle = plt.Circle(xy=(0,0), radius=.75, facecolor='white')
plt.gca().add_artist(circle)
plt.show()
