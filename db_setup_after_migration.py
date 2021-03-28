import numpy as np
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('sqlite:///application/simulator2.db', echo=False)

# Saudi Project

# hbu = pd.read_excel("HBU.xlsx")
# hbu.to_sql('hbu_saudi', con=engine, index=False, if_exists="replace")

# init_data = pd.read_excel("initial_data_saudi.xlsx")
# init_data.to_sql('init_data', con=engine, index=False, if_exists="replace")

# price_levels = pd.read_excel("Design Sheet V2.xlsx", sheet_name="Price Attribute Levels")
# price_levels = price_levels.drop([0])
# price_levels = price_levels.reset_index(drop=True)
# price_levels = price_levels[['SKU Name','Level 9']]
# price_levels.columns = ['sku_name','zero_percent']
# price_levels['project_id'] = 1
# price_levels.to_sql('zero_price_level', con=engine, index=False, if_exists="replace")


# Algeria Project

# hbu = pd.read_excel("algeria-hbu.xlsx")
# hbu.to_sql('hbu_algeria', con=engine, index=False, if_exists="replace")

init_data = pd.read_excel("algeria-design.xlsx", sheet_name='Product List')
init_data.to_sql('init_data', con=engine, index=False, if_exists="append")

# price_levels = pd.read_excel("algeria-design.xlsx", sheet_name="Price Attribute Levels")
# price_levels = price_levels.drop([0])
# price_levels = price_levels.reset_index(drop=True)
# price_levels = price_levels[['SKU Name','Level 11']]
# price_levels.columns = ['sku_name','zero_percent']
# price_levels['project_id'] = 3
# price_levels.to_sql('zero_price_level', con=engine, index=False, if_exists="append")
