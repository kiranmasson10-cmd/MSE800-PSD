````markdown
# Student Login Project

A simple Python project demonstrating the use of decorators for logging and debugging student-related activities.

---

## Project Overview

This project simulates a small student management workflow where users can:

- Log in
- Submit assignments
- View grades

The project demonstrates how Python decorators can be used to:

- Monitor function execution
- Add reusable logging
- Improve debugging
- Keep business logic clean

---

## Project Structure

student_login_project_sample/

├── decorators.py  
├── users.py  
├── main.py  
└── README.md  

---

## How the Decorator Works

The project uses a custom decorator called `log_activity`.

The decorator automatically logs:

- Function name
- Execution time
- Activity status


## Program Flow

The `main.py` file controls the execution flow.

Execution order:

1. Student login
2. Assignment submission
3. Grade viewing

Each function call is automatically wrapped by the decorator.



## Debugging Process

### Step 1 — Analyze File Structure

The project was divided into separate modules:

| File          | Purpose               |
| ------------- | --------------------- |
| decorators.py | Logging functionality |
| users.py      | Student operations    |
| main.py       | Program controller    |

This modular structure improves readability and maintainability.

---

### Step 2 — Verify Decorator Execution

The decorator was tested to confirm:

* Wrapped functions execute correctly
* Arguments are passed properly
* Return values are preserved
* Logging appears in the correct order

Result:

✅ Decorator works correctly.

---

### Step 3 — Trace Function Calls

Program execution flow:

1. `main()` starts
2. `student_login()` executes
3. `submit_assignment()` executes
4. `view_grades()` executes

Each function call is intercepted by the decorator.

---

### Step 4 — Validate Logging Output

Verified logging features:

| Feature                     | Status |
| --------------------------- | ------ |
| Function name logging       | ✅      |
| Timestamp logging           | ✅      |
| Activity start message      | ✅      |
| Activity completion message | ✅      |

---

## Strengths of the Project

### Modular Design

The project separates logic into dedicated files.

### Reusable Decorator

The same decorator can be reused across multiple functions.

### Centralized Debugging

Logging logic is written once and reused everywhere.

### Flexible Function Handling

Using `*args` and `**kwargs` allows compatibility with different functions.

---


## Final Findings

The project successfully demonstrates Python decorators for centralized activity logging and debugging.

The decorator:

* Intercepts function calls
* Logs execution details
* Improves maintainability
* Reduces repeated code

The project also demonstrates:

* Modular programming
* Reusable utilities
* Execution tracing
* Beginner-friendly debugging techniques

