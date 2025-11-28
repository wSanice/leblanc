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

class Agribusiness(Leblanc): 
    CROPS_INFO = {
        'Soybean': {'type': 'Grain', 'price_per_ton': 1800, 'yield_base': 3500},
        'Corn': {'type': 'Grain', 'price_per_ton': 900, 'yield_base': 6000},
        'Coffee': {'type': 'Permanent Crop', 'price_per_bag': 1200, 'yield_base': 30},
        'Beef Cattle': {'type': 'Livestock', 'price_per_arroba': 300, 'yield_base': 15},
        'Fertilizer NPK': {'type': 'Input', 'price_per_ton': 4500, 'yield_base': 0},
    }
    CLIMATE_CONDITIONS = ['Ideal', 'Normal', 'Drought', 'Excess Rain']
    REGIONS = ['Midwest', 'South', 'Southeast', 'Northeast']

    TRANSLATIONS = {
        'pt_BR': {
            'Soybean': 'Soja', 'Corn': 'Milho', 'Coffee': 'Café', 'Beef Cattle': 'Gado de Corte',
            'Fertilizer NPK': 'Fertilizante NPK',
            'Grain': 'Grão', 'Permanent Crop': 'Cultura Perene', 'Livestock': 'Pecuária', 'Input': 'Insumo',
            'Ideal': 'Ideal', 'Normal': 'Normal', 'Drought': 'Seca', 'Excess Rain': 'Chuva Excessiva',
            'Midwest': 'Centro-Oeste', 'South': 'Sul', 'Southeast': 'Sudeste', 'Northeast': 'Nordeste'
        }
    }

    def get_metadata(self):
        return {
            "description": "Agricultural production data",
            "crops_available": list(self.CROPS_INFO.keys())
        }

    def build(self, missing_data_cols=None):
        start_date = datetime(2025, 1, 1)
        agri_data = []
        crop_list = list(self.CROPS_INFO.keys())
        translator = self.TRANSLATIONS.get(self.locale, {})

        for i in range(self.num_records):
            raw_item_name = random.choice(crop_list)
            item_info = self.CROPS_INFO[raw_item_name]            
            raw_climate = random.choice(self.CLIMATE_CONDITIONS)
            raw_region = random.choice(self.REGIONS)
            climate_factor = {'Ideal': 1.1, 'Normal': 1.0, 'Drought': 0.7, 'Excess Rain': 0.85}[raw_climate]
            base_yield = item_info['yield_base']
            area_hectares = np.random.uniform(50, 2000)            
            total_production = 0
            total_revenue = 0
            unit = ''
            price_unit = 0

            if item_info['type'] in ['Grain', 'Permanent Crop']:
                final_yield = base_yield * climate_factor * np.random.uniform(0.9, 1.1)
                total_production = final_yield * area_hectares
                unit = 'kg' if item_info['type'] == 'Grain' else 'bags'
                
                if item_info['type'] == 'Grain':
                    price_unit = item_info.get('price_per_ton', 0)
                    total_revenue = (total_production / 1000) * price_unit
                else:
                    price_unit = item_info.get('price_per_bag', 0)
                    total_revenue = total_production * price_unit
            
            elif item_info['type'] == 'Livestock':
                num_animals = np.random.randint(50, 1000)
                avg_weight = np.random.uniform(400, 600)
                total_production = num_animals * avg_weight
                unit = 'kg'
                price_unit = item_info.get('price_per_arroba', 0)
                total_revenue = (total_production / 15) * price_unit
                
            elif item_info['type'] == 'Input':
                total_production = np.random.uniform(10, 500)
                unit = 'tons'
                price_unit = item_info.get('price_per_ton', 0)
                total_revenue = 0

            item_name = translator.get(raw_item_name, raw_item_name)
            item_type = translator.get(item_info['type'], item_info['type'])
            climate = translator.get(raw_climate, raw_climate)
            region = translator.get(raw_region, raw_region)
            owner_name = self.fake.name()

            agri_data.append({
                'record_id': 9000 + i,
                'record_date': start_date + timedelta(days=np.random.randint(1, 365)),
                'item_name': item_name,
                'type': item_type,
                'region': region,
                'area_hectares': round(area_hectares, 2),
                'climate_condition': climate,
                'production_unit': unit,
                'total_production_volume': round(total_production, 2),
                'market_price_unit': price_unit,
                'total_revenue': round(total_revenue, 2),
                'farm_owner': owner_name
            })
        df = self._create_dataframe(agri_data, "Agribusiness")
        if missing_data_cols:
            df = self.inject_missing_values(df, missing_data_cols)
            
        return df