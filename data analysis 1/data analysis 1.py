import matplotlib.pyplot as plt

delicacies = ['Mushroom', 'Pineapple', 'Prawns', 'Sausage', 'Spinach']
values = [0.28, 0.18, 0.08, 0.28, 0.18]

plt.barh(delicacies, values, color='blue')

plt.title('Barchart')
plt.xlabel('Proportion of Total')
plt.ylabel('delicacies')

plt.show()
