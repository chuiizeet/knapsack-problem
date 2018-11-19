import numpy as np
import csv
import sys
from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint
from pyfiglet import figlet_format

cprint(figlet_format('knapsack', font='big'))
cprint("\tTruck 1: ", 'red', end="")
print("3,500kg/1,200cm^3")
cprint("\tTruck 2: ", 'green', end="")
print("16,000kg/4,000cm^3")

instance = input('\nWhich instance do you want to use?[1-5]: ')

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

#Global Vars
# _binaryList = np.zeros() <---- Local search
_instance = np.genfromtxt('instances/instance_'+str(instance)+'.csv', delimiter=',')
weight = []
vol = []
value = []
sortedList = []
truck1ItemList = []
truck2ItemList = []
sumvW = 0.0
sumvV = 0.0

#Equation: (Value/weight)/(Σ(val/w)) + (Value/vol)/(Σ(val/vol))
def getSortedList():
    for i in _instance:
        weight.append(int(i[1]))
        vol.append(int(i[2]))
        value.append(int(i[3]))

    _weightnp = np.asarray(weight)
    _volnp = np.asarray(vol)
    _valuenp = np.asarray(value)

    #Equation init
    _divValWeightnp = np.divide(_valuenp, _weightnp)
    _divValVolnp = np.divide(_valuenp, _volnp)

    sumvW = np.sum(_divValWeightnp)
    sumvV = np.sum(_divValVolnp)

    _firstFactor = np.divide(_divValWeightnp, sumvW)
    _secondFactor = np.divide(_divValVolnp, sumvV)
    _prod = np.array(_firstFactor+_secondFactor)

    _indexSort = np.array(np.argsort(_prod))
    _divSort = np.sort(_prod)

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
        if(truck2Space(itemList[x][0]) == True):
            truck2ItemList.append(itemList[x][0])
        elif(truck1Space(itemList[x][0]) == True):
            truck1ItemList.append(itemList[x][0])
        else:
            break

    #New search
    otherList = []
    for y in range(len(itemList)-1,-1,-1):
        if(itemList[y][0] not in truck1ItemList and itemList[y][0] not in truck2ItemList ):
            otherList.append(itemList[y][0])

    for z in otherList:
        if(truck1Space(z) == True):
            truck1ItemList.append(z)
            print("\nNew search: Truck 1: add item "+str(z))
        elif(truck2Space(z) == True):
            truck2ItemList.append(z)
            print("\nNew search: Truck 2: add item "+str(z))

    cprint("--------------------------", 'red')
    print("Truck 1 items: ", truck1ItemList)
    print("Truck 1 Weight: "+str(_trucks[0][0]))
    print("Truck 1 Vol: "+str(_trucks[0][1]))
    print("Truck 1 Value: "+str(_trucks[0][2]))
    cprint("--------------------------", 'red')

    cprint("--------------------------", 'green')
    print("Truck 2 items: ", truck2ItemList)
    print("Truck 2 Weight: "+str(_trucks[1][0]))
    print("Truck 2 Vol: "+str(_trucks[1][1]))
    print("Truck 2 Value: "+str(_trucks[1][2]))
    cprint("--------------------------", 'green')
    cprint("\nTotal value: ", "yellow", end="")
    print(int(_trucks[0][2])+int(_trucks[1][2]))

addItem()
