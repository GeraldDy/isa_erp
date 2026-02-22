# ISA ERP System

A modern **ERP (Enterprise Resource Planning) Web Application** built with:

* Django (Backend)
* Tailwind CSS + DaisyUI (Frontend)
* Modular Architecture (Inventory & Sales)

---

# Features

## Dashboard

* Overview of system activities
* Quick insights (Sales, Inventory, etc.)

## Inventory Module

* Manage Stocks
* Supplier Management
* Warehouse Tracking

## Sales Module

* Orders Management
* Invoice Generation
* Customer Records

## System

* Configuration Settings
* User Management (extendable)

---

# Project Structure

```
isa_erp/
│
├── manage.py
├── isa_erp/
│   └── settings.py
│
├── templates/
│   └── layout/
│       └── base.html
│
├── theme/
├── main_app/
└── static/
```

---

# Requirements

* Python 3.10+
* pip
* Node.js (LTS recommended)
* npm

---

# Installation Guide

## 1. Clone the Project

```
git clone <your-repo-url>
cd isa_erp
```

---

## 2. Create Virtual Environment

```
python -m venv venv
```

Activate:

### Windows

```
venv\Scripts\activate
```

### Linux / Mac

```
source venv/bin/activate
```

---

## 3. Install Python Dependencies

```
pip install -r requirements.txt
```

---

## 4. Install Node.js Dependencies

Check installation:

```
node -v
npm -v
```

Download if needed:
https://nodejs.org

---

## 5. Configure Tailwind

If npm is not detected, add in `settings.py`:

```
NPM_BIN_PATH = r"C:\Program Files\nodejs\npm.cmd"
```

Then run:

```
python manage.py tailwind install
```

---

## 6. Apply Database Migrations

```
python manage.py migrate
```

---

## 7. Create Superuser (Optional)

```
python manage.py createsuperuser
```

---

# Run the Application

```
python manage.py runserver
```

Open in browser:

```
http://127.0.0.1:8000/
```

---

# UI Overview

## Sidebar Layout

* Left-side navigation
* Modules:

  * Dashboard
  * Inventory
  * Sales
  * System

## Top Navbar

* Page title
* User section

## Responsive Design

* Built with Tailwind CSS
* Clean layout

---

# Authentication

* Django built-in authentication
* Logout button in sidebar
* CSRF protection enabled

---

# Customization

* Add new modules (HR, Accounting)
* Implement role-based access
* Integrate APIs
* Upgrade frontend to React

---

# Common Issues & Fixes

## Tailwind Install Error

```
NPM_BIN_PATH = r"C:\Program Files\nodejs\npm.cmd"
```

---

## TemplateDoesNotExist

```
TEMPLATES = [
    {
        'DIRS': [BASE_DIR / "templates"],
    },
]
```

---

## Static Files Not Loading

```
python manage.py collectstatic
```

---

# Future Improvements

* Dashboard analytics
* Notifications
* Mobile responsiveness
* Role-based access control
* React frontend integration

---

# Author

GERALD D. BALLETA

---

# License

For internal or development use.
