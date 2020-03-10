# Pedestrian Traffic Forecasting in Melbourne City Centre
### by Khairul Omar | <a href="mailto:khairul.omar@gmail.com">khairul.omar@gmail.com</a> | <a href="https://www.linkedin.com/in/khairulomar/">LinkedIn</a>

<img src="/images/heat_map_animate.gif">

## Key project files:
1. <a href="https://nbviewer.jupyter.org/github/khairulomar/Melbourne_pedestrian/blob/master/Melbourne_pedestrian.ipynb?flush_cache=true">Main Python codes Jupyter notebook</a>
2. <a href="https://github.com/khairulomar/Melbourne_pedestrian/blob/master/library.py">Python formulas library Jupyter notebook</a>
1. <a href="https://github.com/khairulomar/Melbourne_pedestrian/blob/master/Melbourne_pedestrian.pdf">Stakeholder presentation slides</a>

## Project Objective
Melbourne was voted world's most liveable city for six consecutive years between 2012 and 2017. The city centre, or more commonly referred to as the Central Business District (CBD), takes the shape of a one-mile by half-a-mile core grid that is home to most of the city's businesses. In order to better understand pedestrian traffic in the CBD, numerous sensors were installed at strategic locations all over the city that are designed to count people movements.
<p>
The city has made data from these sensors publically available and is updated on an hourly basis. While analysis can readily be done on historical data, there has not been much work on developing forecasting models to predict pedestrian traffic in the city. This project is aimed to address this gap into order to support various stakeholders, including the local government, Victoria State Police and business owners via a seven-day forecasting system.
<p>
<img src="/images/pedestrians.png">

## Project Methodology
Data from individual sensors was gathered via <a href="https://dev.socrata.com/foundry/data.melbourne.vic.gov.au/b2ak-trbp"> City of Melbourne Open Data API</a> interface. As the length of period and completeness of data varies by location, sample of sensors to be used for the project needed to be shortlisted and additional data cleansing was required to deal with missing data caused by outages.

The initial strategy for the project was to formulate a single model that could be applied to all locations. However, it appeared that this strategy may not be feasible as different traffic patterns started to emerge when all sensor locations were analysed based on their traffic volume, and by hour of the day and day of the week. Principle Component Analysis (PCA) technique was used to group different sensor locations into 3 groups, namely Group 1: Mix-use areas, Group 2: Office areas and Group 3: Leisure areas, as summarised in the normalized traffic plots below.

<img src="/images/EDA_groups.png">

Two machine learning techniques were identified as the main option due to the time series nature of the data to address the project objective. The first strategy for the forecasting model was based on Long Short-Term Memory (LSTM) which a configuration of recurrent neural network (RNN), followed by Seasonal Autoregressive Moving Average (SARIMA) model.

## Findings from modelling process
**LSTM** was initially expected to be the best candidate for modelling the time series data set as it has the capability to learn from past trends and seasonality, given the large amount of available data and the long training set used. However, despite generating low values of error calculations (including mean squared error), the predicted traffic behaves more like a sine wave that is not able to detect the intricacies of the hourly and daily variation. In addition, the the forecast also seem to deteriorate further beyond four days which falls short of our seven-day target.
<p>
  
**SARIMA** model was first trained and tested on Group 1 average, which performs significantly better than LSTM in predicting hourly and daily variations. The best performance was obtained with [(7,1,6)(2,1,2),168)] configuration over a seasonality period of one week (168 hours). When the generic Group 1 model was applied to individual Group 1 sensors, it was noted that locations with traffic patterns that are almost similar to Group 1 average (e.g. sites 30 and 35) performs better than others (e.g. sites 34 and 36) as shown in the seven-day prediction plots below.
<p>
<img src="/images/group1.png">
<p>
When the generic model is extended to Group 2 sites, the difference can be further observed below (e.g. sites 9 and 18) as the traffic pattern in office areas behave significantly different to mixed-use location, particularly during weekends and peak commuting hours. From these results, it is concluded that group-level models would not generate the best performance at individual site level due to their individual characteristics that cannot be easily generalized.
<p>
<img src="/images/group2.png">
<p>
For the rollout of this project, it was decided that each site is to be trained individually at site level using its own respective group hyperparameters in order to generate the best level of performance. The fact that SARIMA model is relatively fast to train is an added bonus when the model needs to be updated with more recent data in the future.

Below is an example of how pedestrian traffic forecast data can be presented to stakeholders for a single site, focusing on the hourly variation of a single day and followed by a seven-day view of longer-term needs.
<p>
<img src="/images/one_week_plot.png">
<p>
In this project, pedestrian traffic forecast is also visualised in the form of animated heat map of the CBD (shown at the beginning of this page) which displays traffic pattern at different hour of the day at all sensor locations. This would serve as highly effective method in conveying the information in a quick and meaningful way to most stakeholders.
  
## Business Applications

Multiple stakeholders that could benefit from a good pedestrian forecasting system in Melbourne CBD have been identified. This model can also be readily extended to other cities around the world to take advantage of similar benefits as summarized below.

1. To the state police and traffic police: by anticipating busy periods, staffing resources can be allocated appropriately to manage the traffic flow and the potential increase in crime.

2. To security services and the state police: Melbourne has had two terror attacks recently whereby vehicles rammed into pedestrian paths in the CBD. The forecasting model may help to assess risk factors that can be acted upon.

3. To the city council: by understanding the traffic pattern and projected growth, city planning policies can be formulated to achieve best practice outcomes, including improving public walkability experience and the possibility of turning some streets into pedestrian-only zones.

4. To the business community and property owners: untapped opportunities may emerge from the study, such as identifying new trends in previously under-visited areas of the city centre. A forecasting model would also help the real estate industry to evaluate forecast property price trends in different parts of the city.

5. To the general public: a given day's itinerary can be planned in advance in order to avoid large crowds by anticipating peak periods at specific locations of interest.
