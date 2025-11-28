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

class Forestry(Leblanc):
    
    PRODUCTS_FORESTRY = {
        'Eucalyptus Grandis': {'species': 'Eucalyptus', 'target_age': 7, 'unit': 'm3/ha', 'price': 80},
        'Pinus Elliotti': {'species': 'Pinus', 'target_age': 18, 'unit': 'm3/ha', 'price': 150},
        'Native Hardwood': {'species': 'Native', 'target_age': 30, 'unit': 'm3/ha', 'price': 400},
        'Biomass Wood': {'species': 'Eucalyptus', 'target_age': 5, 'unit': 'tons', 'price': 50},
    }
    MANAGEMENT = ['Intensive', 'Sustainable', 'Reforestation']
    REGIONS = ['Northern', 'Southern', 'Coastal']

    TRANSLATIONS = {
        'pt_BR': {
            'Eucalyptus': 'Eucalipto', 'Native': 'Nativa',
            'Intensive': 'Intensivo', 'Sustainable': 'Sustentável', 'Reforestation': 'Reflorestamento',
            'Northern': 'Norte', 'Southern': 'Sul', 'Coastal': 'Litoral',
            'Eucalyptus Grandis': 'Eucalipto Grandis (Celulose)', 'Pinus Elliotti': 'Pinus (Serraria)',
            'Native Hardwood': 'Madeira de Lei (Manejo)', 'Biomass Wood': 'Madeira para Biomassa'
        }
    }

    def get_metadata(self):
        return {"description": "Forestry inventory and harvest data"}

    def build(self, missing_data_cols=None):
        data = []
        prod_list = list(self.PRODUCTS_FORESTRY.keys())
        start_date = datetime(2025, 1, 1)
        translator = self.TRANSLATIONS.get(self.locale, {})

        for i in range(self.num_records):
            raw_prod = random.choice(prod_list)
            info = self.PRODUCTS_FORESTRY[raw_prod]
            raw_mgmt = random.choice(self.MANAGEMENT)
            raw_reg = random.choice(self.REGIONS)
            area = np.random.uniform(100, 5000)
            age = np.random.randint(1, info['target_age'] * 2)
            age_factor = min(age / info['target_age'], 1.5)
            mgmt_factor = {'Intensive': 1.1, 'Sustainable': 1.0, 'Reforestation': 0.9}[raw_mgmt]
            total_vol = info['price'] * age_factor * mgmt_factor * area * np.random.uniform(0.9, 1.1)
            revenue = total_vol * info['price']
            prod = translator.get(raw_prod, raw_prod)
            spec = translator.get(info['species'], info['species'])
            mgmt = translator.get(raw_mgmt, raw_mgmt)
            reg = translator.get(raw_reg, raw_reg)
            data.append({
                'inventory_id': 6000 + i,
                'record_date': start_date + timedelta(days=np.random.randint(1, 365)),
                'product_name': prod,
                'species': spec,
                'region': reg,
                'area_hectares': round(area, 2),
                'planting_age_years': age,
                'management_type': mgmt,
                'total_estimated_volume': round(total_vol, 2),
                'estimated_revenue': round(revenue, 2),
                'owner_name': self.fake.name()
            })

        df = self._create_dataframe(data, "Forestry & Timber")
        if missing_data_cols:
            df = self.inject_missing_values(df, missing_data_cols)
        return df