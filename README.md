\# Kart Maintenance Tracker

\### Nova 23 Racing (N5R) Technical Initiative



A specialized fleet management system designed to track maintenance intervals, part lifespans, and performance logs for competitive karting. Developed as part of the N5R STEM outreach program.



\## Project Goal

To provide a data-driven approach to karting maintenance, ensuring safety and peak performance for drivers in the STEM racing programs, including collaborations with partners like Spire Motorsports.


## Current Features
* **Fleet Dashboard:** View real-time status of all chassis in the N5R fleet.
* **Relational Tracking:** Cascading hour updates (updating kart hours automatically updates all attached components).
* **Component Lifespan Alerts:** Visual "Service Required" warnings when parts exceed their maximum hour limit.
* **Maintenance Audit Trail:** Detailed log history for every part, tracking specific service dates and technician notes.

## Project Structure
* `app.py`: Main Flask application and backend logic.
* `schema.sql`: Database architecture for Karts, Parts, and Logs.
* `init_db.py`: Script to initialize the SQLite database.
* `templates/`: HTML interface files.


\## Tech Stack

\* \*\*Backend:\*\* Python / Flask

\* \*\*Database:\*\* SQLite / SQL

\* \*\*Frontend:\*\* HTML5, CSS3, JavaScript



\## Setup Instructions

1\. Clone the repository.

2\. Create a virtual environment: `python -m venv venv`.

3\. Activate: `.\\venv\\Scripts\\Activate.ps1`.

4\. Install dependencies: `pip install -r requirements.txt`.

