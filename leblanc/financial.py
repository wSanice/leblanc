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

class Financial(Leblanc):
    
    PRODUCTS_FINANCIAL = {
        'Personal Loan': {'type': 'Loan', 'min_value': 5000, 'max_value': 50000, 'base_interest': 0.015},
        'Credit Card': {'type': 'Service', 'min_value': 1000, 'max_value': 20000, 'base_interest': 0.05},
        'Checking Account': {'type': 'Service', 'min_value': 0, 'max_value': 0, 'base_interest': 0.0},
        'Mortgage': {'type': 'Loan', 'min_value': 100000, 'max_value': 500000, 'base_interest': 0.007},
    }
    RISK_LEVELS = ['Low', 'Medium', 'High']

    TRANSLATIONS = {
        'pt_BR': {
            'Personal Loan': 'Empréstimo Pessoal', 'Credit Card': 'Cartão de Crédito',
            'Checking Account': 'Conta Corrente', 'Mortgage': 'Financiamento Imobiliário',
            'Loan': 'Empréstimo', 'Service': 'Serviço',
            'Low': 'Baixo', 'Medium': 'Médio', 'High': 'Alto'
        }
    }

    def get_metadata(self):
        return {"description": "Banking transactions and risk profiles"}

    def build(self, missing_data_cols=None):
        data = []
        prod_list = list(self.PRODUCTS_FINANCIAL.keys())
        start_date = datetime(2025, 7, 1)
        translator = self.TRANSLATIONS.get(self.locale, {})

        for i in range(self.num_records):
            raw_prod = random.choice(prod_list)
            info = self.PRODUCTS_FINANCIAL[raw_prod]
            raw_risk = random.choice(self.RISK_LEVELS)
            value_base = info['min_value'] + np.random.rand() * (info['max_value'] - info['min_value'])
            risk_factor = {'Low': 0.9, 'Medium': 1.0, 'High': 1.2}[raw_risk]
            final_interest = info['base_interest'] * risk_factor * np.random.uniform(0.95, 1.05)
            is_default = (raw_risk == 'High' and np.random.rand() < 0.2) or (raw_prod == 'Credit Card' and np.random.rand() < 0.1)

            product = translator.get(raw_prod, raw_prod)
            prod_type = translator.get(info['type'], info['type'])
            risk = translator.get(raw_risk, raw_risk)

            data.append({
                'client_id': 7000 + np.random.randint(1, 100),
                'transaction_date': start_date + timedelta(days=np.random.randint(1, 150)),
                'financial_product': product,
                'type': prod_type,
                'contracted_value': round(value_base, 2),
                'monthly_interest_rate': round(final_interest, 4),
                'client_risk_level': risk,
                'is_default': is_default
            })

        df = self._create_dataframe(data, "Financial Services")
        if missing_data_cols:
            df = self.inject_missing_values(df, missing_data_cols)
        return df