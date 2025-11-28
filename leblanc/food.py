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

from .base import Leblanc
from datetime import datetime, timedelta
import numpy as np
import random

class Food(Leblanc):
    
    PRODUCTS_FOOD = {
        'Whole Milk 1L': {'category': 'Dairy', 'price': 5.50, 'perishable': True},
        'Roasted Coffee 500g': {'category': 'Grocery', 'price': 18.00, 'perishable': False},
        'Beef Tenderloin (kg)': {'category': 'Meat', 'price': 65.00, 'perishable': True},
        'Craft Beer 6-pack': {'category': 'Beverages', 'price': 55.00, 'perishable': False},
        'Parboiled Rice 5kg': {'category': 'Grocery', 'price': 22.00, 'perishable': False},
    }

    TRANSLATIONS = {
        'pt_BR': {
            'Dairy': 'Laticínios', 'Grocery': 'Mercearia', 'Meat': 'Açougue', 'Beverages': 'Bebidas',
            'Whole Milk 1L': 'Leite Integral 1L', 'Roasted Coffee 500g': 'Café Torrado 500g',
            'Beef Tenderloin (kg)': 'Filé Mignon (kg)', 'Craft Beer 6-pack': 'Cerveja Artesanal 6-pack',
            'Parboiled Rice 5kg': 'Arroz Parboilizado 5kg'
        }
    }

    def get_metadata(self):
        return {"description": "Food and Beverages retail sales", "products": list(self.PRODUCTS_FOOD.keys())}

    def build(self, missing_data_cols=None):
        sales_data = []
        product_list = list(self.PRODUCTS_FOOD.keys())
        start_date = datetime(2025, 10, 1)
        translator = self.TRANSLATIONS.get(self.locale, {})

        for i in range(self.num_records):
            raw_prod = random.choice(product_list)
            info = self.PRODUCTS_FOOD[raw_prod]
            order_date = start_date + timedelta(days=np.random.randint(1, 150), hours=np.random.randint(0, 23))
            base_price = info['price']
            if info['perishable'] and np.random.rand() < 0.15:
                unit_price = base_price * 0.80
            else:
                unit_price = base_price * np.random.uniform(0.95, 1.05)
            
            validity_days = np.random.randint(3, 30 if info['perishable'] else 365)
            expiration_date = order_date + timedelta(days=validity_days)
            product_name = translator.get(raw_prod, raw_prod)
            category = translator.get(info['category'], info['category'])

            sales_data.append({
                'transaction_id': 5000 + i,
                'order_date': order_date,
                'product': product_name,
                'category': category,
                'unit_price': round(unit_price, 2),
                'quantity': np.random.randint(1, 20),
                'total_sale': round(unit_price * np.random.randint(1, 20), 2),
                'expiration_date': expiration_date,
                'customer_name': self.fake.name(),
                'delivery_zipcode': self.fake.postcode()
            })

        df = self._create_dataframe(sales_data, "Food and Beverages")
        if missing_data_cols:
            df = self.inject_missing_values(df, missing_data_cols)
        return df