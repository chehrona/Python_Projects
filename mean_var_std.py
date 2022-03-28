import numpy as np

def calculate(listValues):
    if len(listValues) < 9:
        raise ValueError("List must contain nine numbers.")
    calculations = dict()
    
    columnValues = formulas(listValues, 0)
    rowValues = formulas(listValues, 1)
    flatValues = formulas(listValues)

    calculations['mean'] = [columnValues['mean'], rowValues['mean'], flatValues['mean']]
    calculations['variance'] = [columnValues['variance'], rowValues['variance'], flatValues['variance']]
    calculations['standard deviation'] = [columnValues['standard deviation'], rowValues['standard deviation'], flatValues['standard deviation']]
    calculations['max'] = [columnValues['max'], rowValues['max'], flatValues['max']]
    calculations['min'] = [columnValues['min'], rowValues['min'], flatValues['min']]
    calculations['sum'] = [columnValues['sum'], rowValues['sum'], flatValues['sum']]
    
    return calculations


def formulas(listValues, axisValue = None):
    listToArray = np.array(listValues).reshape(3, 3)
    average = listToArray.mean(axis=axisValue).tolist()
    variance = listToArray.var(axis=axisValue).tolist()
    stdeviation = listToArray.std(axis=axisValue).tolist()
    maximums = listToArray.max(axis=axisValue).tolist()
    minimums = listToArray.min(axis=axisValue).tolist()
    added = listToArray.sum(axis=axisValue).tolist()
    dictFormulas = dict()
    dictFormulas['mean'] = average
    dictFormulas['variance'] = variance
    dictFormulas['standard deviation'] = stdeviation
    dictFormulas['max'] = maximums
    dictFormulas['min'] = minimums
    dictFormulas['sum'] = added

    return dictFormulas

print(calculate([0,1,2,3,4,5,6,7,8]))
