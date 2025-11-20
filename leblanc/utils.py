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

import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
from faker import Faker

random.seed(42)
np.random.seed(42)
fake = Faker('en_US') 

def set_seed(seed=42):
    random.seed(seed)
    np.random.seed(seed)
    
def get_fake_person_info():
    return {
        'customer_id': np.random.randint(100, 9999),
        'customer_name': fake.name(),
        'city': fake.city(),
        'state': fake.state_abbr()
    }

def create_dataframe(data_list, area_name):
    df = pd.DataFrame(data_list)
    print(f"Synthetic Data for {area_name} Generated Successfully. Total: {len(df)} records.")
    return df