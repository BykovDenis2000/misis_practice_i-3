# misis_practice_i-3
### Forecasting of cargo stowage density
To predict the density of cargo stowage, it is necessary to have a json file of this structure:
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
Here in cargo_space the dimensions of the cargo space are written, and in cargo_groups the boxes with their characteristics are listed.
### Example of running the program
In test.json is an example of data for which using EstimateDensity.py you can predict the stacking densities in this way:
```python
python EstimateDensity.py test.json
```
```shell
Estimated density percent: 0.8999495600313133
```
