# Copyright 2025 w.Sanice
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from .utils import np, pd, random, datetime, timedelta, set_seed, create_dataframe, get_fake_person_info, fake

PRODUCTS_APPAREL = {
    'Slim Fit Jeans': {'category': 'Bottom Wear', 'price': 180.00},
    'Basic Cotton T-Shirt': {'category': 'Top Wear', 'price': 60.00},
    'Casual Running Shoes': {'category': 'Footwear', 'price': 320.00},
    'Summer Midi Dress': {'category': 'Womenswear', 'price': 150.00},
    'Dress Socks (Pair)': {'category': 'Accessories', 'price': 15.00},
}
SIZES = ['XS', 'S', 'M', 'L', 'XL']
COLORS = ['Black', 'White', 'Navy Blue', 'Grey', 'Red']

def generate_apparel_sales(num_records=500):
    set_seed()
    product_list = list(PRODUCTS_APPAREL.keys())
    sales_data = []
    start_date = datetime(2025, 9, 1)

    for i in range(num_records):
        product_name = random.choice(product_list)
        
        order_date = start_date + timedelta(days=i * random.uniform(0.5, 1.5))
        if order_date.month in [10, 11, 12]:
             quantity = np.random.randint(1, 10)
        else:
             quantity = np.random.randint(1, 5)

        unit_price = PRODUCTS_APPAREL[product_name]['price'] * np.random.uniform(0.9, 1.1)
        
        customer_info = get_fake_person_info()

        sales_data.append({
            'transaction_id': 3000 + i,
            'transaction_date': order_date,
            'product': product_name,
            'category': PRODUCTS_APPAREL[product_name]['category'],
            'unit_price': round(unit_price, 2),
            'quantity': quantity,
            'total_sale': round(unit_price * quantity, 2),
            'size': random.choice(SIZES),
            'color': random.choice(COLORS),
            'customer_id': customer_info['customer_id'],
            'return_flag': np.random.choice([True, False], p=[0.15, 0.85])
        })
    return create_dataframe(sales_data, "Apparel and Fashion")