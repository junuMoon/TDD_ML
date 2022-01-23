# Dataset EDA

## Dataset overview
- train dataset size: 891
- test dataset size: 418
- num of columns: 11
- target variable: Survived

|Variable|Definition|Key|
|--- |--- |--- |
|survival|Survival|0 = No, 1 = Yes|
|pclass|Ticket class|1 = 1st, 2 = 2nd, 3 = 3rd|
|sex|Sex||
|Age|Age in years||
|sibsp|# of siblings / spouses aboard the Titanic||
|parch|# of parents / children aboard the Titanic||
|ticket|Ticket number||
|fare|Passenger fare||
|cabin|Cabin number||
|embarked|Port of Embarkation|C = Cherbourg, Q = Queenstown, S = Southampton|

## Variable Notes

pclass: A proxy for socio-economic status (SES)
1st = Upper
2nd = Middle
3rd = Lower

age: Age is fractional if less than 1. If the age is estimated, is it in the form of xx.5

sibsp: The dataset defines family relations in this way...
Sibling = brother, sister, stepbrother, stepsister
Spouse = husband, wife (mistresses and fiancés were ignored)

parch: The dataset defines family relations in this way...
Parent = mother, father
Child = daughter, son, stepdaughter, stepson
Some children travelled only with a nanny, therefore parch=0 for them.

## Target variable
- Survived:
    - 0: died, 549(61.6%)
    - 1: survived, 342(38.4%)

## Null Percentage

'Embarked', 'Age', 'Cabin' needs to be imputed.

|             |   null_pcnt |
|:------------|------------:|
| PassengerId |  0          |
| Survived    |  0          |
| Pclass      |  0          |
| Name        |  0          |
| Sex         |  0          |
| Age         |  0.198653   |
| SibSp       |  0          |
| Parch       |  0          |
| Ticket      |  0          |
| Fare        |  0          |
| Cabin       |  0.771044   |
| Embarked    |  0.00224467 |

## Categorical Variables

### Category Proportions

- Embarked:
    - S: 72.3%
    - C: 18.9$
    - Q: 8.6%
- Pclass:
    - 1: 24.2%
    - 2: 20.7%
    - 3: 55.1%
- Sex:
    - male: 64.8%
    - female: 35.2%
- SibSp:
    - 0: 68.2%
    - 1: 23.5%
    - 2: 3.1%
    - 3: 1.8%
    - 4: 2.0%
    - 5: 0.6%
    - 8: 0.8%
- Parch:
    - 0: 76.1%
    - 1: 13.2%
    - 2: 9.0%
    - 3: 0.6%
    - 4: 0.4%
    - 5: 0.6%
    - 6: 0.1%
    
#### Comments

- frequency(`Sibsip` == 8) = 0.8%
- In `Sibsp` and `Parch`, 0 is the most frequent value. Check this means the majority of passengers were alone.
    - No parch and no sibsp = 537, 60.2%

### Survived proportion per category
- Embarked:
    - S: 33.7%
    - C: 55.4%
    - Q: 39.0%
- Pclass:
    - 1: 63.0%
    - 2: 47.3%
    - 3: 24.2%
- Sex:
    - male: 18.9%
    - female: 74.2%
- SibSp:
    - 0: 34.5%
    - 1: 53.6%
    - 2: 46.4%
    - 3: 25.0%
    - 4: 16.7%
    - 5: 0.0%
    - 8: 0.0%
- Parch:
    - 0: 34.4%
    - 1: 55.1%
    - 2: 50.0%
    - 3: 60.0%
    - 4: 0.0%
    - 5: 20.0%
    - 6: 0.0%

#### Comments

- Male survivor percent is extremly lower thatn Female's
- `Embarked` refers to location. Is will be a factor of survivor?
- In `Parch`, value 1 has the highest survivor proportion. 
- In `SibSp`, value 3 has the highest survivor proportion. 
