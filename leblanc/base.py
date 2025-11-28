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
# leblanc/agribusiness.py

import pandas as pd
import numpy as np
from faker import Faker
import random
from abc import ABC, abstractmethod

class Leblanc(ABC):
    def __init__(self, num_records, locale='en_US', seed=42):
        self.num_records = num_records
        self.locale = locale
        self.seed = seed
        self._setup_randomness(seed)
        self.fake = Faker(locale)

    def _setup_randomness(self, seed):
        random.seed(seed)
        np.random.seed(seed)
        Faker.seed(seed)

    def inject_missing_values(self, df, columns, missing_rate=0.05):
        df_copy = df.copy()
        for col in columns:
            if col in df_copy.columns:
                mask = np.random.choice([True, False], size=len(df), p=[missing_rate, 1-missing_rate])
                df_copy.loc[mask, col] = np.nan
        return df_copy

    @abstractmethod
    def get_metadata(self):
        pass

    @abstractmethod
    def build(self):
        pass

    def _create_dataframe(self, data, dataset_name):
        df = pd.DataFrame(data)
        print(f"[Leblanc] {dataset_name} ({self.locale}): {len(df)} lines generated.")
        return df