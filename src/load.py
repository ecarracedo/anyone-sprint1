from typing import Dict
from pandas import DataFrame
from sqlalchemy.engine.base import Engine


def load(data_frames: Dict[str, DataFrame], database: Engine):
    """Load the dataframes into the sqlite database.

    Args:
        data_frames (Dict[str, DataFrame]): A dictionary with keys as the table names
        and values as the dataframes.
    """
    # TODO: Implement this function. For each dataframe in the dictionary, you must
    # use pandas.Dataframe.to_sql() to load the dataframe into the database as a
    # table.
    # For the table name use the `data_frames` dict keys.

    # Itera sobre el diccionario `data_frames`, donde:
    # - `table` es la clave (nombre de las tablas)
    # - `df` es el DataFrame asociado a esa clave
    for table, df in data_frames.items():
    
        # Abre una conexión a la base de datos utilizando el engine de SQLAlchemy
        with database.connect() as connection:
            
            # Escribe el DataFrame en la base de datos como una tabla.
            # - `name=table`: el nombre de la tabla será la clave del diccionario
            # - `con=connection`: se usa la conexión abierta
            # - `if_exists='replace'`: si la tabla ya existe, la reemplaza
            # - `index=False`: no incluye el índice del DataFrame como columna en la tabla
            df.to_sql(name=table, con=connection, if_exists='replace', index=False)

            # NOTA: para que me funcionara el codigo, tuve que 
            # actualizar la version de pandas a 2.2.2 y SqlAlchemy a 2.0.40
            # debido a que habia una incompatibilidad entre las versiones 1.5.2 de pandas
            # y 1.4.47 de SqlAlchemy, en la version de Python 3.12.7

    #raise NotImplementedError
