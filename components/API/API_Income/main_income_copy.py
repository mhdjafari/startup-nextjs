import sys, os
script_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(script_dir)
utils_path = os.path.join(parent_dir, "API_Utils")
sys.path.insert(0, utils_path)
import cloudpickle
import logging
import json
import psycopg2
import time
import cachetools
from cachetools import cached
import warnings
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

warnings.filterwarnings("ignore")
# from authentication import *
# from utils import *
# ----------------------------------------------------------------------------------------------------------------------

# Configure logging
logging.basicConfig(
    level=logging.INFO,  # Set the log level to INFO or DEBUG
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='app.log',  # Specify the log file name
    filemode='w'  # 'w' for writing a new log file each time, 'a' for appending
)

# Create a logger instance for your application
logger = logging.getLogger(__name__)

def read_pickle(path):
    with open(path, 'rb') as file:
        serialized_object = file.read()
        deserialized_object = cloudpickle.loads(serialized_object)
    return deserialized_object

# parent_path = "/Users/mohamadjafari/PycharmProjects/Startup/FAST_REACT_APP/FASTAPI/API_Files/Disposable_Income_Module_API"
parent_path = "/Users/mohamadjafari/PycharmProjects/Startup/FAST_REACT_APP/REACT/LandingPage2/Disposable_Income_Module_API"

experience_weight_data_path = os.path.join(parent_path, "Data", "Experience_Weight_Data_09_12_2023.pkl")
income_data_path = os.path.join(parent_path, "Data", "Income_Data_09_12_2023.pkl")
income_weight_data_path = os.path.join(parent_path, "Data", "Income_Weight_Data_09_12_2023.pkl")
zip_code_data_path = os.path.join(parent_path, "Data", "Zip_Code_Data_09_12_2023.pkl")

cost_of_live_data_path = os.path.join(parent_path, "Data", "Cost_of_Living_Data_09_12_2023.pkl")
cost_of_living_fitline_data_path = os.path.join(parent_path, "Data", "Cost_of_Living_Fit_Line_Data_09_12_2023.pkl")
tax_data_path = os.path.join(parent_path, "Data", "Tax_Data_09_12_2023.pkl")

income_model_path = os.path.join(parent_path,"Model", "Income_Model_09_12_2023.pkl")
apply_experience_model_path = os.path.join(parent_path,"Model", "Apply_Experience_Model_09_12_2023.pkl")
cost_of_live_model_path = os.path.join(parent_path,"Model", "Cost_of_Live_Model_09_12_2023.pkl")
disposable_income_model_path = os.path.join(parent_path,"Model", "Disposable_Income_Model_09_12_2023.pkl")
tax_model_path = os.path.join(parent_path,"Model", "Tax_Model_09_12_2023.pkl")

df_zip_pkl = read_pickle(zip_code_data_path)
df_salary_pkl = read_pickle(income_data_path)
df_salary_weight_pkl = read_pickle(income_weight_data_path)
df_cost_of_live_fit_pkl = read_pickle(cost_of_living_fitline_data_path)
df_tax_pkl = read_pickle(tax_data_path)

income_model = read_pickle(income_model_path)
apply_experience_model = read_pickle(apply_experience_model_path)
cost_of_live_model = read_pickle(cost_of_live_model_path)
tax_model = read_pickle(tax_model_path)
disposable_income_model = read_pickle(disposable_income_model_path)

app = FastAPI()

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    # allow_origins=["*"],  # Set this to your frontend's domain during production
    allow_origins=["https://www.fintekera.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/calculator2")
async def calculator2(stated_gross_income: int, zip_code: str, job_title: str, monthly_debt: int or None=None,
                    requested_monthly_payment: int or None=None):

    variable_json = disposable_income_model(
        df_zip_pkl,
        df_salary_pkl,
        df_salary_weight_pkl,
        df_cost_of_live_fit_pkl,
        df_tax_pkl,
        income_model,
        apply_experience_model,
        tax_model,
        cost_of_live_model,
        zip_code,
        job_title,
        stated_gross_income,
        monthly_debt,
        requested_monthly_payment,
    )

    variable_json = json.loads(variable_json)

    return {"Results": variable_json}


