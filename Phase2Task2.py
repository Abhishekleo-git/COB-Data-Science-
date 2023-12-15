import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import requests
from io import BytesIO

# Define the URLs for the datasets
train_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRTK2NvcndgPX41Czu6Ft2Ho_nE-z50BgTqdzwFW0rsJ2nvyNLe2DoIg1COzUbgw80oaRBjfy5-WtFk/pub?output=xlsx"
test_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRyvZ7lknwiSghK9aen1SaTEYoN3JS40rrGLpcyrsVZy1tB2T4gn6Y3-cdzPUFCPMmmqREWefW3kl4_/pub?output=xlsx"

# Download the datasets
response_train = requests.get(train_url)
response_test = requests.get(test_url)

# Read the downloaded XLSX files
train_df = pd.read_excel(BytesIO(response_train.content))
test_df = pd.read_excel(BytesIO(response_test.content))

X_train = train_df[['X']]
y_train = train_df['y']

X_test = test_df[['X']]
y_true = test_df['y']

# Train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_true, y_pred)
print(f'Mean Squared Error: {mse}')

# Visualize predictions against actual values
plt.scatter(X_test, y_true, color='black', label='Actual')
plt.plot(X_test, y_pred, color='blue', linewidth=3, label='Predicted')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Linear Regression Prediction')
plt.legend()
plt.show()
