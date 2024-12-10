# Budget App

Welcome to the Budget App! This application was developed as part of a software testing project to demonstrate various testing techniques and ensure the robustness of the system.

## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Installation](#installation)
4. [Running the App in Testing Configuration](#running-the-app-in-testing-configuration)
5. [Running the Tests](#running-the-tests)

## Overview

The Budget App allows users to manage their expenses by registering, logging in, managing budgets, tracking income and expenses, and viewing budget summaries.

## Features

- User registration and authentication
- Budget Management
- Expense Tracking
- Report Generation

## Installation

To run the Budget App, ensure you have the following prerequisites:

- Python 3.8 or higher
- `virtualenv` (optional but recommended)

### Step-by-Step Installation

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/yourusername/budget-app.git
    cd budget-app
    ```

2. **Create a Virtual Environment** (optional but recommended):

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install Dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

## Running the App in Testing Configuration

To run the app in the testing configuration, follow these steps:

1. **Set the Environment Variables**:

    ```bash
    export FLASK_APP=app.py # On Windows, use 'set FLASK_APP=app.py'
    export FLASK_CONFIG=testing  # On Windows, use `set FLASK_CONFIG=testing`
    ```

2. **Run the Application**:

    ```bash
    flask run
    ```

The app will be available at `http://localhost:5000`.

## Running the Tests

This project includes several tests to ensure the application's security and functionality. To run the tests, follow these steps:

1. **Run the Model Unit Tests**:

    ```bash
    python run_tests_models.py
    ```
2. **Run the Integration Unit Tests**:
    ```bash
    python run_tests_endpoints.py
    ```
3. **Run the System Selenium Tests**:
   ```bash
    python run_tests_system.py
    ```


