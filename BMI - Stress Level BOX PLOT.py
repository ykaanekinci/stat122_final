import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
sleep="ZZZZZ.xlsx"
Project = pd.read_excel(sleep)



Project['BMI'] = Project['Weight Kg'] / (Project['Height M'] ** 2)

siralama = ['Low', 'Medium', 'High']
Project['Stress Level'] = pd.Categorical(Project['Stress Level'], categories=siralama, ordered=True)

sns.boxplot(x='Stress Level', y='BMI',data=Project,hue='Stress Level',palette='Set3')

plt.title('BMI by Stress Level')
plt.xlabel('Stress Level')
plt.ylabel('BMI')

plt.show()
