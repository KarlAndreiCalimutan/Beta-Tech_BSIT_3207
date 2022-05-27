import matplotlib.pyplot as plt

labels = ['Cambodia', 'Indonesia', 'Lao', 'Malaysia', 'Myanmar','Philippines', 'Thailand', 'Timor-Leste', 'Vietnam']
share = [934, 1823, 43, 160, 305,838,2247,3,2412]

explode = (0,0.1,0,0, 0, 0, 0, 0,0)
plt.style.use('ggplot')
plt.title('Total Deaths in 20 Years')
plt.pie(x=share, explode=explode, labels=labels, autopct='%.2f%%',
        startangle=90)
plt.axis('equal')
plt.legend(loc='upper right')


#circle = plt.Circle(xy=(0,0), radius=.75, facecolor='white')
#plt.gca().add_artist(circle)
plt.show()


