# importing the required module
import matplotlib.pyplot as plt

# x-axis values
x = [0,1,2,3,4]
# y-axis values
y = [0, 0, 0, 0, 0]

# marking (0,0) as blue point
plt.plot(0,0, marker = 'o', color = 'blue')
# marking (1,0) as blue point
plt.plot(1,0, marker = 'o', color = 'blue')
# marking (2,0) as blue point
plt.plot(2, 0, marker = 'o', color = 'blue')
# marking (3,0) as blue point
plt.plot(3, 0, marker = 'o', color = 'blue')
# marking (4,0) as blue point
plt.plot(4,0, marker = 'o', color = 'blue')
plt.plot([0,4], [0,0])
# x-axis label
plt.xlabel('x - axis')
# frequency label
plt.ylabel('y - axis')
# plot title
plt.title('number line')
# showing legend
plt.legend()

# function to show the plot
plt.show()
