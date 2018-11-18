import numpy as np
import csv

#Trucks
#[0]: Weight
#[1]: Vol
#[2]: Value
_trucks = np.array([
[3500,1200,0],
[16000,4000,0]])

#Get data from csv
#[0]: Item
#[1]: Weight
#[2]: Vol
#[3]: Value
_instance = np.genfromtxt('instances/instance_1.csv', delimiter=',')
_binaryList = np.zeros(25)

weight = []
vol = []
value = []
sortedList = []

truck1ItemList = []
truck2ItemList = []


#TODO: Create the general equation
def getSortedList():
    for i in _instance:
        weight.append(int(i[1]))
        vol.append(int(i[2]))
        value.append(int(i[3]))

    _weightnp = np.asarray(weight)
    _valuenp = np.asarray(value)
    _div = np.divide(_valuenp,_weightnp)
    _indexSort = np.array(np.argsort(_div))
    _divSort = np.sort(_div)

    for j in range(0,len(_indexSort)):
        sortedList.append([_indexSort[j],_divSort[j]])
    return sortedList

def truck1Space(index):
    if(_trucks[0][0] >= _instance[index][1] and _trucks[0][1] >= _instance[index][2]):
        _trucks[0][0] -= _instance[index][1]
        _trucks[0][1] -= _instance[index][2]
        _trucks[0][2] += _instance[index][3]
        return True
    else:
        return False

def truck2Space(index):
    if(_trucks[1][0] >= _instance[index][1] and _trucks[1][1] >= _instance[index][2]):
        _trucks[1][0] -= _instance[index][1]
        _trucks[1][1] -= _instance[index][2]
        _trucks[1][2] += _instance[index][3]
        return True
    else:
        return False



def addItem():
    itemList = getSortedList()
    for x in range(len(itemList)-1,-1,-1):

        if(truck1Space(itemList[x][0]) == True):
            truck1ItemList.append(itemList[x][0])

        elif(truck2Space(itemList[x][0]) == True):
            truck2ItemList.append(itemList[x][0])
        else:
            break

    print("--------------------------")
    print("Truck1 items: ", truck1ItemList)
    print("Truck1 Weight: "+str(_trucks[0][0]))
    print("Truck1 Vol: "+str(_trucks[0][1]))
    print("Truck1 Value: "+str(_trucks[0][2]))

    print("--------------------------")
    print("Truck2 items: ", truck2ItemList)
    print("Truck2 Weight: "+str(_trucks[1][0]))
    print("Truck2 Vol: "+str(_trucks[1][1]))
    print("Truck2 Value: "+str(_trucks[1][2]))



addItem()
