from collections import OrderedDict
import pymongo
import business_functions
import app_config as config

mongo_client = pymongo.MongoClient(config.MONGO_DB_CONNECTION_STRING)

db = mongo_client['excel_data']
collection_entries = db['entries']

def insert_after_check(data_list):
    invalid_data_list = []
    for i in range(len(data_list)):
        data_list[i]['Date'] = business_functions.get_current_date()
        engine_number = data_list[i]["Engine Number"]
        chassis_number = data_list[i]["Chassis Number"]
        query_check_engine_number = {"Engine Number":engine_number}
        query_check_chassis_number = {"Chassis Number":chassis_number}

        if collection_entries.find(query_check_engine_number,projection={'_id':False}).count()==0 and collection_entries.find(query_check_chassis_number,projection={'_id':False}).count()==0:
            collection_entries.insert_one(data_list[i])
        else:
            invalid_data = OrderedDict()
            invalid_data['Engine Number'] = engine_number
            invalid_data['Chassis Number'] = chassis_number
            invalid_data['Date'] = business_functions.get_current_date()
            invalid_data_list.append(invalid_data)

    return invalid_data_list
