# Knapsack-problem(TSO)

## Project for TSO
- **Truck 1**: 3,500kg/1,200cm^3
- **Truck 2**: 16,000kg/4,000cm^3

![Trucks](https://i.imgur.com/DZ0EY44.png)
## Menu
![Menu](https://i.imgur.com/LPe98aO.png)

## Equation:
### (Value/weight)/(Σ(val/w)) + (Value/vol)/(Σ(val/vol))

```python
_divValWeightnp = np.divide(_valuenp, _weightnp)
_divValVolnp = np.divide(_valuenp, _volnp)

sumvW = np.sum(_divValWeightnp)
sumvV = np.sum(_divValVolnp)

_firstFactor = np.divide(_divValWeightnp, sumvW)
_secondFactor = np.divide(_divValVolnp, sumvV)
_prod = np.array(_firstFactor+_secondFactor)
```
## Instances
### [Source](https://github.com/irisabril/TSO-FIME-2018)
