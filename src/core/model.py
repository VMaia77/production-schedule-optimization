
from typing import Dict
import pyomo.environ as pyo
from pyomo.opt import SolverFactory
from src.core.objective_function import define_objective_function
from src.core.constraints import define_constraints
from src.core.configs import MACHINES_NAMES


def define_model(demand: int,
                 n_days: int, 
                 machines_prod_per_hour: Dict[str, float],
                 surplus_tolerance: float,  
                 minimum_working_hours: Dict[str, int], 
                 maximum_working_hours: Dict[str, int], 
                 machine_type1_mult1: float, 
                 machine_type1_add1: float, 
                 machine_type2_mult1: float, 
                 machine_type2_add1: float,
                 machine_type3_mult1: float, 
                 machine_type3_mult2: float, 
                 machine_type3_add1: float):

    model = pyo.ConcreteModel()

    # parameters and sets
    model.Machines = pyo.Set(initialize=MACHINES_NAMES)
    model.Demand = demand
    model.Days = [i for i in range(n_days)]
    model.ProdPerHour = machines_prod_per_hour
    model.MinimumWorkingHours = minimum_working_hours
    model.MaximumWorkingHours = maximum_working_hours
    model.SurplusTolerance = 1 + surplus_tolerance
    
    day_duration = 24

    # variables
    model.P = pyo.Var(model.Machines, model.Days, within=pyo.Integers)
    model.WorkingHours = pyo.Var(model.Machines, model.Days, within=pyo.Integers, bounds=(0, day_duration))
    model.ActivateMachine = pyo.Var(model.Machines, model.Days, within=pyo.Binary)

    # objective parameters
    model.MachineType1Mult1 = machine_type1_mult1
    model.MachineType1Add1 = machine_type1_add1

    model.MachineType2Mult1 = machine_type2_mult1
    model.MachineType2Add1 = machine_type2_add1

    model.MachineType3Mult1 = machine_type3_mult1
    model.MachineType3Mult2 = machine_type3_mult2
    model.MachineType3Add1 = machine_type3_add1

    # big M
    model.M = 1e21

    define_objective_function(model)
    define_constraints(model)

    return model


def solve(model, time_limit=None):
    solver = SolverFactory('mindtpy')
    strategy = 'OA'
    mip_solver = 'glpk'
    nlp_solver = 'ipopt'
    if time_limit:
        solution = solver.solve(model, strategy = strategy, mip_solver = mip_solver, nlp_solver = nlp_solver, time_limit = time_limit)
    else:
        solution = solver.solve(model, strategy = strategy, mip_solver = mip_solver, nlp_solver = nlp_solver)
    return solution