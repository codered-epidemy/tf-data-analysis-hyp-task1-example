import pandas as pd
import numpy as np
from statsmodels.stats.proportion import proportions_ztest

chat_id = 191207196 

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
  
    alpha = 0.04
    
    count = np.array([x_success, y_success])
    nobs = np.array([x_cnt, y_cnt])
    
    stat, pval = proportions_ztest(count, nobs, alternative='larger')
    
    return pval < alpha
