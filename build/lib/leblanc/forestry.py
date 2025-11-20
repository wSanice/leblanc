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

PRODUCTS_FORESTRY = {
    'Eucalyptus Grandis (Pulp)': {'species': 'Eucalyptus', 'target_age': 7, 'unit': 'm3/ha', 'price_per_unit': 80},
    'Pinus Elliotti (Sawwood)': {'species': 'Pinus', 'target_age': 18, 'unit': 'm3/ha', 'price_per_unit': 150},
    'Native Hardwood (Sust. Harvest)': {'species': 'Native', 'target_age': 30, 'unit': 'm3/ha', 'price_per_unit': 400},
    'Biomass/Energy Wood': {'species': 'Eucalyptus', 'target_age': 5, 'unit': 'tons', 'price_per_unit': 50},
}
MANAGEMENT_TYPES = ['Intensive', 'Sustainable', 'Reforestation']
REGIONS_FLORESTAL = ['Northern', 'Southern', 'Coastal']

def generate_forestry_records(num_records=350):
    set_seed()
    product_list = list(PRODUCTS_FORESTRY.keys())
    forestry_data = []
    start_date = datetime(2025, 1, 1)

    for i in range(num_records):
        product_name = random.choice(product_list)
        product_info = PRODUCTS_FORESTRY[product_name]
        record_date = start_date + timedelta(days=np.random.randint(1, 365))
        area_hectares = np.random.uniform(100, 5000)
        planting_age = np.random.randint(1, product_info['target_age'] * 2)
        management = random.choice(MANAGEMENT_TYPES)
        region = random.choice(REGIONS_FLORESTAL)
        age_factor = min(planting_age / product_info['target_age'], 1.5) if product_info['target_age'] > 0 else 1.0
        management_factor = {'Intensive': 1.1, 'Sustainable': 1.0, 'Reforestation': 0.9}[management]
        volume_per_unit = product_info['price_per_unit']
        total_volume = volume_per_unit * age_factor * management_factor * np.random.uniform(0.9, 1.1) * area_hectares
        total_revenue = total_volume * product_info['price_per_unit'] * np.random.uniform(0.9, 1.1)
        
        owner_info = get_fake_person_info()

        forestry_data.append({
            'inventory_id': 6000 + i,
            'record_date': record_date,
            'product_name': product_name,
            'species': product_info['species'],
            'region': region,
            'area_hectares': round(area_hectares, 2),
            'planting_age_years': planting_age,
            'management_type': management,
            'unit_of_measure': product_info['unit'],
            'total_volume': round(total_volume, 2),
            'estimated_unit_price': product_info['price_per_unit'],
            'total_estimated_revenue': round(total_revenue, 2),
            'owner_name': owner_info['customer_name']
        })
    return create_dataframe(forestry_data, "Forestry and Timber")