# Function to split time series data into:
#   n consecutive time steps of data as X
#   and 1 time step of data as y

import numpy as np
def split_data(data, n_steps):
    X, y = list(), list()
    for i in range(len(data)):
        # index of last element for each grouping of steps
        end_ix = i + n_steps
    # break condition at the end of the sequence
        if end_ix > len(data)-1:
            break
        # X = first n elements, y = the element after
        seq_x, seq_y = data[i:end_ix], data[end_ix]
        X.append(seq_x)
        y.append(seq_y)
    return np.array(X), np.array(y)


# Function to decompose time series data into its components

from statsmodels.tsa.seasonal import seasonal_decompose
def decomp_list(data, groups):
    decomp, titles = [], []
    for group in groups:
        d    = seasonal_decompose(data[group],model='additive')
        decomp.append(data[group])
        titles.append('Before decompose: Group {g}'.format(g=group))
        decomp.append(d.trend)
        titles.append('Trend: Group {g}'.format(g=group))
        decomp.append(d.seasonal)
        titles.append('Seasonality: Group {g}'.format(g=group))
        decomp.append(d.resid)
        titles.append('Residual: Group {g}'.format(g=group))
    return decomp, titles


# Function to generate exog variables

import pandas as pd
def exog_days(data):
    exog_days = pd.DataFrame(data.index)
    exog_days['wkday']  = exog_days['date_time'].dt.dayofweek
    for day in range(0,7):
        col_name = 'day{d}'.format(d=day)
        exog_days[col_name] = exog_days['wkday'].map(lambda row: 1 if row==day else 0)
    exog_days = exog_days.iloc[:,2:].values
    return exog_days


# Function to generate SARIMA prediction and combine into dataframe
# together with test data

from sklearn.preprocessing import StandardScaler, MinMaxScaler
from statsmodels.tsa.statespace.sarimax import SARIMAX
import pandas as pd
import numpy as np

def sarima_mse(model, data, scaler, test_start, test_plot_weeks):
    one_week   = pd.Timedelta(hours=7*24)
    test_end   = test_start + one_week * test_plot_weeks
    data_test0 = data[test_start : test_end]

    # Standardized test data:
    scaler = scaler.fit(np.array(data_test0).reshape(-1, 1))
    data_test = scaler.transform(np.array(data_test0).reshape(-1, 1)).ravel()
    data_test = pd.DataFrame(data_test, index=data_test0.index)

    # Standardized predictions:
    # Calc prediction
    pred = model.predict(start=test_start, end=test_end, dynamic=True)
    # Calc confidence interval
    pred_conf = model.get_forecast(len(pred)).conf_int()
    # Calc confidence intervals
    pc_upper = pred_conf.iloc[:,1]
    pc_lower = pred_conf.iloc[:,0]

    # Non-standardized predictions:
    if scaler!=None:  
        # Inverse transform then calc prediction
        pred0 = scaler.inverse_transform(np.array(pred).reshape(-1, 1))
        pred0 = pd.DataFrame(pred0, index=data_test0.index)
        # Inverse transform then calc confidence interval
        pred_conf0 = scaler.inverse_transform(pred_conf)
        pred_conf0 = pd.DataFrame(pred_conf0, index=data_test0.index,
                                  columns=['upper 1','lower 1'])
        # Calc confidence intervals
        pc_upper0 = pred_conf0.iloc[:,1]
        pc_lower0 = pred_conf0.iloc[:,0]
    
    return data_test, pred, pc_upper, pc_lower, data_test0, pred0, pc_upper0, pc_lower0


# Function to create 'roads' on grid map

def fill_roads(array, horiz=1, fixed=0, start=0, stop=0, fill=1):
    if horiz == 1:
        for col in range(start, stop+1):
            array[fixed][col] = fill
    else:
        for row in range(start, stop+1):
            array[row][fixed] = fill
    return array


# Static data on roads to be plotted on map

def fetch_map_data():
    horiz_roads = [[1,  7, 18, 22],
                   [1, 10,  0, 68], # format: horiz=1, row, start_col, end_col
                   [1, 18,  0, 68],
                   [1, 26,  2, 66],
                   [1, 30, 43, 65],
                   [1, 34,  0, 68],
                   [1, 42,  0, 68],
                   [1, 50, 16, 52],
                   [1, 58, 16, 36]]

    vert_roads  = [[0,  2,  0, 44], # format: horiz=0, col, start_row, end_col
                   [0, 10,  0, 44],
                   [0, 18,  8, 60],
                   [0, 22,  0,  6],
                   [0, 26, 11, 60],
                   [0, 34, 11, 60],
                   [0, 42,  0, 52],
                   [0, 50, 11, 52],
                   [0, 58,  0, 44],
                   [0, 66, 11, 41]]
    
    yarra_river =  [[1, 0, 52, 54], # format: horiz=1, row, start_col, end_col
                    [1, 1, 52, 54],
                    [1, 2, 52, 54],
                    [1, 3, 51, 54],
                    [1, 4,  0, 54],
                    [1, 5,  0, 53],
                    [1, 6,  0, 52]]
    
    return horiz_roads, vert_roads, yarra_river


