import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sleep="ZZZZZ.xlsx"
Project = pd.read_excel(sleep)

yyy=Project['Work Hours']
lll=Project['Snoring']

araliklar = range(40, 61, 5)
sns.boxplot(x=yyy, y=lll , data=Project)
plt.title('Snoring vs Work Hours')
plt.ylabel('Snoring')
plt.xlabel('Work Hours')
plt.xticks(araliklar)
plt.show()