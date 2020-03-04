# Pedestrian Traffic Forecasting in Melbourne City Centre
### by Khairul Omar

<img src="/images/pedestrians.png">

Key files:
1. <a href="https://github.com/khairulomar/Melbourne_pedestrian/blob/master/Melbourne_pedestrian.ipynb">Main Jupyter notebook</a>
2. <a href="https://github.com/khairulomar/Melbourne_pedestrian/blob/master/library.py">Python formulas Jupyter notebook</a>
1. <a href="https://docs.google.com/presentation/d/1mdEAQ9iz1uUEMc6Xku6apKgG_EvlaO9VxIGmaZn40FA/edit?usp=sharing">Stakeholder presentation in Google Slides</a>

## Project objective
Melbourne was voted world's most liveable city for 6 consecutive years between 2012 and 2017 for its high quality of life. The city centre, more commonly known as the Central Business District (CBD) takes the shape of a one-mile by half-a-mile core grid that is home to most of the city's businesses. Since 2010, the city has rolled out sensors that counts hourly pedestrian traffic at various strategic locations all over the CBD.
<p>
The city has made data from the sensors publically available and is updated on an hourly basis. While analysis can readily be done on historical data, there has not been much work on developing forecasting models to predict future pedestrian traffic in the city. This project is aimed to address this gap into order to support various stakeholders, including the local government authority, Victoria State Police and business owners via a 7-day forecasting system.

## Methodology
Data from individual sensors was gathered via <a href="https://dev.socrata.com/foundry/data.melbourne.vic.gov.au/b2ak-trbp"> City of Melbourne Open Data API</a> interface. As the sensors were installed at different times and there has been intermittent outages at several locations which sometimes lasted for weeks or months, the list of sensors to be used for the project is shortlisted and additional data cleansing was required to deal with the missing data.

The initial strategy for the project was to formulate a single generic model that could be applied to all locations. However, it appeared that this strategy may not be feasible as different traffic patterns started to emerge when all sensor locations were investigated based on their traffic volume and by hour of the day and day of the week. Principle Component Analysis (PCA) was used to group the different locations into 3 groups: mix used sites, business sites and leisure sites as summarised in the plots below.

<img src="/images/EDA_groups.png">

Two machine learning techniques were identified as prime candidates due to the time series nature of the data and project objective. First strategy for the forecasting model was based on Long Short-Term Memory (LSTM), a recurrent neural network (RNN) and followed by Seasonal Autoregressive Moving Average (SARIMA) model.

## Findings
LSTM was initially expected as the best candidate for modelling the time series data set as it would be able to learn from past trends and seasonality, given the large amount of available data and the long training set used. However, despite generating low value of various error calculations (including mean squared error), the predicted traffic behaves more like a sine wave that is not able to detect the intricacies of the hourly and daily variation. In addition, the the forecast also seem to deteriorate further beyond 4 days which fall short of our 7-day target.
<p>
Explain SARIMA - what is it - hyper parameters
<p>
Explain results of group 1
<img src="/images/SARIMA_group1.png">
<p>
<img src="/images/SARIMA_group2.png">
<p>

## Recommendations
