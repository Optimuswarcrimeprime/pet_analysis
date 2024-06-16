import unittest
import pandas as pd
from datetime import datetime
import pet_analysis as pa

class TestPetAnalysis(unittest.TestCase):

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

    def test_load_data(self):
        df = pa.load_data('pets.csv')
        self.assertEqual(list(df.columns), ['PetID', 'Name', 'Birthdate', 'Price', 'Species', 'SpecialFeature'])
        self.assertGreater(len(df), 0)

    def test_clean_data(self):
        cleaned_df = pa.clean_data(self.df)
        self.assertFalse(cleaned_df.isnull().values.any())
        self.assertEqual(cleaned_df['Price'].dtype, 'float64')
        self.assertEqual(cleaned_df['Species'].dtype.name, 'category')
        self.assertEqual(cleaned_df['SpecialFeature'].dtype.name, 'category')
        self.assertTrue(pd.api.types.is_datetime64_any_dtype(cleaned_df['Birthdate']))
        self.assertIn('Age', cleaned_df.columns)

    def test_calculate_average_price(self):
        avg_price = pa.calculate_average_price(self.df, 'Cat')
        self.assertEqual(avg_price, 183.33333333333334)

    def test_find_pets_with_feature(self):
        pets_with_feature = pa.find_pets_with_feature(self.df, 'yes')
        self.assertEqual(pets_with_feature, ['Fluffy', 'Bella', 'Charlie'])

    def test_get_species_statistics(self):
        stats = pa.get_species_statistics(self.df)
        self.assertIn('Cat', stats)
        self.assertIn('Dog', stats)
        self.assertEqual(stats['Cat']['Average Price'], 183.33333333333334)
        self.assertEqual(stats['Dog']['Average Price'], 225.0)

    def test_plot_price_distribution(self):
        pa.plot_price_distribution(self.df)

    def test_plot_average_price_by_species(self):
        pa.plot_average_price_by_species(self.df)

    def test_plot_price_vs_age(self):
        pa.plot_price_vs_age(self.df)

    def test_plot_age_distribution_by_species(self):
        pa.plot_age_distribution_by_species(self.df)

if __name__ == '__main__':
    unittest.main()
