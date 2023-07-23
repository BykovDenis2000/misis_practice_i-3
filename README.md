# misis_practice_i-3
### Прогнозирование плотности укладки грузов
Для прогнозирования плотности укладки грузов необходимо иметь json файл такого типа:
```json

{
   "cargo_space": {
       "id": "1111",
       "mass": 20,
       "size": {
           "width": 800,
           "height": 2300,
           "length": 1200
       }
   },
   "cargo_groups": [
       {
           "mass": 6357,
           "size": {
               "width": 190,
               "height": 237,
               "length": 260
           },
           "sort": 1,
           "count": 1,
           "group_id": "11111",
           "stacking": true,
           "turnover": true,
           "overhang_angle": 50,
           "stacking_limit": 0,
           "stacking_is_limited": false
       }
   ]
}
```
Здесь в cargo_space написаны габариты грузового пространства, а в cargo_groups перечислены коробки с их характеристиками.
### Пример запуска программы
В test.json есть пример данных для которых с помощью EstimateDensity.py можно спрогнозировать плотности укладки таким образом:
```python
python EstimateDensity.py test.json
```
```shell
Estimated density percent: 0.8999495600313133
```
