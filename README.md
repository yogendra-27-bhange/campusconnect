# Django College Management CRUD System

This is a simple Django-based web application for managing student records in a college. It supports full CRUD (Create, Read, Update, Delete) functionality using Django forms and templates.

## 🚀 Features

- List all students
- Add new student
- Edit existing student details
- Delete student record
- Bootstrap-styled HTML templates

## 🛠️ Tech Stack

- Python 3.10+
- Django 5.1.7
- HTML, CSS (Bootstrap)
- SQLite (default Django DB)

## 📁 Project Structure

campusconnect/
├── campusconnect/ # Project settings
├── students/ # Student app
│ ├── templates/
│ │ └── student/
│ │ ├── student_list.html
│ │ ├── student_form.html
│ │ └── student_confirm_delete.html
│ ├── models.py
│ ├── views.py
│ ├── forms.py
│ ├── urls.py
│ └── ...
└── manage.py


