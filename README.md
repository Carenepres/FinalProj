# django_todo_app
This Todo App built with Django is a great to learn how to implement CRUD operations in Django.

## Description

The Django Todo App is a simple application that allows users to manage their tasks. Users can create, update, and delete tasks. The application includes basic CRUD functionality and a user-friendly interface.

## Features

- Create new tasks
- Update existing tasks
- Delete tasks
- Input validation to prevent numeric-only task titles
- Responsive and modern user interface
- Centered delete confirmation box for better user experience

## Project Setup

### Prerequisites

- Python 3.8+
- Django 4.2.7

### Installation Steps

1. Clone the repository:
   ```sh
   git clone https://github.com/Carenepres/FinalProj.git
   cd todoapp
   ```

2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Option 2: Generate the Database**
   - If you want users to generate the database, instruct them to run the following commands:
     ```sh
     python manage.py migrate
     ```


4.  Run the development server:
   ```sh
   python manage.py runserver
   ```

## Usage

1. Open the application in a web browser by navigating to `http://127.0.0.1:8000/`.
2. To add a new task, enter the task title in the input box and click the "Add" button.
3. To update a task, click the edit icon next to the task, modify the title, and save.
4. To delete a task, click the delete icon next to the task and confirm the deletion.

## Future Enhancements

- Implement user authentication and authorization.
- Add due dates and priority levels to tasks.
- Implement search and filter functionality for tasks.

## References and Resources

- [Django Documentation](https://docs.djangoproject.com/en/4.2/)
- [Bootstrap Documentation](https://getbootstrap.com/docs/5.2/getting-started/introduction/)
- [Google Fonts](https://fonts.google.com/)
- [Font Awesome](https://fontawesome.com/)
```