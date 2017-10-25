import pandas
data = pandas.read_csv('titanic.csv')
print(data.groupby(['Survived'])['PassengerId'].count())
