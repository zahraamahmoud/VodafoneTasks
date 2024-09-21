import pandas as pd


USD_to_EGP=50
dataFrame=pd.read_csv('Employees.csv')
print(dataFrame)

dataFrame=dataFrame.drop_duplicates()


dataFrame['Age']=dataFrame['Age'].astype(int)

dataFrame['Salary(EGP)']=dataFrame['Salary(USD)']*USD_to_EGP
dataFrame = dataFrame.drop(columns=['Salary(USD)'])

avg_Age=dataFrame['Age'].mean()
print('Average Age: '+str(avg_Age))

median_sal=dataFrame['Salary(EGP)'].median()
print('median salary: '+str(median_sal))

gender_count=dataFrame['Gender'].value_counts()
if gender_count['F'] > 0:
      Ratio=gender_count['M']/gender_count['F']
      print('Ratio between males and female: '+str(Ratio))
else :
    print('can not divide by Zero')

print(dataFrame)

dataFrame.to_csv('newEmployees.csv',index=False)

