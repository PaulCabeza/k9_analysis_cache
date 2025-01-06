# k9_analysis_cache

## Description

`k9_analysis_cache` is a Django project designed to implement a model that interacts with a MySQL database. The primary goal of this project is to create a Django model that allows for efficient access to analysis cache data. The model includes a method to bulk load records based on the `partition_id` field. Additionally, unit tests have been implemented to ensure the proper functionality of the create, read, and bulk read methods.

## Requirements

- Python 3.8 or higher
- Django 5.1.4
- MySQL
- Docker (for running MySQL in a container)
- pip

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/PaulCabeza/k9_analysis_cache.git
   cd k9_analysis_cache
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the MySQL database**:
   You can run a MySQL container using Docker. Use the following command to start a MySQL container:
   ```bash
   docker run --name mysql-container -e MYSQL_ROOT_PASSWORD=my_secret_password -d -p 3306:3306 mysql:latest
   ```

5. **Create a database**:
   After starting the MySQL container, connect to it and create a database:
   ```bash
   docker exec -it mysql-container mysql -u root -p
   # Enter the password: my_secret_password
   CREATE DATABASE k9_analysis;
   ```

6. **Configure the database settings**:
   Update your `.env` file or directly in `settings.py` with the following database configuration:
   ```plaintext
   DB_NAME=k9_analysis
   DB_USER=root
   DB_PASSWORD=my_secret_password
   DB_HOST=localhost
   DB_PORT=3306
   ```

7. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

8. **Create a superuser** (optional):
   ```bash
   python manage.py createsuperuser
   ```

9. **Run the server**:
   ```bash
   python manage.py runserver
   ```

## Project Structure

- `cachemanager/`: Contains the model logic and unit tests.
- `k9_analysis_cache/`: Django project configuration.
- `tests.py`: Contains unit tests for the model and cache functionality.

## Testing

To run the unit tests, ensure your test database is configured and execute:
bash
pytest
```

### Customization

- **Description**: Ensure that the description accurately reflects the purpose and functionality of your project.
- **Requirements**: Add any additional requirements your project may have.
- **Installation**: Make sure the installation steps are clear and precise.
- **Project Structure**: You can add more details about the project structure if necessary.
- **Contributions**: If you have a specific process for contributions, include it.

This README.md provides a comprehensive overview of your project, including setup instructions for running a MySQL container with Docker, which should help users understand how to get started with your project.

## Contributions

Contributions are welcome! If you would like to contribute, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.