# Static labels to be plotted on map

def fetch_map_label():
    road_labels = [[14, 10, 0,  'Flinders Street'], # format: x, y, rotation, name
                   [14, 18, 0,  'Collins Street'],
                   [14, 26, 0,  'Bourke Street'],
                   [14, 34, 0,  'Lonsdale Street'],
                   [14, 42, 0,  'La Trobe Street'],
                   [54, 10, 0,  'Flinders Street'],
                   [54, 18, 0,  'Collins Street'],
                   [54, 26, 0,  'Bourke Street'],
                   [54, 30, 0,  'Chinatown'],
                   [54, 34, 0,  'Lonsdale Street'],
                   [54, 42, 0,  'La Trobe Street'],
                   [26, 58, 0,  'Victoria St'],
                   [34, 50, 0,  'Franklin Street'],
                   [ 2, 26, 90, 'Spencer Street'],
                   [10, 26, 90, 'King Street'],
                   [18, 26, 90, 'William Street'],
                   [26, 26, 90, 'Queen Street'],
                   [34, 26, 90, 'Elizabeth Street'],
                   [42,  5, 90, 'Princes Bridge'],
                   [42, 26, 90, 'Swanston Street'],
                   [50, 26, 90, 'Russell Street'],
                   [58, 26, 90, 'Exhibition Street'],
                   [66, 26, 90, 'Spring Street'],]

    # Label buildings on map
    area_labels = [[ 0, 26, 90, 'Southern Cross Station'],
                   [22, 54,  0, 'Victoria\nMarket'],
                   [30, 54,  0, 'Victoria\nMarket'],
                   [32,  7,  0, 'Flinders'],
                   [33,  1,  0, 'Southbank Promenade'],
                   [37,  7,  0, 'Street Station'],
                   [38, 15,  0, 'City Library'],
                   [38, 29,  0, 'Myers &\nDavidJones'],
                   [38, 23,  0, 'Bourke St\nMall'],
                   [38, 32,  0, 'Emporium'],
                   [38, 38,  0, 'Melbourne\nCentral'],
                   [39,  1,  0, 'Arts\nCentre'],
                   [45, 12,  0, "St Paul's"],
                   [45, 16,  0, 'City Square'],
                   [45, 20,  0, 'Town Hall'],
                   [47,  8,  0, 'Federation Square'],
                   [46, 27,  0, 'Target'],
                   [46, 36,  0, 'QV'],
                   [46, 39,  0, 'State\nLibrary'],
                   [46, 44,  0, 'RMIT Univ'],
                   [47, 22,  0, 'QT'],
                   [55, 21,  0, 'Nauru\nHouse'],
                   [63, 28,  0, 'Princess\nTheatre'],
                   [68, 26, 90, 'State Parliament']]

    # Label tram lines
    tram_lines_h = [[7.5,  18.5, 22.5],
                    [10.5,  2.5, 11.5],
                    [10.5, 17.5, 51.5],
                    [10.5, 57.5,   69],
                    [18.5,  2.5,   12],
                    [18.5, 17.5,   52],
                    [18.5, 57.5,   69],
                    [26.5,  2.5, 11.5],
                    [26.5, 17.5, 51.5],
                    [26.5,   57,   66],
                    [42.5,  2.5, 11.5],
                    [42.5,   18, 51.5],
                    [42.5,   57,   69]]

    tram_lines_v = [[ 2.5,    0,   23],
                    [ 2.5, 29.5,   45],
                    [18.5,  7.5,   23],
                    [18.5,   29.5, 61],
                    [22.5,    0,  7.5],
                    [34.5, 10.5,   23],
                    [34.5, 29.5,   50],
                    [34.5,   51,   61],
                    [42.5,    0,  1.5],
                    [42.5,    9,   23],
                    [42.5, 29.5,   53],
                    [66.5, 11.5,   23],
                    [66.5, 29.5, 42.5]]
    
    return road_labels, area_labels, tram_lines_h, tram_lines_v