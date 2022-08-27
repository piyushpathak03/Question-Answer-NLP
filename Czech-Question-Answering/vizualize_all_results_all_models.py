import matplotlib.pyplot as plt
import numpy as np 

labels = ['BiDAF tCZ80dCZ','BiDAF tCZ100dCZ','BiDAF tENdCZ-EN-CZ','M-BERTc tENdCZ-EN-CZ','M-BERTu tENdCZ-EN-CZ',
          'M-BERTc tCZ80dCZ','M-BERTu tCZ80dCZ','M-BERTc tCZ100dCZ','M-BERTu tCZ100dCZ',
          'M-BERTc tENdCZ','M-BERTu tENdCZ']
em =[53.74,53.15,53.57,65.49,65.17,64.34,60.48,62.16,62.14,58.78,63.71]
f1 =[65.49,62.7,65.84,77.0,77.0,72.77,73.46,73.0,73.46,70.16,74.78]


plt.title('Model results for Czech QA')
ax = plt.subplot(111)

ax.set_xlabel('Model')
ax.set_ylabel('Value [%]')

ax.bar(np.arange(0,len(f1)),f1, label='F1 score',color='k')
ax.bar(np.arange(0,len(em)),em, label='Exact match',color='g') 
ax.set_xticks(np.arange(len(em))) 
ax.set_xticklabels(labels, rotation='vertical')
ax.legend()
ax.set_ylim(bottom=50)
plt.savefig('cz-all.png', bbox_inches='tight')



