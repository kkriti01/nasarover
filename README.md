# Scoll.in Assignment

## How to run program
Setup:
```
pip install -r requirements.txt
```
execute script:
```
python nasa.py
```
or
```
from nasa import NasaRover
rover = NasaRover()
rover.run()
```
enter impputs (e.g.):
```
5 5
1 2 N
LMLMLMLMM
3 3 E
MMRMMRMRRM
```

## Test
```
nosetests --with-coverage
```
