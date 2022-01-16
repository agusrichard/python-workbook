#!/usr/bin/env python

"""
    Author: Agus Richard Lubis
    Description:
        Given three inputs: Product data, stock data and location data
        These data need to be processed into the specified returns value.

        The programming language used is Python and there is some adjustment to the variable and function name
        to be more Pythonic.

        There is no built-in functions used. 
        All the imported objects are used for type hints and pretty print the result for easier read.

        Time complexity of process_data is O(n^2), given:
            - main for-loop =  O(a)
            - group_stock =  O(b)
            - locations_list_to_dict = O(c)
            - list comprehension for detail key = O(d)
        Looking at the code execution, big O can be simplified into:
            (O(a) + O(b) + O(c))(O(d))
        By Big-O's definition as all the inputs get larger and larger, the above expression can be simplified further into:
            O(n*n) = O(n^2)
        Note that inside the script execution section, there is a simple benchmarking using timeit module.
        Though the result will differ from machine to machine.

        Since get item in dictionary has average Big-O of O(1) which means constant.
        Accessing item in a dictionary is used many times inside this function.
"""

from numbers import Number
from typing import Dict, List

product_data = [
    {
        'product_id': 1000,
        'product_name': 'Product 1000'
    },
    {
        'product_id': 1001,
        'product_name': 'Product 1001'
    },
]

stock_data = [
    {
        'product_id': 1000,
        'location_id': 1,
        'stock': 21
    },
    {
        'product_id': 1000,
        'location_id': 2,
        'stock': 8
    },
    {
        'product_id': 1001,
        'location_id': 1,
        'stock': 4
    },
    {
        'product_id': 1001,
        'location_id': 2,
        'stock': 10
    }
]

location_data = [
    {
        'location_id': 1,
        'location_name': 'Location 1'
    },
    {
        'location_id': 2,
        'location_name': 'Location 2'
    }
]

def sum_list(lst: List[Number]) -> Number:
    """
        sum standard function from scratch
        
        Parameters:
            lst: List[Number] -> List of numbers to be reduced (through summation)
        Returns:
            Number: result of summation
    """
    temp = 0
    for i in lst:
        temp += i

    return temp

def locations_list_to_dict(locations: List) -> Dict:
    """
        Find location item using location_id in locations
        
        Parameters:
            location_id: int
            locations: List -> List of locations containing location_id and location_name
        Returns:
            Dict: location id, if not found empty dictionary will be given
    """
    result = {}

    for loc in locations:
        result[loc.get('location_id')] = loc

    return result



def group_stock(stocks: List) -> Dict:
    """
        Group stocks by product_id

        Parameters:
            stocks: List -> List of stocks
        Returns:
            Dict: Stocks group by product_id with key product_id
        Raises:
            ValueError: If there is a key not found, the data is assumed inconsistent
    """
    try:
        result = {}
        for stock in stocks:
            if stock.get('product_id') in result:
                result[stock.get('product_id')] = {
                    'data': result[stock.get('product_id')]['data'] + [stock],
                    'total': result[stock.get('product_id')]['total'] + stock['stock']
                }
            else:
                result[stock.get('product_id')] = {
                    'data': [stock],
                    'total': stock['stock']
                }

        return result
    except KeyError:
        raise ValueError('inconsistent data')


def process_data(products: List, stocks: List, locations: List) -> List:
    """
        Process products, stocks and locations into the expected output
        Each product item has product name and stocks.
        Stock item has total and detail (locations and stock)

        Parameters:
            products: List -> List of products
            stocks: List -> List of stocks
            locations: List -> List of locations
        Returns:
            List: Processed data of products with its detail
        Raises:
            ValueError: If there is a key not found, the data is assumed inconsistent
    """
    try:
        result = []

        grouped_stocks = group_stock(stocks)
        locations_dict = locations_list_to_dict(location_data)
        for product in products:
            result = result + [
                {
                    'product_name': product.get('product_name'),
                    'stock': {
                        'total': grouped_stocks[product.get('product_id')]['total'],
                        'detail': [
                            {
                                'stock': data.get('stock'),
                                'location_name': locations_dict[data.get('location_id')]['location_name']
                            }
                            for data in grouped_stocks[product.get('product_id')]['data']
                        ]
                    }
                }
            ]

        return result
    except KeyError:
        raise ValueError('inconsistent data')


        


if __name__ == '__main__':
    import json
    import timeit

    print('Execution time for 1000000 reps: ', timeit.timeit('process_data(product_data, stock_data, location_data)', globals=globals(), number=1000000))
    print('Result: ', json.dumps(process_data(product_data, stock_data, location_data), sort_keys=True, indent=4))
