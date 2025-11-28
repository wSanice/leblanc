<p align="center">
  <img src="https://raw.githubusercontent.com/wSanice/leblanc/refs/heads/main/assets/leblanc.png" alt="Leblanc Banner" width="100%"/>
</p>

# leblanc: Sectorial Synthetic Data Generator

## I. Overview

**leblanc** is a modular Python library designed for Data Scientists to rapidly generate large-scale synthetic datasets across various business sectors. Built on top of **Pandas**, **NumPy**, and **Faker**, it creates realistic, structured DataFrames suitable for training, testing, and Exploratory Data Analysis (EDA).

**New in v0.6.3:**
* **Object-Oriented Design:** Use Classes for better control.
* **Internationalization (i18n):** Native support for Brazilian Portuguese (`pt_BR`).
* **Data Cleaning Practice:** Native support for injecting missing values (`NaN`).

### Supported Sectors (Classes)

| Class | Data Generated | Key Domain Variables |
| :--- | :--- | :--- |
| `Tech` | Tech Sales | Unit Price, Quantity, Category |
| `Food` | Food & Beverages Sales | Expiration Date, Perishability |
| `Apparel` | Apparel & Fashion Sales | Size, Color, Return Flag |
| `Financial` | Financial Transactions | Interest Rate, Client Risk Level, Default Flag |
| `HealthBeauty` | Health & Beauty Sales/Services | Recurrence Days, Sales Channel |
| `Agribusiness` | Agribusiness Records | Climate Condition, Area (Ha), Production Yield |
| `Forestry` | Forestry Inventory/Harvest | Planting Age, Management Type, Total Volume ($m^3$) |

---

## II. Installation

leblanc is available on PyPI. Use `pip` to install the latest stable version:

```bash
pip install leblanc
```
## III. Usage Example
### 1. Basic Usage (English - Default)
The library now uses classes with a standard `.build()` method.

```python
import pandas as pd
from leblanc import Tech, Agribusiness

# 1. Generate Technology Sales Data
# Uses seed=42 by default for reproducibility
df_tech = Tech(num_records=1000).build()

print("--- Technology Data Sample ---")
print(df_tech.head())

# 2. Generate Agribusiness Records
df_agro = Agribusiness(num_records=500).build()

```
### 2. Brazilian Portuguese Support (pt_BR) 🇧🇷

You can generate data localized for Brazil (translated products, categories, and regions) by passing the `locale` parameter.

```python
from leblanc import Food

# Generates data with 'Leite', 'Café', 'Açougue', etc.
df_food_br = Food(num_records=100, locale='pt_BR').build()

print(df_food_br.head())
```

### 3. Data Cleaning Practice (Injecting Nulls) 

Perfect for teaching or testing how models handle missing data. You can inject `NaN` values into specific columns.
```python
from leblanc import Financial

# Simulates a dirty dataset where 'contracted_value' has missing data
df_fin = Financial(num_records=1000).build(missing_data_cols=['contracted_value'])

print(f"Missing values generated: {df_fin['contracted_value'].isnull().sum()}")
```

## IV. License

This project is licensed under the Apache License, Version 2.0. See the [LICENSE](https://www.apache.org/licenses/LICENSE-2.0)  for details.

<br><br><br><br>

# 🇧🇷 leblanc: Gerador Setorial de Dados Sintéticos

## I. Visão Geral

**leblanc** é uma biblioteca Python modular projetada para a geração rápida de conjuntos de dados sintéticos de grande escala. É construída utilizando **Pandas**, **NumPy** e **Faker** para criar DataFrames estruturados e realistas, adequados para treinamento em Data Science, testes e análise exploratória de dados (EDA).


**Novidades na v0.6.3:**

**Design Orientado a Objetos:** Uso de Classes para maior controle.

**Internacionalização (i18n):** Suporte nativo para Português do Brasil (`pt_BR`).

**Prática de Limpeza de Dados:** Suporte nativo para injeção de valores nulos (`NaN`).

### Setores Suportados (Classes)

| Classe | Dados Gerados | Variáveis-Chave do Domínio |
| :--- | :--- | :--- |
| `Tech` | Vendas de Tecnologia | Preço Unitário, Quantidade, Categoria |
| `Food` | Vendas de Alimentos e Bebidas | Data de Validade, Perecibilidade |
| `Apparel` | Vendas de Vestuário e Moda | Tamanho, Cor, Flag de Devolução |
| `Financial` | Transações Financeiras | Taxa de Juros, Nível de Risco do Cliente, Flag de Inadimplência |
| `HealthBeauty` | Vendas/Serviços de Saúde e Beleza | Dias de Recorrência, Canal de Vendas |
| `Agribusiness` | Registros de Agronegócios | Condição Climática, Área (Ha), Produtividade |
| `Forestry` | Inventário/Colheita Florestal | Idade do Plantio, Tipo de Manejo, Volume Total (m³) |

## II. Instalação

leblanc está disponível no PyPI. Use o `pip` para instalar a versão estável mais recente:

```bash
pip install leblanc
```

## III. Exemplos de Uso
### 1. Uso Básico (Padrão)

A biblioteca agora utiliza classes com um método padronizado `.build()`.

```python
import pandas as pd
from leblanc import Tech, Agribusiness

# 1. Gera Dados de Vendas de Tecnologia
# Usa seed=42 por padrão para reprodutibilidade
df_tech = Tech(num_records=1000).build()

print("--- Amostra de Dados de Tecnologia ---")
print(df_tech.head())
```
### 2. Suporte a Português (pt_BR) 🇧🇷

Você pode gerar dados localizados para o Brasil (produtos, categorias e regiões traduzidas) passando o parâmetro `locale`.

```python
from leblanc import Food

# Gera dados com 'Leite', 'Café', 'Açougue', etc.
df_food_br = Food(num_records=100, locale='pt_BR').build()

print(df_food_br.head())
```
### 3. Prática de Limpeza de Dados (Injeção de Nulos)
Perfeito para estudo de como modelos lidam com dados faltantes. 
Você pode injetar valores `NaN` em colunas específicas.
```python
from leblanc import Financial

# Simula um dataset "sujo" onde 'contracted_value' possui dados faltantes
df_fin = Financial(num_records=1000).build(missing_data_cols=['contracted_value'])

print(f"Valores nulos gerados: {df_fin['contracted_value'].isnull().sum()}")
```


## IV. Licença

Este projeto está licenciado sob a Apache License, Version 2.0. Consulte a [LICENSE](https://www.apache.org/licenses/LICENSE-2.0)
 para obter detalhes.