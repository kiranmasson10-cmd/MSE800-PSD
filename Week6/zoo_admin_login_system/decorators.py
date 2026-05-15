from datetime import datetime


# Decorator used for logging admin activities
# Adds execution tracking before and after function calls

def log_activity(func):

    def wrapper(*args, **kwargs):

        print("\n============================")
        print(f"Function: {func.__name__}")
        print(f"Time: {datetime.now()}")
        print("Activity started...")

        result = func(*args, **kwargs)

        print("Activity completed.")
        print("============================\n")

        return result

    return wrapper