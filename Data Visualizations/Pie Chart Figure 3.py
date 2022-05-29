import matplotlib.pyplot as plt

labels = ['Riverine flood', 'Flash flood', 'Coastal flood']
share = [14, 10,0]

explode = (0.1,0,0)
plt.style.use('ggplot')
plt.title('Thailand flood Subtype in 20 years')
plt.pie(x=share, explode=explode, labels=labels, autopct='%.2f%%',
        startangle=90)
plt.axis('equal')
plt.legend(loc='upper right')



plt.show()