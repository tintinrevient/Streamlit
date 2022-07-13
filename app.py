from os.path import abspath

import streamlit as st
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import plotly.express as px

# warehouse_location points to the default location for managed databases and tables
warehouse_location = abspath('spark-warehouse')

# 0. start Spark
spark = SparkSession.builder\
    .appName('demo')\
    .config('spark.sql.warehouse.dir', warehouse_location)\
    .enableHiveSupport().getOrCreate()

# 1. load Hive table
# df = spark.sql('SELECT * FROM global_temp.consistency_table')
df = spark.read.parquet(f'{warehouse_location}/consistency_table')
df = df.orderBy(col('datetime').asc())

# 2. show dataframe
st.write('Consistency DataFrame')
st.dataframe(df.toPandas())

# 3. show chart
st.write('Consistency Chart')

df_melted = df.toPandas().melt(id_vars=['feature'] + ['match_rate'])

fig = px.line(df_melted, x='value', y='match_rate', color='feature')

fig.update_xaxes(tickformat='%Y-%m-%d %H')
fig.update_layout(legend=dict(
    yanchor='bottom',
    y=0.99,
    xanchor='left',
    x=0.01
))

st.plotly_chart(fig, use_container_width=True)

