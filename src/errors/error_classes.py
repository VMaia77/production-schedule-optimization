


class BaseError:
    def to_dict(self, runtime=-1):
        return dict(message_code=self.message_code, message = self.message, runtime = runtime)


class RuntimeError(BaseError):
    def __init__(self):
        self.message_code = "RUNTIME_ERROR"
        self.message = "A runtime error occurred"


class InfeasibilityError(BaseError):
    def __init__(self):
        self.message_code = "INFEASIBLE_ERROR"
        self.message = "No feasible solutions were found."