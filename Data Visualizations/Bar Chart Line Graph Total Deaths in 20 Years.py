import matplotlib.pyplot as plt

# x axis
x= [1,2,3,4,5,6,7,8,9]

# y axis
y= [934,1823,43,160,305,838,2247,3,2412]

plt.style.use('seaborn')
plt.bar(x=x, height=y, width=0.4)
plt.xticks(x, ('Cambodia','Indonesia','Lao' ,'Malaysia','Myanmar','Philippines','Thailand','Timor-Leste','Vietnam'))

y2 = [i+3 for i in y]
plt.title('Total Deaths in 20 Years')

plt.plot(x, y2, color='green')
plt.scatter(x, y2)

plt.xlabel('Country')
plt.ylabel('Deaths')

plt.show()
