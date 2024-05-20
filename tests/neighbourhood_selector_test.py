import unittest

from src.neighbourhood_selector import *


class NeighbourhoodSelectorTest(unittest.TestCase):
    def setUp(self):
        table = {'id': [1, 2, 3, 4, 5],
                 'name': ['Room with a View', 'Loft', 'Cheap', 'Cozy', 'Expensive'],
                 'neighbourhood_group': ['Manhattan', 'Manhattan', 'Brooklyn', 'Brooklyn', 'Queens'],
                 'neighbourhood': ['Upper East Side', 'East Village', 'Williamsburg', 'Williamsburg', 'Astoria'],
                 'room_type': ['Entire home/apt', 'Entire home/apt', 'Private room', 'Entire home/apt', 'Private room'],
                 'price': [100, 200, 50, 150, 500],
                 }
        df = pd.DataFrame(table)
        self.neighbourhood_selector = NeighbourhoodSelector(df=df)

    def test_set_selection_neighbourhood(self):
        """Test if neighbourhood selection works correctly"""
        df = self.neighbourhood_selector.set_selection(neighbourhood='Williamsburg')
        self.assertEqual(df['name'].to_list(), ['Cheap', 'Cozy'], msg="Neighbourhood selection failed")

    def test_set_selection_room_type(self):
        """Test if room type selection works correctly"""
        df = self.neighbourhood_selector.set_selection(neighbourhood=None, room_type='Private room')
        self.assertEqual(df['name'].to_list(), ['Cheap', 'Expensive'], msg="Room type selection failed")

    def test_set_selection_price(self):
        """Test if price selection works correctly"""
        df = self.neighbourhood_selector.set_selection(price=150)
        self.assertEqual(df['name'].to_list(), ['Room with a View', 'Cheap', 'Cozy'], msg="Price selection failed")

    def test_set_selection_combined(self):
        """Test if the selection in multiple categories at one works correctly"""
        df = self.neighbourhood_selector.set_selection(neighbourhood='Williamsburg', room_type='Private room',
                                                       price=100)
        self.assertEqual(df['name'].to_list(), ['Cheap'], msg="Neighbourhood and room type selection failed")

    def test_set_selection_impossible(self):
        """Test if the selection of an impossible combination works correctly"""
        df = self.neighbourhood_selector.set_selection(neighbourhood='Williamsburg', room_type='Private room', price=0)
        self.assertEqual(df, None, msg="Neighbourhood selection should be empty")

    def test_set_selection_nonexistent_neighbourhood(self):
        """Test if the selection of a non-existent neighbourhood is handled"""
        df = self.neighbourhood_selector.set_selection(neighbourhood='<Nonexistent>')
        self.assertEqual(df, None, msg="Neighbourhood selection should be empty")

    def test_get_neighbourhoods(self):
        self.assertEqual(self.neighbourhood_selector.get_neighbourhoods().tolist(),
                         ['Upper East Side', 'East Village', 'Williamsburg', 'Astoria'],
                         msg="Get unique neighbourhoods failed")
