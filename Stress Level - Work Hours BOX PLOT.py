import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sleep="ZZZZZ.xlsx"
Project = pd.read_excel(sleep)

yyy=Project['Work Hours']
aaa=Project['Stress Level']

siralama = ['Low', 'Medium', 'High']
Project['Stress Level'] = pd.Categorical(Project['Stress Level'], categories=siralama, ordered=True)


sns.boxplot(x=yyy, y=aaa , data=Project)
araliklar = range(40, 61, 5)
plt.xticks(araliklar)
plt.title('Stress Level vs Work Hours')
plt.ylabel('Stress Level')
plt.xlabel('Work Hours')
plt.show()