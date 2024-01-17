import pandas as pd
import matplotlib.pyplot as plt

sleep="ZZZZZ.xlsx"
Project = pd.read_excel(sleep)

siralama = ['High', 'Medium', 'Low']
Project['Stress Level'] = pd.Categorical(Project['Stress Level'], categories=siralama, ordered=True)
Project['Alcohol Consumption Level'] = pd.Categorical(Project['Alcohol Consumption Level'], categories=siralama, ordered=True)


barc=(Project.groupby(['Stress Level','Alcohol Consumption Level'], observed=False)['Stress Level'].count().unstack(fill_value=0))
grafik= barc.plot(kind='barh',stacked=True,colormap='viridis')

plt.tick_params(axis='x', rotation=45)
plt.tick_params(axis='y', rotation=45)
plt.title('Alcohol Consumption Level and Stress Level')
plt.ylabel('Stress Level')
plt.xlabel('Number of people')
plt.legend(title='Alcohol Consumption Level',loc='upper right')
plt.show()
