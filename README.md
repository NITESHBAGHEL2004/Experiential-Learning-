# Experiential Learning Activity Management System

This project is a web-based application designed to manage and document Experiential Learning Activities (ELA) conducted by faculty and students. The goal is to digitize the process of recording, storing, and reporting learning activities that go beyond classroom instruction and promote real-world engagement.

## 🌟 Features

- Dynamic dropdown selection for Academic Year, School, Program, Branch, Faculty, Semester, Section, and Subject.
- PBL (Project-Based Learning) or Experiential Learning Activity selection from existing list or enter new ("OTHER").
- Interactive form to input:
  - Activity description
  - Activity marks
  - Date of activity (start and end)
  - Upload supporting documents (PDF format only)
  - Multiple LMS submission links
- Real-time form rendering based on activity selection
- CSRF-protected form submission
- Success message display after form submission
- Editable and report-generating functionality (linked via navigation)

## 🛠️ Tech Stack

- **Frontend:** HTML, CSS, JavaScript (vanilla)
- **Backend:** Django (Python)
- **Database:** SQLite (or PostgreSQL/MySQL based on your setup)
- **Templates:** Django templating engine
- **Security:** CSRF protection, input validations


