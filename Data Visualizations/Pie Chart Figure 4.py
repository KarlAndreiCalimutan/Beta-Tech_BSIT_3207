import matplotlib.pyplot as plt

labels = ['Riverine Flood', 'Flash flood', 'Coastal flood']
share = [23, 12,  3]

explode = (0.1,0,0)
plt.style.use('ggplot')
plt.title('20 years Top 2 Country Floodsubtype ')
plt.pie(x=share, explode=explode, labels=labels, autopct='%.2f%%',
        startangle=90)
plt.axis('equal')
plt.legend(loc='upper right')


#circle = plt.Circle(xy=(0,0), radius=.75, facecolor='white')
#plt.gca().add_artist(circle)
plt.show()






