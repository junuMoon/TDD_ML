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

### Proportions

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
- Alone:
    - True: 39%
    - Flase: 61%

### Survived Rates
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
- Alone:
    - True: 30%
    - False: 50%

### Cabin
- Cabin data consists of Capital Letter and random number
- Data should be grouopd by First capital letter

| Cabin_Letter   |   Survived |
|:---------------|-----------:|
| A              |   0.466667 |
| B              |   0.744681 |
| C              |   0.59322  |
| D              |   0.757576 |
| E              |   0.75     |
| F              |   0.615385 |
| G              |   0.5      |
| T              |   0        |
| U              |   0.299854 |

### Ticket 
- Ticket data can divide into two group
    - Ticket has string -> survival rate: 0.38
    - Ticket has no string -> survㅇㅁival rate: 0.38
    - No survival rate difference
- length of Ticker number vary from (1, 3, 4, 5, 6, 7)
- For now it's too complicated to group by Ticket, so drop this col

### Name
- Could extract title from Name
- Survival Rates: Mrs(0.8) > Miss > Master > Unknown > Mr

### Comments

- Male survivor percent is extremly lower thatn Female's
- `Embarked` refers to location. Is will be a factor of survivor?
    - Embarked make difference when Pclass==3, and Sex==Female
    - Don't know why


## Numerical Variables

### Proportions
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

### Survival Rates
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

### Comments

- frequency(`Sibsip` == 8) = 0.8%
- In `Parch`, value 1 has the highest survivor proportion. 
- In `SibSp`, value 3 has the highest survivor proportion. 
- In `Sibsp` and `Parch`, 0 is the most frequent value. Check this means the majority of passengers were alone.
    - Alone(No parch and no sibsp)= 549,  65%
    - Alone survirval rate = 30%
    - Made 'Alone' columns

## Impute

### Age
- Age fill considered columns(Alone, Sex, Pclass)
