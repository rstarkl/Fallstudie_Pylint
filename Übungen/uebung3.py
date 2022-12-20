# Die Teilnehmer sollten Pylint auf den folgenden Code anwenden und alle Probleme beheben, die gefunden werden.

def calculateSum(numbers):
    sum = 0
    for number in numbers:
        sum += number
    print(sum)

calculateSum([1, 2, 3, 4, 5])