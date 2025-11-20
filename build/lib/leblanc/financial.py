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

PRODUCTS_FINANCIAL = {
    'Personal Loan': {'type': 'Loan', 'min_value': 5000, 'max_value': 50000, 'base_interest': 0.015},
    'Credit Card': {'type': 'Service', 'min_value': 1000, 'max_value': 20000, 'base_interest': 0.05},
    'Checking Account': {'type': 'Service', 'min_value': 0, 'max_value': 0, 'base_interest': 0.0},
    'Mortgage': {'type': 'Loan', 'min_value': 100000, 'max_value': 500000, 'base_interest': 0.007},
}
RISK_LEVELS = ['Low', 'Medium', 'High']

def generate_financial_transactions(num_records=300):
    set_seed()
    product_list = list(PRODUCTS_FINANCIAL.keys())
    transaction_data = []
    start_date = datetime(2025, 7, 1)

    for i in range(num_records):
        product = random.choice(product_list)
        value_base = PRODUCTS_FINANCIAL[product]['min_value'] + np.random.rand() * (PRODUCTS_FINANCIAL[product]['max_value'] - PRODUCTS_FINANCIAL[product]['min_value'])
        
        risk = random.choice(RISK_LEVELS)
        risk_factor = {'Low': 0.9, 'Medium': 1.0, 'High': 1.2}[risk]
        
        final_interest = PRODUCTS_FINANCIAL[product]['base_interest'] * risk_factor * np.random.uniform(0.95, 1.05)
        
        is_default = (risk == 'High' and np.random.rand() < 0.2) or \
                       (product == 'Credit Card' and np.random.rand() < 0.1)
        
        transaction_data.append({
            'client_id': 7000 + np.random.randint(1, 100),
            'transaction_date': start_date + timedelta(days=np.random.randint(1, 150)),
            'financial_product': product,
            'type': PRODUCTS_FINANCIAL[product]['type'],
            'contracted_value': round(value_base, 2),
            'monthly_interest_rate': round(final_interest, 4),
            'client_risk_level': risk,
            'is_default': is_default
        })
    return create_dataframe(transaction_data, "Financial Services")