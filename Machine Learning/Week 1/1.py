import pandas
data = pandas.read_csv('titanic.csv')
print(data['Age'].sum())
