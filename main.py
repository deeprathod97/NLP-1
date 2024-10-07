import pandas as pd
import numpy as np

# Create synthetic dataset
np.random.seed(42)
data_size = 100

square_footage = np.random.randint(500, 5000, data_size)
bedrooms = np.random.randint(1, 6, data_size)
bathrooms = np.random.randint(1, 4, data_size)
price = (square_footage * 0.1 + bedrooms * 10 + bathrooms * 5 + np.random.randn(data_size) * 10)

# Create DataFrame
house_data = pd.DataFrame({
    'SquareFootage': square_footage,
    'Bedrooms': bedrooms,
    'Bathrooms': bathrooms,
    'Price': price
})

# Save to CSV
house_data.to_csv('house_prices.csv', index=False)
print("Dataset created and saved as 'house_prices.csv'")