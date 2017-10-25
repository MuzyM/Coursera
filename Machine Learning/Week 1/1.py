import pandas
data = pandas.read_csv('titanic.csv')
print(data['Sex'].value_counts())
#print(data['Sex'].value_counts())
