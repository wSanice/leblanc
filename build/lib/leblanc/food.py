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

PRODUCTS_FOOD = {
    'Whole Milk 1L': {'category': 'Dairy', 'price': 5.50, 'perishable': True},
    'Roasted Coffee 500g': {'category': 'Grocery', 'price': 18.00, 'perishable': False},
    'Beef Tenderloin (kg)': {'category': 'Meat', 'price': 65.00, 'perishable': True},
    'Craft Beer 6-pack': {'category': 'Beverages', 'price': 55.00, 'perishable': False},
    'Parboiled Rice 5kg': {'category': 'Grocery', 'price': 22.00, 'perishable': False},
}

def generate_food_sales(num_records=400):
    set_seed()
    product_list = list(PRODUCTS_FOOD.keys())
    sales_data = []
    start_date = datetime(2025, 10, 1)

    for i in range(num_records):
        product_name = random.choice(product_list)
        order_date = start_date + timedelta(days=np.random.randint(1, 150), hours=np.random.randint(0, 23))
        quantity = np.random.randint(1, 20)
        
        base_price = PRODUCTS_FOOD[product_name]['price']
        
        if PRODUCTS_FOOD[product_name]['perishable'] and np.random.rand() < 0.15:
            unit_price = base_price * 0.80
        else:
            unit_price = base_price * np.random.uniform(0.95, 1.05)
            
        is_perishable = PRODUCTS_FOOD[product_name]['perishable']
        validity_days = np.random.randint(3, 30 if is_perishable else 365)
        expiration_date = order_date + timedelta(days=validity_days)
        
        customer_info = get_fake_person_info()

        sales_data.append({
            'transaction_id': 5000 + i,
            'order_date': order_date,
            'product': product_name,
            'category': PRODUCTS_FOOD[product_name]['category'],
            'unit_price': round(unit_price, 2),
            'quantity': quantity,
            'total_sale': round(unit_price * quantity, 2),
            'expiration_date': expiration_date,
            'customer_name': customer_info['customer_name'],
            'delivery_zipcode': fake.postcode()
        })
    return create_dataframe(sales_data, "Food and Beverages")