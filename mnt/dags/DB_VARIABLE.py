DB_CONNECTION_INFO = {
    "host": "122.154.29.17",
    "port": "5433",
    "database": "ddpmdb",
    "password": "Bigdata@dm1n",
    "user": "bdadm"
}

DTYPE_DICT = {
    'LST_7Days_GISTDA': {
        'name': "LST_7Days_GISTDA",
        'dtype': {
            "lst_mean": "Float",
            "pv_idn": "Varchar(2)",
            "pv_th": "Varchar(250)",
            "pv_en": "Varchar(250)",
            "ap_idn": "Varchar(2)", 
            "ap_th": "Varchar(250)",
            "ap_en": "Varchar(250)",
            "tb_idn": "Varchar(2)",
            "tb_th": "Varchar(250)",
            "tb_en": "Varchar(250)",
            "lst_datetime": "TIMESTAMP",
            "write_datetime": "TIMESTAMP"
        }
    },
    'NDVI_7Days_GISTDA': {
        'name': "NDVI_7Days_GISTDA",
        'dtype': {
            "ndvi_mean": "Float",
            "pv_idn": "Varchar(2)",
            "pv_th": "Varchar(250)",
            "pv_en": "Varchar(250)",
            "ap_idn": "Varchar(2)", 
            "ap_th": "Varchar(250)",
            "ap_en": "Varchar(250)",
            "tb_idn": "Varchar(2)",
            "tb_th": "Varchar(250)",
            "tb_en": "Varchar(250)",
            "ndvi_datetime": "TIMESTAMP",
            "write_datetime": "TIMESTAMP"
        }
    },
    'Rainfall_3h_TMD': {
        'name': "Rainfall_3h_TMD",
        'dtype': {
            "station_id": "Varchar(4)",
            "rainfall_24h": "Float",
            "rainfall_3h": "Float",
            "rainfall_date_calc": "TIMESTAMP",
            "rainfall_datetime": "TIMESTAMP",
            "write_datetime": "TIMESTAMP"
        }
    },
    'Rainfall_Hourly_HII': {
        'name': "Rainfall_Hourly_HII",
        'dtype': {
            "station_id": "Varchar(6)",
            "rainfall_10m": "Float",
            "rainfall_1h": "Float",
            "rainfall_24h": "Float",
            "rainfall_today": "Float",
            "rainfall_date_calc": "TIMESTAMP",
            "rainfall_datetime": "TIMESTAMP",
            "write_datetime": "TIMESTAMP"
        }
    },
        'Rainfall_Hourly_DWR': {
        'name': "Rainfall_Hourly_DWR",
        'dtype': {
            "station_id": "Varchar(6)",
            "rainfall_15m": "Float",
            "rainfall_12h": "Float",
            "rainfall_24h": "Float",
            "rainfall_datetime": "TIMESTAMP",
            "write_datetime": "TIMESTAMP"
        }
    },
        'Rainfall_Hourly_DDS': {
        'name': "Rainfall_Hourly_DDS",
        'dtype': {
            "rainfall_5m": "Float",
            "rainfall_15m": "Float",
            "rainfall_30m": "Float",
            "rainfall_1h": "Float",
            "rainfall_3h": "Float",
            "rainfall_6h": "Float",
            "rainfall_12h": "Float",
            "rainfall_24h": "Float",
            "station_id": "Varchar(6)",
            "rainfall_datetime": "TIMESTAMP",
            "write_datetime": "TIMESTAMP"
        }
    },
        'Dam_Daily_EGAT': {
        'name': "Dam_Daily_EGAT",
        'dtype': {
            "dam_date": "TIMESTAMP",
            "dam_evap": "Float",
            "dam_id": "Varchar(2)",
            "dam_inflow": "Float",
            "dam_level": "Float",
            "dam_losses": "Float",
            "dam_released": "Float",
            "dam_spilled": "Float",
            "dam_storage": "Float",
            "write_datetime": "TIMESTAMP"
        }
    },
        'Dam_Hourly_EGAT': {
        'name': "Dam_Hourly_EGAT",
        'dtype': {
            "dam_datetime": "TIMESTAMP",
            "dam_id": "Varchar(2)",
            "dam_inflow": "Float",
            "dam_level": "Float",
            "dam_released": "Float",
            "dam_spilled": "Float",
            "dam_storage": "Float",
            "write_datetime": "TIMESTAMP"
        }
    },
        'WaterLevel_10m_HII': {
        'name': "WaterLevel_10m_HII",
        'dtype': {
            "station_id": "Varchar(10)",
            "waterlevel_datetime": "TIMESTAMP",
            "waterlevel_msl": "Float",
            "write_datetime": "TIMESTAMP"
        }
    },
        'Waterlevel_15m_DWR': {
        'name': "Waterlevel_15m_DWR",
        'dtype': {
            "station_id": "Varchar(10)",
            "waterlevel_datetime": "TIMESTAMP",
            "waterlevel_msl": "Float",
            "write_datetime": "TIMESTAMP"
        }
    },
        'Waterlevel_5m_DSS': {
        'name': "Waterlevel_5m_DSS",
        'dtype': {
            "station_id": "Varchar(3)",
            "canal_waterlevel_datetime": "TIMESTAMP",
            "canal_waterlevel_out": "Float",
            "canal_waterlevel_value": "Float",
            "write_datetime": "TIMESTAMP"
        }
    },
        'AQI_Daily_PCD': {
        'name': "AQI_Daily_PCD",
        'dtype': {
            "station_id": "Varchar(10)",
            "station_name_th": "Varchar(250)",
            "station_name_en": "Varchar(250)",
            "location_th": "Varchar(250)",
            "location_en": "Varchar(250)",
            "station_type": "Varchar(50)",
            "lat": "Float",
            "long": "Float",
            "pm25_value": "Float",
            "pm10_value": "Float",
            "o3_value": "Float",
            "co_value": "Float",
            "no2_value": "Float",
            "so2_value": "Float",
            "aqi": "Float",
            "aqi_datetime": "TIMESTAMP",
            "write_datetime": "TIMESTAMP"
        }
    },
        'Weather_7DaysForecast_TMD': {
        'name': "Weather_7DaysForecast_TMD",
        'dtype': {
            "province_name_th": "Varchar(100)",
            "province_name_en": "Varchar(100)",
            "forecast_date": "Date",
            "temp_max": "Float",
            "temp_min": "Float",
            "wind_direction": "Float",
            "wind_speed": "Float",
            "percent_rain_cover": "Float",
            "weather_desc_th": "Varchar(100)",
            "weather_desc_en": "Varchar(100)",
            "temp_desc_th": "Varchar(100)",
            "temp_desc_en": "Varchar(100)",
            "wave_height_th": "Varchar(100)",
            "wave_height_en": "Varchar(100)",
            "get_date": "Date",
            "write_datetime": "TIMESTAMP"
        }
    },
        'Weather_DailyForecast_TMD': {
        'name': "Weather_DailyForecast_TMD",
        'dtype': {
            "forecast_datetime": "Varchar(42601)",
            "forecast_desc_th": "Varchar(42601)",
            "forecast_desc_en": "Varchar(42601)",
            "region_name_th": "Varchar(42601)",
            "region_forecast_th": "Varchar(42601)",
            "region_name_en": "Varchar(42601)",
            "region_forecast_en": "Varchar(42601)",
            "write_datetime": "TIMESTAMP"
        }
    },
        'Weather_3h_TMD': {
        'name': "Weather_3h_TMD",
        'dtype': {
            "station_id": "Varchar(5)",
            "station_name_th": "Varchar(100)",
            "station_name_en": "Varchar(100)",
            "province_name_th": "Varchar(50)",
            "lat": "Float",
            "lng": "Float",
            "obs_datetime": "TIMESTAMP",
            "station_pressure": "Float",
            "mean_sealevel_pressure": "Float",
            "temp_max": "Float",
            "air_temp": "Float",
            "dew_point": "Float",
            "relative_humidity": "Float",
            "vapor_pressure": "Float",
            "land_visibility": "Float",
            "wind_direction": "Varchar(3)",
            "wind_speed": "Float",
            "rainfall_3h": "Float",
            "rainfall_24h": "Float",
            "write_datetime": "TIMESTAMP"
        }
    },
        'Rainfall_3h_TMD': {
        'name': "Rainfall_3h_TMD",
        'dtype': {
            "station_id": "Varchar(5)",
            "station_name_th": "Varchar(100)",
            "station_name_en": "Varchar(100)",
            "province_name_th": "Varchar(50)",
            "lat": "Float",
            "lng": "Float",
            "obs_datetime": "TIMESTAMP",
            "rainfall_3h": "Float",
            "rainfall_24h": "Float",
            "write_datetime": "TIMESTAMP"
        }
    },
        'Strom_6h_TMD': {
        'name': "Strom_6h_TMD",
        'dtype': {
            "strom_title": "Varchar(42601)",
            "strom_detail": "Varchar(42601)",
            "publish_datetime": "Varchar(50)",
            "write_datetime": "TIMESTAMP"
        }
    },
        'SoilMoisture_15m_DWR': {
        'name': "SoilMoisture_15m_DWR",
        'dtype': {
            "soil_datetime": "TIMESTAMP",
            "soil_value": "Float",
            "station_id": "Varchar(10)",
            "write_datetime": "TIMESTAMP"
        }
    },
    'NDWI_7Days_GISTDA': {
        'name': "NDWI_7Days_GISTDA",
        'dtype': {
            "ndwi_mean": "Float",
            "pv_idn": "Varchar(2)",
            "pv_th": "Varchar(250)",
            "pv_en": "Varchar(250)",
            "ap_idn": "Varchar(2)", 
            "ap_th": "Varchar(250)",
            "ap_en": "Varchar(250)",
            "tb_idn": "Varchar(2)",
            "tb_th": "Varchar(250)",
            "tb_en": "Varchar(250)",
            "ndwi_datetime": "TIMESTAMP",
            "write_datetime": "TIMESTAMP"
        }
    },
    'DRI_7Days_GISTDA': {
        'name': "DRI_7Days_GISTDA",
        'dtype': {
            "dri_mean": "Float",
            "pv_idn": "Varchar(2)",
            "pv_th": "Varchar(250)",
            "pv_en": "Varchar(250)",
            "ap_idn": "Varchar(2)", 
            "ap_th": "Varchar(250)",
            "ap_en": "Varchar(250)",
            "tb_idn": "Varchar(2)",
            "tb_th": "Varchar(250)",
            "tb_en": "Varchar(250)",
            "dri_datetime": "TIMESTAMP",
            "write_datetime": "TIMESTAMP"
        }
    },
    'SoilMoisture_7Days_GISTDA': {
        'name': "SoilMoisture_7Days_GISTDA",
        'dtype': {
            "smap_mean": "Float",
            "pv_idn": "Varchar(2)",
            "pv_th": "Varchar(250)",
            "pv_en": "Varchar(250)",
            "ap_idn": "Varchar(2)", 
            "ap_th": "Varchar(250)",
            "ap_en": "Varchar(250)",
            "tb_idn": "Varchar(2)",
            "tb_th": "Varchar(250)",
            "tb_en": "Varchar(250)",
            "smap_datetime": "TIMESTAMP",
            "write_datetime": "TIMESTAMP"
        }
    },
        'Earthquake_Global_USGS': {
        'name': "Earthquake_Global_USGS",
        'dtype': {
            "mag": "Float",
            "place": "Varchar(250)",
            "time": "Varchar(13)",
            "lon": "Float",
            "lat": "Float",
            "depth": "Float",
            "write_datetime": "TIMESTAMP"
        }
    },
        'Earthquake_Global_GEOFON': {
        'name': "Earthquake_Global_GEOFON",
        'dtype': {
            "title": "Varchar(250)",
            "description": "Varchar(250)",
            "write_datetime": "TIMESTAMP"
        }
    },
        'Earthquake_Global_IRIS': {
        'name': "Earthquake_Global_IRIS",
        'dtype': {
            "eq_datetime": "TIMESTAMP",
            "lat": "Float",
            "lon": "Float",
            "mag": "Float",
            "depth": "Float",
            "location": "Varchar(250)",
            "id": "Varchar(8)",
            "write_datetime": "TIMESTAMP"
        }
    },
        'Strom_Track_JMA': {
        'name': "Strom_Track_JMA",
        'dtype': {
            "international_id": "Varchar(4)",
            "strom_name": "Varchar(50)",
            "strom_datetime": "Varchar(8)",
            "grade": "Varchar(1)",
            "lat": "Float",
            "lon": "Float",
            "central_pressure": "Float",
            "max_sustained_wind_speed": "Float",
            "direction_longest_radius_50kt": "Varchar(1)",
            "longest_radius_50kt": "Float",
            "shortest_radius_50kt": "Float",
            "direction_longest_radius_30kt": "Varchar(1)",
            "longest_radius_30kt": "Float",
            "shortest_radius_30kt": "Float",
            "indicator_of_landfall_or_passage": "Varchar(1)",
            "write_datetime": "TIMESTAMP"
        }
    },
        'Soil_LandUse_LDD': {
        'name': "Soil_LandUse_LDD",
        'dtype': {
            "lu_id_l1": "Varchar(1)",
            "lu_id_l2": "Varchar(2)",
            "lu_id_l3": "Varchar(4)",
            "lu_code": "Varchar(4)",
            "lu_des_th": "Varchar(100)",
            "lu_des_en": "Varchar(100)",
            "lu_code_l1": "Varchar(1)",
            "lu_code_l2": "Varchar(2)",
            "area": "Float",
            "lu_detail": "Varchar(100)",
            "area_rai": "Float",
            "geometry": "GEOMETRY",
            "length": "Float",
            "write_datetime": "TIMESTAMP"
        }
    },
        'MainBasin_Area_ONWR': {
        'name': "MainBasin_Area_ONWR",
        'dtype': {
            "mb_code": "Varchar(5)",
            "mb_name_th": "Varchar(100)",
            "mb_name_en": "Varchar(100)",
            "area_sqkm": "Float",
            "geometry": "GEOMETRY",
            "write_datetime": "TIMESTAMP"
        }
    }
}
