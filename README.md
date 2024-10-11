# Summoner Wars Rune Optimizer

### Overview

Summoner Wars Rune Optimizer is a web application designed to help players of the mobile game Summoners War optimize their rune setups for monsters. Built using Django and Django REST Framework, this app provides a robust backend API that can be used with various frontend interfaces.

### Features

    •	Rune Management: Add, update, and delete runes.
    •	Monster Management: Manage your monster collection.
    •	Optimization Algorithms: Optimize rune builds based on user-defined criteria.
    •	User Authentication: Secure login and registration system.
    •	RESTful API: Access and manipulate data through API endpoints.

### Technologies Used

    •	Python 3.x
    •	Django
    •	Django REST Framework
    •	SQLite (default database, can be replaced with PostgreSQL or MySQL)
    •	Docker (optional, for containerization)
    •	Git for version control

### Getting Started

- Prerequisites

  • Python 3.x installed on your system.
  • pip package manager.
  • Virtual Environment tool like venv or virtualenv.
  • Git for cloning the repository.
  • Docker (optional, if you prefer containerization).

- Installation

  1.  Clone the Repository

```bash
git clone https://github.com/yourusername/summoner-wars-rune-optimizer.git
cd summoner-wars-rune-optimizer
```

2. Create a Virtual Environment

```bash
python3 -m venv venv
```

3. Activate the Virtual Environment

- On Windows:

`venv\Scripts\activate`

- On macOS/Linux:

`source venv/bin/activate`

4. Install Dependencies

`pip install -r requirements.txt`

5. Apply Migrations

`python manage.py migrate`

6. Create a Superuser

`python manage.py createsuperuser`

7. Run the Development Server

`python manage.py runserver`

8. Access the Application
   Open your web browser and navigate to http://127.0.0.1:8000/.

### API Documentation

API Documentation

The API provides endpoints for managing runes, monsters, and optimization processes.

Base URL

http://127.0.0.1:8000/api/

Endpoints

    •	Runes
    •	GET /runes/ - List all runes.
    •	POST /runes/ - Create a new rune.
    •	GET /runes/{id}/ - Retrieve a specific rune.
    •	PUT /runes/{id}/ - Update a rune.
    •	DELETE /runes/{id}/ - Delete a rune.
    •	Monsters
    •	GET /monsters/ - List all monsters.
    •	POST /monsters/ - Create a new monster.
    •	GET /monsters/{id}/ - Retrieve a specific monster.
    •	PUT /monsters/{id}/ - Update a monster.
    •	DELETE /monsters/{id}/ - Delete a monster.
    •	Optimization
    •	POST /optimize/ - Optimize rune setups based on criteria.

### Deployment

    1.	Configure Environment Variables

Set DEBUG=False and configure allowed hosts in settings.py. 2. Use a Production-Ready Server
Use servers like Gunicorn or uWSGI along with Nginx. 3. Configure the Database
Replace SQLite with PostgreSQL or another production-ready database. 4. SSL Certificate
Secure your application with SSL certificates.

### Contributing

Contributions are welcome! Please follow these steps:

    1.	Fork the Repository
    2.	Create a Feature Branch

git checkout -b feature/YourFeature

    3.	Commit Your Changes

git commit -m 'Add some feature'

    4.	Push to the Branch

git push origin feature/YourFeature

    5.	Open a Pull Request

License

This project is licensed under the MIT License. See the LICENSE file for details.

Contact

> Author: Non

> Email: @fadingNA

> GitHub: @fadingNA
