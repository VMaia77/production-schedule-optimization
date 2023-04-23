from src.api.requests import post_request


def api_post_test():
    
    problem_data = {

        "demand": 100000,

        "n_days": 5,

        "machines_prod_per_hour": {
            "machine1": 800.5,
            "machine2": 400.6,
            "machine3": 300.7,
            "machine4": 300.7
        },

        # let demand_max = demand * surplus_tolerance, 
        # so the production will be > demand and < demand_max.
        # it must be >= 1
        "surplus_tolerance": 0.15, 

        "minimum_working_hours": {
            "machine1": 16,
            "machine2": 16,
            "machine3": 12,
            "machine4": 12
        },
        
        "maximum_working_hours": {
            "machine1": 24, 
            "machine2": 20, 
            "machine3": 20, 
            "machine4": 20
        },
        
        # these are the parameters cost to plug in the machine cost function
        "machine_type1_mult1": 0.001,
        "machine_type1_add1": 1000,
        "machine_type2_mult1": 0.03,
        "machine_type2_add1": 1700,
        "machine_type3_mult1": 0.002,
        "machine_type3_mult2": 0.001,
        "machine_type3_add1": 300,

        # time limit for the solver
        "time_limit": 7,

        "request_id": 173
    }

    response_json = post_request(problem_data)

    return response_json


if __name__ == "__main__":
    response_json = api_post_test()
    print(response_json)
