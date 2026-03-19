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
