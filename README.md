# Pedestrian Traffic Forecasting in Melbourne City Centre
### by Khairul Omar

<img src="/images/pedestrians.png">

Key files:
1. <a href="https://github.com/khairulomar/Melbourne_pedestrian/blob/master/Melbourne_pedestrian.ipynb">Main Jupyter notebook</a>
2. <a href="https://github.com/khairulomar/Melbourne_pedestrian/blob/master/library.py">Python formulas Jupyter notebook</a>
1. <a href="https://docs.google.com/presentation/d/1mdEAQ9iz1uUEMc6Xku6apKgG_EvlaO9VxIGmaZn40FA/edit?usp=sharing">Stakeholder presentation in Google Slides</a>

## Project objective
Melbourne was voted world's most liveable city for six consecutive years between 2012 and 2017. The city centre, more commonly referred to as the Central Business District (CBD), takes the shape of a one-mile by half-a-mile core grid that is home to most of the city's businesses. In order to learn about pedestrian traffic in the CBD, numerous sensors were installed at strategic locations all over the city that are designed to count people movements.
<p>
The city has made data from these sensors publically available and is updated on an hourly basis. While analysis can readily be done on historical data, there has not been much work on developing forecasting models to predict pedestrian traffic in the city. This project is aimed to address this gap into order to support various stakeholders, including the local government, Victoria State Police and business owners via a 7-day forecasting system.

## Methodology
Data from individual sensors was gathered via <a href="https://dev.socrata.com/foundry/data.melbourne.vic.gov.au/b2ak-trbp"> City of Melbourne Open Data API</a> interface. As the length of period and completeness of data varies by location, sample of sensors to be used for the project needed to be shortlisted and additional data cleansing was required to deal with missing data.

The initial strategy for the project was to formulate a single model that could be applied to all locations. However, it appeared that this strategy may not be feasible as different traffic patterns started to emerge when all sensor locations were analysed based on their traffic volume and by hour of the day and day of the week. Principle Component Analysis (PCA) technique was used to group different sensor locations into 3 groups: mix-use sites, business sites and leisure sites as summarised in the plots below.

<img src="/images/EDA_groups.png">

Two machine learning techniques were identified as prime candidates due to the time series nature of the data to address the project objective. The first strategy for the forecasting model was based on Long Short-Term Memory (LSTM) which a configuration of recurrent neural network (RNN), followed by Seasonal Autoregressive Moving Average (SARIMA) model.

## Findings
LSTM was initially expected to be the best candidate for modelling the time series data set as it has the capability to learn from past trends and seasonality, given the large amount of available data and the long training set used. However, despite generating low values of error calculations (including mean squared error), the predicted traffic behaves more like a sine wave that is not able to detect the intricacies of the hourly and daily variation. In addition, the the forecast also seem to deteriorate further beyond 4 days which falls short of our 7-day target.
<p>
Explain SARIMA - what is it - hyper parameters
<p>
Explain results of group 1. Plots: show only 1 column, not 2
<p>
<img src="/images/SARIMA_group1.png">
<p>
When result is extended to group 2 bla bla as below
<p>
<img src="/images/SARIMA_group2.png">

## Benefits to stakeholders

Security, city planning & business opportunities
<p>
Explain heat map
<p>
Add heatmap here
