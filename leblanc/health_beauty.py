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

PRODUCTS_HEALTH_BEAUTY = {
    'Hydrating Facial Cream': {'type': 'Product', 'category': 'Skincare', 'price': 85.00, 'recurrence_days': 60},
    'Whey Protein Isolate 900g': {'type': 'Product', 'category': 'Supplements', 'price': 150.00, 'recurrence_days': 45},
    'Hair Shampoo (Anti-Frizz)': {'type': 'Product', 'category': 'Haircare', 'price': 35.00, 'recurrence_days': 30},
    'Lip Filler Session': {'type': 'Service', 'category': 'Aesthetics', 'price': 1200.00, 'recurrence_days': 180},
    'Deep Tissue Massage': {'type': 'Service', 'category': 'Wellness', 'price': 150.00, 'recurrence_days': 90},
    'Multivitamin Daily': {'type': 'Product', 'category': 'Supplements', 'price': 70.00, 'recurrence_days': 90},
}
DISCOUNT_CHANNELS = ['Online Store', 'Physical Store', 'Subscription']

def generate_health_beauty_sales(num_records=550):
    set_seed()
    product_list = list(PRODUCTS_HEALTH_BEAUTY.keys())
    sales_data = []
    start_date = datetime(2025, 11, 1)

    for i in range(num_records):
        product_name = random.choice(product_list)
        product_info = PRODUCTS_HEALTH_BEAUTY[product_name]

        transaction_date = start_date + timedelta(days=np.random.randint(1, 120), hours=np.random.randint(0, 23))
        quantity = np.random.randint(1, 4) if product_info['type'] == 'Product' else 1
        channel = random.choice(DISCOUNT_CHANNELS)
        unit_price = product_info['price']
        
        if channel == 'Subscription':
            unit_price = unit_price * 0.90
        else:
            unit_price = unit_price * np.random.uniform(0.95, 1.05)

        days_to_next_purchase = product_info['recurrence_days'] + np.random.randint(-15, 15)
        
        customer_info = get_fake_person_info()

        sales_data.append({
            'transaction_id': 8000 + i,
            'transaction_date': transaction_date,
            'item_name': product_name,
            'type': product_info['type'],
            'category': product_info['category'],
            'unit_price': round(unit_price, 2),
            'quantity': quantity,
            'total_sale': round(unit_price * quantity, 2),
            'customer_id': customer_info['customer_id'],
            'sales_channel': channel,
            'days_until_next_purchase_expected': days_to_next_purchase,
            'consultant_name': fake.name() if product_info['type'] == 'Service' else None
        })
    return create_dataframe(sales_data, "Health and Beauty")