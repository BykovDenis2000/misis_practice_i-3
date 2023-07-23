import json
import numpy as np
import os
import pandas as pd
import pickle
import sys



def data_preparation(row):
    # getting loading_* params
    lw = row['cargo_space']['size']['width']
    lh = row['cargo_space']['size']['height']
    ll = row['cargo_space']['size']['length']
    
    # normalizing box size params
    cargoes = row['cargo_groups']
    w, h, l, t, s = [], [], [], [], []
    
    for cargo in cargoes:
        count = int(cargo['count'])
        size_width = cargo['size']['width']
        size_height = cargo['size']['height']
        size_length = cargo['size']['length'] 
        turnover = int(cargo['turnover'])
        stacking = int(cargo['stacking'])
        
        # append the values count times
        w.extend([size_width] * count)
        h.extend([size_height] * count)
        l.extend([size_length] * count)
        t.extend([turnover] * count)
        s.extend([stacking] * count)
    
    w = np.array(w) / lw
    h = np.array(h) / lh
    l = np.array(l) / ll
    t = np.array(t)
    s = np.array(s)
    
    # make custom params
    w_t = w[t == 1]
    h_t = h[t == 1]
    l_t = l[t == 1]
    v_t = w_t * h_t * l_t 
    w_nt = w[t == 0]
    h_nt = h[t == 0]
    l_nt = l[t == 0]
    v_nt = w_nt * h_nt * l_nt

    w_s = w[s == 1]
    h_s = h[s == 1]
    l_s = l[s == 1]
    v_s = w_s * h_s * l_s
    w_ns = w[s == 0]
    h_ns = h[s == 0]
    l_ns = l[s == 0]
    v_ns = w_ns * h_ns * l_ns
    
    # getting volume
    v = w * h * l
    
    # used quantiles
    qs = [0, 0.2, 0.4, 0.6, 0.8, 1]
    return {
        "mean_width": w.mean(),
        "mean_height": h.mean(),
        "mean_length": l.mean(),
        "mean_volume": v.mean(),
        "std_width" : w.std(),
        "std_height" : h.std(),
        "std_length" : l.std(),
        "std_volume" : v.std(),
        "sum_width": w.sum(),
        "sum_height": h.sum(),
        "sum_length": l.sum(),
        "sum_volume": v.sum(),
        "mean_turnover": t.mean(),
        "mean_stacking": s.mean(),
        
        "mean_width_turnover": w_t.mean(),
        "mean_height_turnover": h_t.mean(),
        "mean_length_turnover": l_t.mean(),
        "mean_volume_turnover": v_t.mean(),
        "std_width_turnover" : w_t.std(),
        "std_height_turnover" : h_t.std(),
        "std_length_turnover" : l_t.std(),
        "std_volume_turnover" : v_t.std(),
        "sum_width_turnover": w_t.sum(),
        "sum_height_turnover": h_t.sum(),
        "sum_length_turnover": l_t.sum(),
        "sum_volume_turnover": v_t.sum(),
        
        "mean_width_no_turnover": w_nt.mean(),
        "mean_height_no_turnover": h_nt.mean(),
        "mean_length_no_turnover": l_nt.mean(),
        "mean_volume_no_turnover": v_nt.mean(),
        "std_width_no_turnover" : w_nt.std(),
        "std_height_no_turnover" : h_nt.std(),
        "std_length_no_turnover" : l_nt.std(),
        "std_volume_no_turnover" : v_nt.std(),
        "sum_width_no_turnover": w_nt.sum(),
        "sum_height_no_turnover": h_nt.sum(),
        "sum_length_no_turnover": l_nt.sum(),
        "sum_volume_no_turnover": v_nt.sum(),
        
        "mean_width_stacking": w_s.mean(),
        "mean_height_stacking": h_s.mean(),
        "mean_length_stacking": l_s.mean(),
        "mean_volume_stacking": v_s.mean(),        
        "std_width_stacking" : w_s.std(),
        "std_height_stacking" : h_s.std(),
        "std_length_stacking" : l_s.std(),
        "std_volume_stacking" : v_s.std(),
        "sum_width_stacking": w_s.sum(),
        "sum_height_stacking": h_s.sum(),
        "sum_length_stacking": l_s.sum(),
        "sum_volume_stacking": v_s.sum(),
        
        "mean_width_no_stacking": w_ns.mean(),
        "mean_height_no_stacking": h_ns.mean(),
        "mean_length_no_stacking": l_ns.mean(),
        "mean_volume_no_stacking": v_ns.mean(),
        "std_width_no_stacking" : w_ns.std(),
        "std_height_no_stacking" : h_ns.std(),
        "std_length_no_stacking" : l_ns.std(),
        "std_volume_no_stacking" : v_ns.std(),
        "sum_width_no_stacking": w_ns.sum(),
        "sum_height_no_stacking": h_ns.sum(),
        "sum_length_no_stacking": l_ns.sum(),
        "sum_volume_no_stacking": v_ns.sum(),
        **{
            "width_p{}".format(int(q * 100)): np.quantile(w, q) for q in qs
        },
        **{
            "heigth_p{}".format(int(q * 100)): np.quantile(h, q) for q in qs
        },
        **{
            "length_p{}".format(int(q * 100)): np.quantile(l, q) for q in qs
        },
        **{
            "volume_p{}".format(int(q * 100)): np.quantile(v, q) for q in qs
        },
        **{
            "width_turning_p{}".format(int(q * 100)): -1 if len(w_t) == 0 else np.quantile(w_t, q) for q in qs
        },
        **{
            "heigth_turning_p{}".format(int(q * 100)): -1 if len(h_t) == 0 else np.quantile(h_t, q) for q in qs
        },
        **{
            "length_turning_p{}".format(int(q * 100)): -1 if len(l_t) == 0 else np.quantile(l_t, q) for q in qs
        },
        **{
            "volume_turning_p{}".format(int(q * 100)): -1 if len(v_t) == 0 else np.quantile(v_t, q) for q in qs
        },
        **{
            "width_stacking_p{}".format(int(q * 100)): -1 if len(w_s) == 0 else np.quantile(w_s, q) for q in qs
        },
        **{
            "heigth_stacking_p{}".format(int(q * 100)): -1 if len(h_s) == 0 else np.quantile(h_s, q) for q in qs
        },
        **{
            "length_stacking_p{}".format(int(q * 100)): -1 if len(l_s) == 0 else np.quantile(l_s, q) for q in qs
        },
        **{
            "volume_stacking_p{}".format(int(q * 100)): -1 if len(v_s) == 0 else np.quantile(v_s, q) for q in qs
        },
#         "loading_width": lw,
#         "loading_height": lh,
#         "loading_length": ll,
        
# labels
    }

def distrib(x):
    # used for bootstrapping
    return np.random.normal(x / 50)

def bootstrap(row):
    # used for increasing dataset size
    row['cargo_space']['size']['width'] += distrib(row['cargo_space']['size']['width'])
    row['cargo_space']['size']['height'] += distrib(row['cargo_space']['size']['height'])
    row['cargo_space']['size']['length'] += distrib(row['cargo_space']['size']['length'])
    return row

try:
    path = sys.argv[1]
except IndexError as e:
    print('\033[93m' + 'No path added\n','Add the path off the file in the terminal like this:\n python EstimateDensity.py test.json'.format(e))
    sys.exit()
data = []
with open(path, 'r', encoding='utf-8') as f:
    raw = json.load(f)
    data.append(data_preparation(raw))
    
df = pd.DataFrame(data)
df[df.isna()] = -1

linear_model = pickle.load(open('Saved_Models/LinearRegression.sav', 'rb'))
linear_predict = linear_model.predict(df)

df['reg_predict'] = linear_predict
catboost_model = pickle.load(open('Saved_models/CatBoostRegressor.sav', 'rb'))
print('Estimated density percent:', catboost_model.predict(df)[0])
