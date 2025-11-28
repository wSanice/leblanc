import sys
import pandas as pd

try:
    from leblanc import (
        Agribusiness, 
        Tech, 
        Food, 
        Apparel, 
        Financial, 
        HealthBeauty, 
        Forestry
    )
    print("[OK] Biblioteca 'leblanc' importada com sucesso!\n")
except ImportError as e:
    print(f"[ERRO] Erro Critico: Nao foi possivel importar 'leblanc'.")
    print(f"Detalhe: {e}")
    print("DICA: Voce rodou 'pip install -e .' no ambiente virtual?")
    sys.exit(1)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

def run_test_for_module(generator_class, name, target_col_for_nan):
    print(f"{'='*60}")
    print(f"[TESTE] TESTANDO MODULO: {name}")
    print(f"{'='*60}")

    try:
        print(f"-> Gerando registros em Portugues (pt_BR)...")
        generator = generator_class(num_records=10, locale='pt_BR')
        
        print(f"-> Testando .build() com injecao de falhas em '{target_col_for_nan}'...")
        df = generator.build(missing_data_cols=[target_col_for_nan])

        if df.empty:
            raise ValueError("O DataFrame retornado esta vazio!")
        
        null_count = df[target_col_for_nan].isnull().sum()
        
        print(f"[OK] Sucesso! {len(df)} linhas geradas.")
        print(f"[OK] Traducao OK (Verifique visualmente abaixo).")
        print(f"[OK] Missing Values: {null_count} encontrados na coluna alvo.")
        print("\n[DADOS] Amostra de Dados:")
        print(df.head(3))
        print("\n")
        
        return True

    except Exception as e:
        print(f"[FALHA] FALHA no modulo {name}.")
        print(f"Erro: {e}")
        return False
MODULES_TO_TEST = [
    (Agribusiness, "Agribusiness", "total_revenue"),
    (Tech,         "Tech Sales",   "total_sale"),
    (Food,         "Food & Bev",   "customer_name"),
    (Apparel,      "Apparel",      "return_flag"),
    (Financial,    "Financial",    "contracted_value"),
    (HealthBeauty, "Health/Beauty","sales_channel"),
    (Forestry,     "Forestry",     "estimated_revenue"),
]

if __name__ == "__main__":
    print(">>> Iniciando Suite de Testes para Contribuidores (v0.8.0)...\n")
    
    failures = []
    
    for cls, name, nan_col in MODULES_TO_TEST:
        success = run_test_for_module(cls, name, nan_col)
        if not success:
            failures.append(name)
    
    print(f"{'='*60}")
    if failures:
        print(f"[!] TESTES FALHARAM nos seguintes modulos: {failures}")
        sys.exit(1)
    else:
        print("[SUCESSO] TODOS OS MODULOS PASSARAM NOS TESTES!")
        sys.exit(0)