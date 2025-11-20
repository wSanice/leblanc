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

CROPS_INFO = {
    'Soybean': {'type': 'Grain', 'price_per_ton': 1800, 'yield_base': 3500},
    'Corn': {'type': 'Grain', 'price_per_ton': 900, 'yield_base': 6000},
    'Coffee': {'type': 'Permanent Crop', 'price_per_bag': 1200, 'yield_base': 30},
    'Beef Cattle': {'type': 'Livestock', 'price_per_arroba': 300, 'yield_base': 15},
    'Fertilizer NPK': {'type': 'Input', 'price_per_ton': 4500, 'yield_base': 0},
}
CLIMATE_CONDITIONS = ['Ideal', 'Normal', 'Drought', 'Excess Rain']
REGIONS = ['Midwest', 'South', 'Southeast', 'Northeast']

def generate_agribusiness_records(num_records=500):
    set_seed()
    crop_list = list(CROPS_INFO.keys())
    agri_data = []
    start_date = datetime(2025, 1, 1)

    for i in range(num_records):
        item_name = random.choice(crop_list)
        item_info = CROPS_INFO[item_name]
        record_date = start_date + timedelta(days=np.random.randint(1, 365))
        area_hectares = np.random.uniform(50, 2000)
        climate = random.choice(CLIMATE_CONDITIONS)
        region = random.choice(REGIONS)
        
        climate_factor = {'Ideal': 1.1, 'Normal': 1.0, 'Drought': 0.7, 'Excess Rain': 0.85}[climate]
        base_yield = item_info['yield_base']
        
        if item_info['type'] == 'Grain' or item_info['type'] == 'Permanent Crop':
            final_yield = base_yield * climate_factor * np.random.uniform(0.9, 1.1)
            total_production = final_yield * area_hectares
            unit = 'kg' if item_info['type'] == 'Grain' else 'bags'
            price_key = 'price_per_ton' if item_info['type'] == 'Grain' else 'price_per_bag'
            total_revenue = (total_production / 1000) * item_info.get('price_per_ton', 0) if item_info['type'] == 'Grain' else total_production * item_info.get('price_per_bag', 0)
        
        elif item_info['type'] == 'Livestock':
            num_animals = np.random.randint(50, 1000)
            avg_weight = np.random.uniform(400, 600)
            total_production = num_animals * avg_weight
            unit = 'kg'
            price_key = 'price_per_arroba'
            total_revenue = (total_production / 15) * item_info.get('price_per_arroba', 0)
            
        elif item_info['type'] == 'Input':
            total_production = np.random.uniform(10, 500)
            unit = 'tons'
            price_key = 'price_per_ton'
            total_revenue = 0

        farmer_info = get_fake_person_info()

        agri_data.append({
            'record_id': 9000 + i,
            'record_date': record_date,
            'item_name': item_name,
            'type': item_info['type'],
            'region': region,
            'area_hectares': round(area_hectares, 2),
            'climate_condition': climate,
            'production_unit': unit,
            'total_production_volume': round(total_production, 2),
            'market_price_unit': item_info.get(price_key, 0),
            'total_revenue': round(total_revenue, 2),
            'farm_owner': farmer_info['customer_name']
        })
    return create_dataframe(agri_data, "Agribusiness Production and Sales")