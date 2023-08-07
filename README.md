# CZBioHubSF_Assessment

## fibbo_series
The Fibbo_series is a Django web application that allows users to generate and display Fibonacci numbers.

### Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.8 or higher is installed.
- Pip package manager is installed.
- Git is installed.
- SQLite database is used for development.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/PrudhviVeeravelly/CZBioHubSF_Assessment.git

### SetUp
1. Navigate to the project directory:

   ```
   cd fibonacci-generator
2. Create and activate a virtual environment:

   ```
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate

3. Install project dependencies:

   ```
   pip install -r requirements.txt

4. Apply database migrations:

   ```
   python manage.py makemigrations
   python manage.py migrate

5. Start the development server:

   ```
   python manage.py runserver

### Usage
1.  Access the Fibonacci Generator web application by visiting http://127.0.0.1:8001 in your web browser.

2. Enter a positive integer n and submit the form to generate the first n Fibonacci numbers.

3. The generated Fibonacci numbers will be displayed on the page.
