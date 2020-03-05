# Pedestrian Traffic Forecasting in Melbourne City Centre
### by Khairul Omar

<img src="/images/pedestrians.png">

Key files:
1. <a href="https://github.com/khairulomar/Melbourne_pedestrian/blob/master/Melbourne_pedestrian.ipynb">Main Jupyter notebook</a>
2. <a href="https://github.com/khairulomar/Melbourne_pedestrian/blob/master/library.py">Python formulas Jupyter notebook</a>
1. <a href="https://docs.google.com/presentation/d/1mdEAQ9iz1uUEMc6Xku6apKgG_EvlaO9VxIGmaZn40FA/edit?usp=sharing">Stakeholder presentation in Google Slides</a>

## Project objective
Melbourne was voted world's most liveable city for six consecutive years between 2012 and 2017. The city centre, or more commonly referred to as the Central Business District (CBD), takes the shape of a one-mile by half-a-mile core grid that is home to most of the city's businesses. In order to better understand pedestrian traffic in the CBD, numerous sensors were installed at strategic locations all over the city that are designed to count people movements.
<p>
The city has made data from these sensors publically available and is updated on an hourly basis. While analysis can readily be done on historical data, there has not been much work on developing forecasting models to predict pedestrian traffic in the city. This project is aimed to address this gap into order to support various stakeholders, including the local government, Victoria State Police and business owners via a seven-day forecasting system.

## Methodology
Data from individual sensors was gathered via <a href="https://dev.socrata.com/foundry/data.melbourne.vic.gov.au/b2ak-trbp"> City of Melbourne Open Data API</a> interface. As the length of period and completeness of data varies by location, sample of sensors to be used for the project needed to be shortlisted and additional data cleansing was required to deal with missing data caused by outages.

The initial strategy for the project was to formulate a single model that could be applied to all locations. However, it appeared that this strategy may not be feasible as different traffic patterns started to emerge when all sensor locations were analysed based on their traffic volume, and by hour of the day and day of the week. Principle Component Analysis (PCA) technique was used to group different sensor locations into 3 groups, namely Group 1: Mix-use areas, Group 2: Business areas and Group 3: Leisure areas as summarised in the normalize traffic plots below.

<img src="/images/EDA_groups.png">

Two machine learning techniques were identified as prime candidates due to the time series nature of the data to address the project objective. The first strategy for the forecasting model was based on Long Short-Term Memory (LSTM) which a configuration of recurrent neural network (RNN), followed by Seasonal Autoregressive Moving Average (SARIMA) model.

## Findings
**LSTM** was initially expected to be the best candidate for modelling the time series data set as it has the capability to learn from past trends and seasonality, given the large amount of available data and the long training set used. However, despite generating low values of error calculations (including mean squared error), the predicted traffic behaves more like a sine wave that is not able to detect the intricacies of the hourly and daily variation. In addition, the the forecast also seem to deteriorate further beyond four days which falls short of our seven-day target.
<p>
  
**SARIMA** model was first trained and tested on Group 1 average, which performs significantly better than LSTM in predicting hourly and daily variations. The best performance was obtained with [(7,1,6)(2,1,2),168)] configuration over a seasonality period of one week (168 hours). When the generic Group 1 model was applied to individual Group 1 sensors, it was noted that locations with traffic patterns that are almost similar to Group 1 average (e.g. sites 30 and 35) performs better than others (e.g. sites 34 and 36) as shown in the seven-day prediction plots below.
<p>
<img src="/images/group1.png">
<p>
When the generic model is extended to Group 2 sites, the difference can be further observed below (e.g. sites 9 and 18) as the traffic pattern in business areas behave significantly different to mixed-use location, particularly during weekends and peak commuting hours. From these results, it is concluded that group-level models would not generate the best performance at individual site level due to their individual characteristics that cannot be easily generalized.
<p>
<img src="/images/group2.png">
<p>
For the rollout of this project, it was decided that each site is to be trained individually at site level using its own respective group hyperparameters in order to generate the best level of performance. The fact that SARIMA model is relatively fast to train is an added bonus when the model needs to be updated with more recent data in the future.
  
## Benefits to stakeholders

Security, city planning & business opportunities
<p>
Explain heat map
<p>
<img src="/images/one_week_plot.png">
<p>
Text here
<p>
<img src="/images/heat_map.png">
