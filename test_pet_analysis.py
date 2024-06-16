import unittest  # Importing the unittest module
import pandas as pd  # Importing pandas for DataFrame manipulation
from datetime import datetime  # Importing datetime for date operations
import pet_analysis as pa  # Importing the pet_analysis module as pa

# Creating a test class that inherits from unittest.TestCase
class TestPetAnalysis(unittest.TestCase):

    # Setting up the test data
    def setUp(self):
        data = {
            'Name': ['Fluffy', 'Spot', 'Bella', 'Max', 'Charlie'],
            'Birthdate': ['2020-01-01', '2019-05-15', '2018-07-20', '2021-02-25', '2017-12-10'],
            'Price': [100, 200, 150, 250, 300],
            'Species': ['Cat', 'Dog', 'Cat', 'Dog', 'Cat'],
            'SpecialFeature': ['yes', 'no', 'yes', 'no', 'yes']
        }
        self.df = pd.DataFrame(data)
        self.df['Birthdate'] = pd.to_datetime(self.df['Birthdate'])

    # Test for the load_data function
    def test_load_data(self):
        # Calling the load_data function with a sample file path
        df = pa.load_data('pets.csv')
        # Asserting that the columns of the DataFrame are as expected
        self.assertEqual(list(df.columns), ['PetID', 'Name', 'Birthdate', 'Price', 'Species', 'SpecialFeature'])
        # Asserting that the DataFrame is not empty
        self.assertGreater(len(df), 0)

    # Test for the clean_data function
    def test_clean_data(self):
        # Calling the clean_data function with the test DataFrame
        cleaned_df = pa.clean_data(self.df)
        # Asserting that there are no missing values in the cleaned DataFrame
        self.assertFalse(cleaned_df.isnull().values.any())
        # Asserting that the 'Price' column is of the correct data type
        self.assertEqual(cleaned_df['Price'].dtype, 'float64')
        # Asserting that the 'Species' and 'SpecialFeature' columns are categorical
        self.assertEqual(cleaned_df['Species'].dtype.name, 'category')
        self.assertEqual(cleaned_df['SpecialFeature'].dtype.name, 'category')
        # Asserting that the 'Birthdate' column is datetime
        self.assertTrue(pd.api.types.is_datetime64_any_dtype(cleaned_df['Birthdate']))
        # Asserting that the 'Age' column is present in the cleaned DataFrame
        self.assertIn('Age', cleaned_df.columns)

    # Test for the calculate_average_price function
    def test_calculate_average_price(self):
        # Calculating the average price for the 'Cat' species in the test DataFrame
        avg_price = pa.calculate_average_price(self.df, 'Cat')
        # Asserting that the calculated average price is correct
        self.assertEqual(avg_price, 183.33333333333334)

    # Test for the find_pets_with_feature function
    def test_find_pets_with_feature(self):
        # Finding pets with the 'yes' special feature in the test DataFrame
        pets_with_feature = pa.find_pets_with_feature(self.df, 'yes')
        # Asserting that the list of pets with the feature is correct
        self.assertEqual(pets_with_feature, ['Fluffy', 'Bella', 'Charlie'])

    # Test for the get_species_statistics function
    def test_get_species_statistics(self):
        # Calculating species statistics for the test DataFrame
        stats = pa.get_species_statistics(self.df)
        # Asserting that 'Cat' and 'Dog' species are in the statistics
        self.assertIn('Cat', stats)
        self.assertIn('Dog', stats)
        # Asserting that the average prices for 'Cat' and 'Dog' are correct
        self.assertEqual(stats['Cat']['Average Price'], 183.33333333333334)
        self.assertEqual(stats['Dog']['Average Price'], 225.0)

    # Test for the plot_price_distribution function
    def test_plot_price_distribution(self):
        # Plotting the price distribution for the test DataFrame
        pa.plot_price_distribution(self.df)

    # Test for the plot_average_price_by_species function
    def test_plot_average_price_by_species(self):
        # Plotting the average price by species for the test DataFrame
        pa.plot_average_price_by_species(self.df)

    # Test for the plot_price_vs_age function
    def test_plot_price_vs_age(self):
        # Plotting the price vs. age scatter plot for the test DataFrame
        pa.plot_price_vs_age(self.df)

    # Test for the plot_age_distribution_by_species function
    def test_plot_age_distribution_by_species(self):
        # Plotting the age distribution by species for the test DataFrame
        pa.plot_age_distribution_by_species(self.df)

# Running the tests if the script is executed as the main module
if __name__ == '__main__':
    unittest.main()
