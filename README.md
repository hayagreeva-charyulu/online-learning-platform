# 🎓 Online Learning Platform

An interactive web-based learning platform built with Django where students and teachers can engage through courses, enrollment, and role-based access. The platform also supports user registration, login, profile management, and course creation.

---

## 🚀 Features

- ✅ User Registration & Login
- ✅ Role-Based Access (Student & Teacher)
- ✅ Create & Manage Courses (for Teachers)
- ✅ Enroll in Courses (for Students)
- ✅ User Dashboard with Enrolled Courses
- ✅ Profile with Bio
- ✅ Responsive Navbar with Login, Register, Profile, Dashboard, etc.
- ✅ Assignments & Progress Tracking *(basic implementation)*

## 🛠️ Technologies Used

- **Backend:** Django, SQLite
- **Frontend:** HTML, CSS, Javascript (Bootstrap)
- **Authentication:** Django’s built-in User Auth
- **Styling:** Bootstrap 5

---

## 🏗️ Project Structure

```bash
online-learning-platform/
│
├── backend/               # Main Django project
├── users/                 # User-related models, views, forms
├── courses/               # Course models, views, and enrollment
├── templates/             # HTML templates
│   ├── users/
│   └── courses/
├── static/                # CSS, JS, and static files
├── media/                 # Uploaded content (optional)
├── venv/                  # Virtual environment (excluded)
├── db.sqlite3             # SQLite DB
├── manage.py              # Django runner
├── requirements.txt       # Dependencies
└── README.md              # You're here!
