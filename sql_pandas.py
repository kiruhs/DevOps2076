# from pandasql import sqldf
# import seaborn as sns
#
# penguins = sns.load_dataset('penguins')
# # print(penguins)
# print(sqldf('''SELECT species, island, sex
#                 FROM penguins
#                 WHERE sex="Female" and island="Torgersen"
#                 LIMIT 15'''
#                 ))
#
# from sqlalchemy import create_engine
# import pandas as pd
#
# username = 'root'
# password = 'root'
# host = 'localhost'
# port = '3306'
# database = 'qa2046'
# table_name = 'people'
#
# conn = create_engine(f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}")
#
# # the next row performs actual connection to the DB, the previous row just set the variable
# df = pd.read_sql(f"SELECT * FROM {table_name} where age > 40", conn)
#
# print(df.to_string())

with open('data.csv') as file:
    file.read()
    print()

file.read()