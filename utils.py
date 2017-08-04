import pandas as pd
import yaml
import numpy as np


#### Double Moving Average
def dema(series, halflife=30, min_periods=10):
    
    ma = series.ewm(halflife=halflife, min_periods=min_periods).mean()
    
    dema = 2*ma - ma.ewm(halflife=halflife).mean()
    
    return dema

#### Triple Moving Average
def tema(series, halflife=30):
    
    ma = series.ewm(halflife=halflife).mean()
    
    dma = ma.ewm(halflife=halflife).mean()
    
    tma = 3*ma - 3*dma + dma.ewm(halflife=halflife).mean()
    
    return tma

def calcula_medias_dema(df, halflifes=(7,30,90)):
    """
    Calcula as médias usando dema.
    df: dic of pd.dataframes
    halflifes: tuple of ints
    return: dict of pd.dataframe
    """
    df_dema = {}
    for halflife in halflifes:
        df_dema[halflife] = {}
        for key, value in df.items():
            df_dema[halflife][key] = value.apply(dema, args=(halflife,))
            
    return df_dema

def check_substitute(x, mini, maxi, rang):
    
    norm = (x - mini) / (maxi + abs(mini)) * rang[1]
    
    if norm > 100:
        return 100
    elif norm < 0:
        return 0
    else:
        return norm

def normaliza(df, rang=(0,100)):
    """
    Normaliza os dataframes de acordo com o rang
    df: dic of pd.dataframes
    range: tuple of ints
    return: dict of pd.dataframe
    """
    fidelidade_dic_dema_norm  = {}
    for hl, dfs in df.items():
        fidelidade_dic_dema_norm[hl]  = {}
        for key, value in dfs.items():
            maxi = max(1.005, min(np.nanmax(value.values), 1.005))
            mini = min(-0.05, max(np.nanmin(value.values), -0.05))

            fidelidade_dic_dema_norm[hl][key] = value.applymap(lambda x: check_substitute(x, mini, maxi, rang))

    return fidelidade_dic_dema_norm

def substitui_sigla_loop(sigla, relacoes):

    sub = relacoes[relacoes['sinonimo'] == sigla]['sigla_atualizada']
    if len(sub) > 0:
        return str(list(sub)[0])
    else:
        return sigla

def substitui_sigla(dataframe=None, partido_column=None):
    """
    Substitui a sigla antiga do partido por uma sigla nova.

    Esse método acessa a tabela desenv.sigla_partido_atualizadas

    :param dataframe: pd.DataFrame que tem uma coluna de partido
    :param partido_column: str Coluna do partido
    :return: dataframe: pd.DataFrame atualizado
    """

    if (dataframe is None) or (partido_column is None):
        raise ValueError ('Preencha todos os parametros')


    conn = connect_sqlalchemy()

    relacoes = pd.read_sql_query('SELECT * FROM desenv.sigla_partido_atulizada', conn)


    dataframe['{}'.format(partido_column + 'Atualizado')] = \
        dataframe[partido_column].apply(substitui_sigla_loop, args=(relacoes,))

    return dataframe

def connect_sqlalchemy():
    with open('/home/Admin/cts/congresso/server_config.yaml', 'r') as f:
        server = yaml.load(f)

    host = server['host']
    database = server['database']
    user = server['user']
    password = server['password']

    from sqlalchemy import create_engine
    url = 'postgresql://{}:{}@{}/{}'
    url = url.format(user, password, host, database)
    return create_engine(url)