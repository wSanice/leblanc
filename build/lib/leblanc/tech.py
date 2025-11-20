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

from .utils import np, pd, random, datetime, timedelta, set_seed, create_dataframe, get_fake_person_info

PRODUCTS_TECH = {
    'Gaming Laptop': {'category': 'Electronics', 'price': 7500.00},
    'Vertical Mouse': {'category': 'Accessories', 'price': 250.00},
    'Mechanical Keyboard': {'category': 'Accessories', 'price': 550.00},
    'Ultrawide Monitor': {'category': 'Electronics', 'price': 2800.00},
    'Gaming Chair': {'category': 'Furniture', 'price': 1200.00},
    'Headset 7.1': {'category': 'Accessories', 'price': 800.00},
    'Video Card': {'category': 'Hardware', 'price': 4500.00},
    'SSD 1TB': {'category': 'Hardware', 'price': 600.00}
}

def generate_tech_sales(num_records=600):
    set_seed()
    product_list = list(PRODUCTS_TECH.keys())
    sales_data = []
    start_date = datetime(2026, 1, 1)

    for i in range(num_records):
        product_name = random.choice(product_list)
        quantity = np.random.randint(1, 8)
        order_date = start_date + timedelta(days=int(i / 5) * random.randint(1, 3), hours=random.randint(0, 23))

        if product_name in ['Vertical Mouse', 'Mechanical Keyboard']:
            unit_price = PRODUCTS_TECH[product_name]['price'] * np.random.uniform(0.9, 1.0)
        else:
            unit_price = PRODUCTS_TECH[product_name]['price']
            
        customer_info = get_fake_person_info()

        sales_data.append({
            'order_id': 1000 + i,
            'order_date': order_date,
            'product_name': product_name,
            'category': PRODUCTS_TECH[product_name]['category'],
            'unit_price': round(unit_price, 2),
            'quantity': quantity,
            'total_sale': round(unit_price * quantity, 2),
            'customer_id': customer_info['customer_id'],
            'city': customer_info['city'],
            'state': customer_info['state']
        })
    return create_dataframe(sales_data, "Technology Sales")