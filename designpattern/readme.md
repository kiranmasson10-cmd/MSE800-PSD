
# Aquarium Management System

## Overview
This project is an Aquarium Management System developed using Python.

The system allows users to:
- Add fish to the aquarium
- Manage fish inventory
- Display the number of fish available

The aquarium is based in Auckland, New Zealand.

---

## Fish Categories
The system supports:
- Goldfish
- Shark
- Angelfish
- Tuna
- Salmon

---

## Design Patterns Used

### 1. Factory Design Pattern
The Factory Pattern is used to create fish objects dynamically without directly creating objects in the client code.

Example:
- Goldfish
- Shark
- Tuna

The `FishFactory` class handles object creation.

---

### 2. Singleton Design Pattern
The Singleton Pattern ensures that only one aquarium inventory exists throughout the application.

The `Aquarium` class stores and manages all fish records.

---

## Project Structure

```text
designpattern/
│
├── main.py
├── fish.py
├── factory.py
├── aquarium.py
├── README.md
````

---

## Technologies Used

* Python 3
* Object-Oriented Programming
* Abstract Classes
* Factory Pattern
* Singleton Pattern

---

## How to Run the Project

Open terminal and run:

python main.py


---

## Sample Output

```text
Available Fish Types:
Goldfish, Shark, Angelfish, Tuna, Salmon

Enter fish type (or 'exit' to quit): Goldfish
Goldfish added successfully.

Enter fish type (or 'exit' to quit): Shark
Shark added successfully.

Enter fish type (or 'exit' to quit): Tuna
Tuna added successfully.

Enter fish type (or 'exit' to quit): Tuna
Tuna added successfully.

Enter fish type (or 'exit' to quit): exit

Aquarium Fish Inventory
------------------------------
Goldfish: 1
Shark: 1
Tuna: 2
```
