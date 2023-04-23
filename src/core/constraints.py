import pyomo.environ as pyo


def constraint_rule0(model):
    return pyo.summation(model.P) >= model.Demand


def constraint_rule1(model):
    return pyo.summation(model.P) <= model.Demand * model.SurplusTolerance


def define_constraints(model):

    model.C0 = pyo.Constraint(rule = constraint_rule0)
    model.C1 = pyo.Constraint(rule = constraint_rule1)

    model.C2 = pyo.ConstraintList()
    model.C3 = pyo.ConstraintList()
    model.C4 = pyo.ConstraintList()
    model.C5 = pyo.ConstraintList()

    for m in model.Machines:
        for d in model.Days:
            model.C2.add(expr = model.P[(m, d)] == model.WorkingHours[(m, d)] * model.ProdPerHour[m])
            model.C3.add(expr = model.WorkingHours[(m, d)] >= model.MinimumWorkingHours[m] * model.ActivateMachine[(m, d)])
            model.C4.add(expr = model.WorkingHours[(m, d)] <= model.M * model.ActivateMachine[(m, d)])
            model.C5.add(expr = model.WorkingHours[(m, d)] <= model.MaximumWorkingHours[m])

    return model