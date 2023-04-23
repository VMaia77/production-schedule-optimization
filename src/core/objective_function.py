import pyomo.environ as pyo


def objective_function(model):

    value = 0
    for d in model.Days:
        m1 = model.MachineType1Add1 + model.MachineType1Mult1 * model.P[('machine1', d)] ** 2
        m2 = model.MachineType2Add1 + model.MachineType2Mult1 * model.P[('machine2', d)]
        m3 = model.MachineType3Add1 + model.MachineType3Mult1 * model.P[('machine3', d)] + \
            model.MachineType3Mult2 * model.P[('machine3', d)] ** 2           
        m4 = model.MachineType3Add1 + model.MachineType3Mult1 * model.P[('machine4', d)] + \
            model.MachineType3Mult2 * model.P[('machine4', d)] ** 2
            
        value += m1
        value += m2
        value += m3
        value += m4
        
    return value


def define_objective_function(model):
    model.obj = pyo.Objective(rule = objective_function, sense=pyo.minimize)
    return model