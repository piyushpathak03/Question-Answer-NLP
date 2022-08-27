import matplotlib.pyplot as plt
import numpy as np 

# czech multibert 1-4epochs train 100
un_exact = [60.9,62.14,61.95,61.83]
un_f1 = [72.38,73.46,73.20,73.12]
c_exact = [61.17,62.12,62.51,62.10]
c_f1 = [72.16,73.0,73.22,72.95]


plt.title('Multilingual BERT trained on Czech with different number of epochs')
# plotting the points  
ax = plt.subplot(111)

ax.set_xlabel('Epochs')
ax.set_ylabel('Value [%]')

ax.plot(un_exact, 'ro--', label='Exact match (uncased)')
ax.plot(c_exact, 'bo--', label='Exact match (cased)')
ax.plot(un_f1, 'go--', label='F1 score (uncased)') 
ax.plot(c_f1, 'ko--', label='F1 score (cased)') 
ax.set_xticks(np.arange(4))
ax.set_xticklabels([1,2,3,4]) 
ax.legend()


plt.savefig('multiczbertepochs100.pdf', bbox_inches='tight')
plt.show()


# czech multibert 1-4epochs train 80
un_exact = [58.68,60.78,60.12,59.92]
un_f1 = [71.95,73.46, 72.99,72.69]
c_exact = [59.44,60.34,60.26,59.28]
c_f1 = [72.42,72.77,72.95,72.22]



plt.title('Multilingual BERT trained on Czech with different number of epochs')
# plotting the points  
ax = plt.subplot(111)

ax.set_xlabel('Epochs')
ax.set_ylabel('Value [%]')

ax.plot(un_exact, 'ro--', label='Exact match (uncased)')
ax.plot(c_exact, 'bo--', label='Exact match (cased)')
ax.plot(un_f1, 'go--', label='F1 score (uncased)') 
ax.plot(c_f1, 'ko--', label='F1 score (cased)') 
ax.set_xticks(np.arange(4)) 
ax.set_xticklabels([1,2,3,4]) 
ax.legend()


plt.savefig('multiczbertepochs80.pdf', bbox_inches='tight')
plt.show()




