# ISA ERP System

A modern **ERP (Enterprise Resource Planning) Web Application** built with:

* Django (Backend)
* Tailwind CSS + DaisyUI (Frontend)
* `django-widget-tweaks` for form styling
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
│   └── layouts/
│       └── base.html
│
├── main_app/
└── static/
```

---

# Requirements

* Python 3.10+
* pip

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

## 4. Apply Database Migrations

```
python manage.py migrate
```

---

## 5. Create Superuser (Optional)

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
* User section with a dropdown menu

## Responsive Design

* Built with Tailwind CSS and DaisyUI
* Clean, modern, and light-themed layout

---

# Authentication

* Django built-in authentication
* Logout button in the user dropdown menu
* CSRF protection enabled

---

# Customization

* Add new modules (HR, Accounting)
* Implement role-based access
* Integrate APIs

---

# Author

GERALD D. BALLETA

---

# License

For internal or development use.
