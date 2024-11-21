import pandas as pd

caminho_do_arquivo = "vendas.csv"
caminho_do_arquivo_para_salvar = "vendas_novo.csv"

def start(caminho_do_arquivo: str, caminho_do_arquivo_para_salvar: str):
    df_dados_vendas = ler_csv(caminho_do_arquivo)
    df_dados_com_categoria = calcular_vendas_categoria(df_dados_vendas)
    salvando_em_csv(df_dados_com_categoria, caminho_do_arquivo_para_salvar)

def ler_csv(caminho_do_csv: str) -> pd.DataFrame:
    df_dados = pd.read_csv(caminho_do_csv)
    return df_dados

def salvando_em_csv(df_dados: pd.DataFrame, caminho_do_csv_save: str):
    print("o novo csv foi salvo")
    df_dados.to_csv(caminho_do_csv_save)

def calcular_vendas_categoria(df_dados: pd.DataFrame) -> pd.DataFrame:
    df_dados["total_de_vendas"] = df_dados["Quantidade"] * df_dados["Venda"] * 2
    return df_dados

if __name__ == "__main__":
    start(caminho_do_arquivo, caminho_do_arquivo_para_salvar)

