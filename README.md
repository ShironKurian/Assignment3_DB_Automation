# Assignment 3: Web App with MySQL & Selenium

## Installation
1. Install dependencies:
   ```bash
   pip install flask mysql-connector-python selenium
   ```
2. Set up MySQL:
   - Create the `users` database and `users` table.
   - Ensure MySQL server is running.

3. Run the Flask app:
   ```bash
   python app.py
   ```

4. Run the Selenium test:
   ```bash
   python selenium_test.py
   ```

## Files
- `app.py`: Flask web app that handles user login and data insertion into MySQL.
- `db_config.py`: MySQL connection configuration.
- `selenium_test.py`: Selenium script that automates login form submission and verifies the data in MySQL.
- `templates/index.html`: HTML login form used in the Flask app.
- `requirements.txt`: Contains the required dependencies.

## Screenshots
Check the `screenshots/` folder for the following:
- Screenshot of the running web app.
- Screenshot of the MySQL database showing the inserted user data.
- Screenshot of the Selenium test execution output.

## Notes
- Ensure MySQL is running and accessible when testing the Selenium script.
- Make sure to install all the dependencies using `pip install -r requirements.txt` before running the app or tests.


