# Pylint wird eine Ausgabe machen, weil die Variable nicht definiert wurde
def someFunction():
        x += 1
    print(x)

# Pylint wird eine Ausgabe machen, weil die Funktion nicht existiert
def someFunction():
    nonExistentFunction()