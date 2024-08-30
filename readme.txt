1. Extract the project files from the zip archive.

2. Open a terminal or command prompt.

3. Create a new virtual environment (optional but recommended):
   ```bash
   python3 -m venv /path/to/your/virtualenv

4. Activate the virtual environment:
   For Linux: source /path/to/your/virtualenv/bin/activate
   For Windows: C:\path\to\your\virtualenv\Scripts\activate

5. Navigate to the extracted project directory in the terminal or command prompt.

6. Install the required packages using pip:
   ```bash
   pip install -r requirements.txt

7. Apply database migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate

8. Create a superuser:
   ```bash
   python manage.py createsuperuser

9. Start the development server:
   ```bash
   python manage.py runserver

10. Access the admin panel by visiting http://127.0.0.1:8000/admin/ in your web browser and log in using the superuser credentials.

11. Use the provided "PhoneBook_Spam.postman_collection.json" file to test the endpoints using tools like Postman. Import the JSON file into Postman to automatically populate the API endpoints and sample requests.

12. Explore the API endpoints and functionalities according to the project requirements.

Note: Replace /path/to/your/virtualenv with the actual path to your desired virtual environment directory.

In these instructions, steps 3 and 4 are for creating and activating a virtual environment, which is recommended for isolating project dependencies and ensuring compatibility across different projects. Adjust the paths and commands as needed based on your specific setup.
