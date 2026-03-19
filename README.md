# Crypto_price_predictor
A neural network-based cryptocurrency price prediction system that analyzes historical market data to forecast short-term price movements. The model leverages time-series architectures such as LSTMs and feedforward networks, incorporates engineered technical indicators, and evaluates predictive accuracy through backtesting simulations.
# 3/15  
  - Wrote my first RNN python script to predict 4th element in a sequence
  - more familiar with activator functions 'relu','tanh','sigmoid' and weigth calculating algorithms like adam
  - more knowledge on tensorflow syntax and data cleaning methods in numpy
  - learned about overfitting and undefitting as well as picking the right amount of neurons and epoch based on the dataset being used
# 3/16 (planning)
  - Before we begin pulling and cleaning and managing crypto data I want to test out and run different scenarios with RNN's, first up "Predicting a teams  point outcome from the nba"
  - I will be pulling my dataset from the nba-api cleaning to fit the model with the architecture as follows:      
            context: we will be using the formula -> team score = (team_ppg + opponent_points_allowed)/2
  - Going to set up data for the model as x = [team_ppg,  opponents_points_allowed,  result from formula] , y = [actual outcome]
  - this is the data that the model will learn from , I will also be implementing the model.save() method from tensorflow to save my model for finer tuning by adding more features(variables) in the x array
  - I will also touch up and learn more on activation functions and weight calculating algorithms as well as testing the model to get a more accurate units(neurons) to epoch ratio
# 3/18 - Data
  - Began pulling data from the nba-api, gathered from teams and teaminfocommon endpoints. Ran into an issue where nba-data.py wouldnt show any output despite not having any errors in my code so still got to fix that.
      - Left my pc on sleep for an entire day so my machine could be the issue 
      - could also be a wifi issue when trying to access the api
      - disregarded rate limit issue since after a sleep() addition to the code we got the same empty output
  - Realized that having the result of (ppg + opponent allowed(ofpo))/2, as a feature in x[] to my model was useless since I would basically be showing the model what the pattern is instead of it deciphering the pattern from the data its given so it was just redundent and would make my model fall apart, therefore ive chosen to go with x[ppg,ofpo] and y [outcome]
  - Next ill probably continue cleaning data and reading more on activator functions as well as algorithms like adam and which are the best for this scenario
  - Ive also read up on monte carlo simulations which could also be very helpful in determining the accuracy of my models prediction

