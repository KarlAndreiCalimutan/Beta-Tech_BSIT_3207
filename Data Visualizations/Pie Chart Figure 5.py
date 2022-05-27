import matplotlib.pyplot as plt

labels = ['Riverine Flood', 'Flash flood', 'Coastal flood']
share = [18, 10,  0]

explode = (0.1,0,0)
plt.style.use('ggplot')
plt.title('20 years Top 3 Country Floodsubtype ')
plt.pie(x=share, explode=explode, labels=labels, autopct='%.2f%%',
        startangle=90)
plt.axis('equal')
plt.legend(loc='upper right')


#circle = plt.Circle(xy=(0,0), radius=.75, facecolor='white')
#plt.gca().add_artist(circle)
plt.show()






