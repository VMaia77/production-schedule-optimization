import pyomo.environ as pyo


def get_results(model, runtime):
        
    results = {}
    results['objective_value'] = pyo.value(model.obj)
    results['total_production'] =  sum([model.P[i].value for i in model.P])

    for machine in model.Machines:
        results[machine] = {}
        results[machine]['production'] = [int(model.P[(m, d)].value) for m, d in model.P if m == machine]
        results[machine]['working_hours'] = [int(model.WorkingHours[(m, d)].value) for m, d in model.WorkingHours if m == machine]

    results['runtime'] = runtime

    return results