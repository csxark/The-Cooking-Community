# The Cooking Community

The Cooking Community is a web application built using HTML, CSS, JavaScript, and Django. It provides a platform for food enthusiasts to explore recipes, share their culinary creations, and connect with other cooking aficionados.

## Features 

- Browse and search for recipes
- Add and share your own recipes
- View detailed recipe instructions and ingredients
- Edit and delete your recipes
- Responsive design for mobile and desktop

## Technologies Used

- Frontend: HTML, CSS, JavaScript
- Backend: Django (Python web framework)
- Database: SQLite (default Django database)
- Version Control: Git

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/the-cooking-community.git
   ```

2. Navigate to the project directory:
   ```
   cd the-cooking-community
   ```

3. Create a virtual environment:
   ```
   python -m venv venv
   ```

4. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```
     source venv/bin/activate
     ```

5. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

6. Run database migrations:
   ```
   python manage.py migrate
   ```

7. Start the development server:
   ```
   python manage.py runserver
   ```

8. Open your web browser and visit `http://localhost:8000` to access the application.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).
