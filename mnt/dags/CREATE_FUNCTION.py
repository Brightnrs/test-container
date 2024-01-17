# install and import library
import datetime as dt
import pandas as pd
import numpy as np
import requests
import json
import pytz
import lxml
import xml.etree.ElementTree as ET
import io
from bs4 import BeautifulSoup
import patoolib
import geopandas as gpd
from scipy.interpolate import griddata
import os
import re
import csv
import verticapy as vp
from verticapy.utilities import *
from DB_VARIABLE import DB_CONNECTION_INFO
import warnings
warnings.filterwarnings('ignore')

# create function for ingest all data sources
def connect_database():
    vp.new_connection(DB_CONNECTION_INFO, name='Vertica_New_Connection')


def add_timestamp(dataframe):
    # create timestamp of landing schema ingestion
    date = dt.datetime.now()
    target_timezone = pytz.timezone('Asia/Bangkok')
    date = date.replace(tzinfo=pytz.utc).astimezone(target_timezone)
    dataframe['write_datetime'] = date.strftime('%Y-%m-%d %H:%M:%S')
    return dataframe


def create_or_insert(dataframe, table_info, schema):
    # ingest data into landing schema with assign dtype for each column
    try:
        pandas_to_vertica(df=dataframe,
                          schema=schema,
                          **table_info
                          )
    except NameError:
        pandas_to_vertica(df=dataframe,
                          schema=schema,
                          insert=True,
                          **table_info
                          )
