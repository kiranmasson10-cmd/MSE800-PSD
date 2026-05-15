# Zoo Admin Login System

A simple Python project that demonstrates an admin login system for a zoo using decorators for activity logging.

---

## Project Structure

```text
zoo_admin_login_system/
│
├── decorators.py
├── admin.py
├── main.py
└── README.md

Features
Admin login authentication
View zoo animal records
Add new animals
Activity logging using decorators
Decorator Implementation

The project uses a custom decorator called log_activity.

The decorator automatically logs:

Function name
Execution time
Activity status

Example:

@log_activity
def admin_login(username, password):

The decorator wraps the function and prints logging information before and after execution.

How to Run
Open terminal
Navigate to project folder
Run:
python main.py