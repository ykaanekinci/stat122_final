import pandas as pd
sleep="ZZZZZ.xlsx"
Project = pd.read_excel(sleep)

#Cleaning duplicate data
Project.drop_duplicates(inplace=True)

#Edit column names
Project.columns=Project.columns.str.replace('##', '').str.strip()
Project.columns=Project.columns.str.replace('_', ' ').str.title()
Project.columns=Project.columns.str.replace('"', '').str.title()

Project.rename(columns={'Screen_Time': 'Screen Time', 'Alcohol_Consumption_Level': 'Alcohol Consumption Level','Unnamed: 8': 'Snoring','Unnamed: 10': 'Job Name'}, inplace=True)

#Removing unnecessary flags and spaces from data
Correction1 = Project.replace('##', '', regex=True, inplace=True)
Correction2 = Project.replace('"', '', regex=True, inplace=True)
Correction3 = Project.replace(' ', '', regex=True, inplace=True)
Correction4 = Project.replace('-', '', regex=True, inplace=True)

#Changing Capital Letters in Data
Project.loc[:, 'Stress Level'] = Project['Stress Level'].apply(lambda x: str(x).title())
Project.loc[:, 'Snoring'] = Project['Snoring'].apply(lambda x: str(x).title())
#Editing Gender Column
gender_mapping = {'F': 'Female','M': 'Male','Female':'Female','Male':'Male'}
Project['Gender'] = Project['Gender'].map(gender_mapping)

#Editing Snoring Column
snoring_mapping = {'Yes': 'Yes','Y': 'Yes','No': 'No'}

Project['Snoring'] = Project['Snoring'].map(snoring_mapping)

#Converting string values in the Sleep Duration column to numeric values
corrected_values = []
for value in Project['Sleep Duration']:
    if isinstance(value, str):
        corrected_values.append(float(value.replace(',', '.')))
    else:
        corrected_values.append(value)
Project['Sleep Duration'] = corrected_values


#Converting string values in the Height M column to numeric values
corrected_values = []
for value in Project['Height M']:
    if isinstance(value, str):
        corrected_values.append(float(value.replace(',', '.')))
    else:
        corrected_values.append(value)
Project['Height M'] = corrected_values

#Filling empty values in Weight Kg column with mean
mean_mass = Project['Weight Kg'].mean()
Project['Weight Kg'].fillna(mean_mass, inplace=True)

#Filling empty values in Sleep Duration column with mean
mean_mass = Project['Sleep Duration'].mean()
Project['Sleep Duration'].fillna(mean_mass, inplace=True)

#Replace outliers in Sleep Duration column with mean
quan1 =Project['Sleep Duration'].quantile(0.25)
quan3 =Project['Sleep Duration'].quantile(0.75)
iqr =quan3-quan1

outlierlar = ((Project['Sleep Duration'] < quan1 - 1.5 * iqr) |(Project['Sleep Duration'] >quan3 +1.5 *iqr))

Project.loc[outlierlar,'Sleep Duration'] = Project['Sleep Duration'].mean()

#Replace outliers in Weight Kg column with mean
quan1 =Project['Weight Kg'].quantile(0.25)
quan3 =Project['Weight Kg'].quantile(0.75)
iqr =quan3-quan1

outlierlar = ((Project['Weight Kg'] < quan1 - 1.5 * iqr) |(Project['Weight Kg'] >quan3 +1.5 *iqr))

Project.loc[outlierlar,'Weight Kg'] = Project['Weight Kg'].mean()

#Filling empty values in Alcohol Consumption Level column with mode
mode_mass = Project['Alcohol Consumption Level'].mode()[0]
Project['Alcohol Consumption Level'].fillna(mode_mass, inplace=True)

#Filling empty values in Screen Time column with mode
mode_mass = Project['Screen Time'].mode()[0]
Project['Screen Time'].fillna(mode_mass, inplace=True)

#Filling empty values in Work Hours column with mean
mean_mass = Project['Work Hours'].mean()
Project['Work Hours'].fillna(mean_mass, inplace=True)

#Filling empty values in Height M column with mean
mean_mass = Project['Height M'].mean()
Project['Height M'].fillna(mean_mass, inplace=True)

#Filling empty values in Screen Time column with mean
mean_mass = Project['Screen Time'].mean()
Project['Screen Time'].fillna(mean_mass, inplace=True)

#ID column removal process
ID_Column = 'Id'

Data = Project.drop(columns=[ID_Column])

#The process of removing the empty data in the Job Name column (I delete all the remaining empty rows, since there is only a blank space in the Job_Name row, it only deletes that row).
Project = Project.dropna()

Project.to_excel(sleep, index=False)