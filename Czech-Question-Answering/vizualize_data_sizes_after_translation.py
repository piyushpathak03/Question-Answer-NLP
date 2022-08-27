import matplotlib.pyplot as plt
import numpy as np 

train=[0.47,0.63-0.47,0.80-0.63,0.88-0.80,0.94-0.88,0.98-0.94]
dev = [0.56,0.73-0.56,0.87-0.73,0.93-0.87,0.96-0.93,0.99-0.96]

labels = ['1.0', '0.9', '0.8', '0.7', '0.6', '0.5']
plt.bar(range(len(train)),train) 
plt.title('Match of translated answer with translated text (Train set)')
plt.ylabel('Preserved data') 
plt.xlabel('Match')
plt.xticks(np.arange(len(train)), labels)
plt.savefig('train-match.pdf')
plt.show()

plt.bar(range(len(dev)),dev) 
plt.title('Match of translated answer with translated text (Dev set)')
plt.ylabel('Preserved data') 
plt.xlabel('Match')
plt.xticks(np.arange(len(train)), labels)
plt.savefig('dev-match.pdf')
plt.show()

