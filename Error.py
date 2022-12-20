# Pylint wird eine Ausgabe machen, weil die Variable nicht definiert wurde
def someFunction():
    print(x)

# Pylint wird eine Ausgabe machen, weil die Funktion nicht existiert
def someFunction():
    nonExistentFunction()