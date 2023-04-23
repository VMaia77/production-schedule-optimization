import os
from typing import Dict
import time
from datetime import datetime
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
import src.environment
from src.logging.logger import create_logger
from src.core.model import define_model, solve
from src.core.utils import get_results
from src.errors.error_classes import RuntimeError, InfeasibilityError


logger = create_logger()

app = FastAPI()

start_time = datetime.now()

logger.info(f'API is ON: {start_time}', exc_info=True)


class Problem(BaseModel):
    demand: int
    n_days: int
    machines_prod_per_hour: Dict[str, float]
    surplus_tolerance: float
    minimum_working_hours: Dict[str, int]
    maximum_working_hours:  Dict[str, int]
    machine_type1_mult1: float
    machine_type1_add1: float
    machine_type2_mult1: float
    machine_type2_add1: float
    machine_type3_mult1: float
    machine_type3_mult2: float
    machine_type3_add1: float
    time_limit: int = None
    request_id: int = 0


@app.get("/status")
async def get_api_status():
    uptime = (datetime.now() - start_time).total_seconds()
    return {
        "status": "OK",
        "uptime_seconds": uptime,
        "start_time": start_time,
        "current_time": datetime.now()
    }


@app.post("/solve")
async def solve_problem(problem: Problem):
    logger.info(f'REQUEST_ID: {problem.request_id}')  
    logger.info('INPUT: ')  
    logger.info(problem.dict())

    t0 = time.time()   

    try:
        model = define_model(demand=problem.demand,
                             n_days=problem.n_days, 
                             machines_prod_per_hour=problem.machines_prod_per_hour,
                             surplus_tolerance=problem.surplus_tolerance, 
                             minimum_working_hours=problem.minimum_working_hours, 
                             maximum_working_hours=problem.maximum_working_hours, 
                             machine_type1_mult1=problem.machine_type1_mult1, 
                             machine_type1_add1=problem.machine_type1_add1, 
                             machine_type2_mult1=problem.machine_type2_mult1, 
                             machine_type2_add1=problem.machine_type2_add1,
                             machine_type3_mult1=problem.machine_type3_mult1, 
                             machine_type3_mult2=problem.machine_type3_mult2, 
                             machine_type3_add1=problem.machine_type3_add1)

        solution = solve(model, time_limit = problem.time_limit)

        if solution.solver.termination_condition == 'infeasible':
            runtime = time.time() - t0
            logger.error('INFEASIBLE_ERROR: ')
            infeasible_error = InfeasibilityError().to_dict(runtime)   
            logger.error(infeasible_error , exc_info=True)
            return infeasible_error
        else:
            runtime = time.time() - t0        
            output = get_results(model, runtime)
            logger.info('OUTPUT: ')  
            logger.info( output, exc_info=True)
            
    except Exception as e:
        runtime = time.time() - t0
        logger.error('RUNTIME_ERROR')
        logger.error(e, exc_info=True)   
        error = RuntimeError().to_dict(runtime)
        logger.info(error)         
        return error
    
    return output
    
if __name__ == "__main__":
    uvicorn.run("main:app", port=int(os.getenv("PORT")), reload=True)