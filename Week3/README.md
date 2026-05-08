# MSE800 Week 3 - Activity 1.2
   ## Updated ER Diagram with Lecturer Entity

   Added Lecturer entity per W3-A1.1 requirements.

   ![ERD](MSE800_Week3_Activity1-2_Kiran.png)

   ### Entities
   1. **Student**: Student_ID(PK), Name, Email
   2. **Course**: Course_ID(PK), Course_Name, Duration, Lecturer_ID(FK)
   3. **Enrollment**: Enrollment_ID(PK), Student_ID(FK), Course_ID(FK), Grade, Status
   4. **Lecturer**: Lecturer_ID(PK), FirstName, LastName, Email, Department - NEW

   ### Relationships
   - Student 1:N Enrollment
   - Course 1:N Enrollment
   - Lecturer 1:N Course
