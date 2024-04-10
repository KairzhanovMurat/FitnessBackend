# Fitness Trainers Scheduling Management Application Backend

This repository contains the backend for a fitness trainers scheduling management application.

## Running

To run the project in Docker, follow these steps:

1. **Install Docker and Docker Compose** if they're not already installed.
2. **Clone the repository:** `git clone https://github.com/KairzhanovMurat/FitnessBackend.git`
3. **Go to project directory:** `cd FitnessBackend`
4. **Run the service with Docker:** `docker-compose up --build`
5. **After successful startup, the application will be available at** `http://127.0.0.1:8000/`
   - Project is already prepopulated with test data
   - **Credentials for login:**
     - email: admin@mail.com
     - password: 123
6. **Enter the credentials to `/auth/token/` endpoint to receive token.**
7. **Enter the token in login form like:** `Token <actual_token>`  
