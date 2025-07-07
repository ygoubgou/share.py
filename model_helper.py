from pathlib import Path
import pickle

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.neighbors import KNeighborsRegressor

rootPath = Path(__file__).parent

modelPaths = rootPath / "models"

"""def get_linear_model() -> LinearRegression:
    with open(modelPaths / 'LinearReg_Model.pkl', "rb") as f:
        model = pickle.load(f)
        return model"""

def get_boosting_model_av() -> GradientBoostingRegressor:
    with open(modelPaths / 'GradientB_Model_av.pkl', "rb") as f:
        model = pickle.load(f)
        return model
    
def get_knn_model_av() -> KNeighborsRegressor:
    with open(modelPaths / 'KNN_Model_av.pkl', "rb") as f:
        model = pickle.load(f)
        return model
    

def get_boosting_model_ap() -> GradientBoostingRegressor:
    with open(modelPaths / 'GradientB_Model_ap.pkl', "rb") as f:
        model = pickle.load(f)
        return model
    
def get_knn_model_ap() -> KNeighborsRegressor:
    with open(modelPaths / 'KNN_Model_ap.pkl', "rb") as f:
        model = pickle.load(f)
        return model
    