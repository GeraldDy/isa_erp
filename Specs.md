# ISA ERP System Specifications

This document outlines the technical specifications and features of the ISA ERP System.

## 1. Project Overview

ISA ERP is a web-based Enterprise Resource Planning system designed to manage core business processes. It is built using the Django web framework for the backend and Tailwind CSS for the frontend, providing a modern and responsive user interface. The system features a modular architecture, initially focusing on Inventory and Sales management.

## 2. Technology Stack

- **Backend:**
    - Python 3.10+
    - Django 5.0.6
    - Django Crispy Forms
    - Gunicorn (for production)
- **Frontend:**
    - HTML5 / CSS3
    - Tailwind CSS with DaisyUI
    - JavaScript
- **Database:**
    - PostgreSQL (Default)
    - SQLite (for development)
- **Development & Tooling:**
    - `pip` for Python package management
    - `npm` for frontend package management
    - Virtual Environment (`venv`)

## 3. Core Modules & Features

### 3.1. Dashboard
- **URL:** `/`
- **View:** `dashboard_view`
- **Template:** `home.html`
- **Description:** Provides an overview of system activities, including statistics on sales and pending orders.

### 3.2. Product Management
- **URL Prefix:** `/products`
- **Models:** `Product`
- **Views:**
    - `product_list`: Displays a list of all products.
    - `product_detail`: Shows details for a specific product.
    - `product_create`: Form to add a new product.
    - `product_update`: Form to edit an existing product.
    - `product_delete`: Confirmation page to delete a product.
- **Templates:** Located in `templates/products/`.

### 3.3. Customer Management
- **URL Prefix:** `/customers`
- **Model:** `Customer`
- **Views:**
    - `customer_list`: Displays a list of all customers.
    - `customer_detail`: Shows details for a specific customer.
    - `customer_create`: Form to add a new customer.
    - `customer_update`: Form to edit an existing customer.
    - `customer_delete`: Confirmation page to delete a customer.
- **Templates:** Located in `templates/customers/`.

### 3.4. Order Management
- **URL Prefix:** `/orders`
- **Models:** `Order`, `OrderItem`
- **Views:**
    - `order_list`: Displays a list of all orders.
    - `order_detail`: Shows details for a specific order and its items.
    - `order_create`: Form to create a new order with multiple items.
    - `order_update`: Form to edit an existing order and its items.
    - `order_delete`: Confirmation page to delete an order.
- **Templates:** Located in `templates/orders/`.

### 3.5. Authentication
- **URLS:** `/login/`, `/logout/`
- **Views:** `login_view`, `logout_view`
- **Description:** Utilizes Django's built-in authentication system for user login and session management.

## 4. Data Models

### `Product`
- `id`: UUID (Primary Key)
- `product_id`: CharField
- `product_name`: CharField
- `product_description`: TextField
- `price`: DecimalField
- `unit_of_measure`: CharField
- `quantity`: PositiveIntegerField
- `brand`: CharField
- `selling_price`: DecimalField
- `status`: CharField
- `created_at`: DateTimeField
- `updated_at`: DateTimeField

### `Customer`
- `id`: UUID (Primary Key)
- `registered_name`: CharField
- `business_address`: TextField
- `tin_number`: CharField
- `mobile_tel_number`: CharField
- `email_address`: EmailField
- `created_at`: DateTimeField
- `updated_at`: DateTimeField

### `Order`
- `id`: UUID (Primary Key)
- `customer`: ForeignKey to `Customer`
- `order_date`: DateField
- `total_amount`: DecimalField
- `created_at`: DateTimeField
- `updated_at`: DateTimeField

### `OrderItem`
- `id`: UUID (Primary Key)
- `order`: ForeignKey to `Order`
- `product`: ForeignKey to `Product`
- `quantity`: PositiveIntegerField
- `price`: DecimalField
- `created_at`: DateTimeField
- `updated_at`: DateTimeField

## 5. Frontend Structure

- **Base Template:** `templates/layouts/base.html` provides the main site structure, including the sidebar and top navigation.
- **Styling:** The `theme` app manages frontend assets. Raw CSS is in `theme/static_src/src/styles.css` and compiled by Tailwind into `theme/static/css/dist/styles.css`.
- **Templates:** Application-specific templates are organized into subdirectories within the `templates` folder (e.g., `templates/products`, `templates/customers`).

## 6. Project Structure Highlights

- `isa_erp/`: Main project configuration directory.
- `main_app/`: The core application containing models, views, and URLs for the ERP modules.
- `theme/`: A Django app to manage frontend assets and Tailwind CSS integration.
- `static/`: Project-wide static files (images, js).
- `templates/`: Project-wide HTML templates.

## 7. Future Improvements (from README)
- Dashboard analytics
- Notifications
- Mobile responsiveness enhancements
- Role-based access control (RBAC)
- Potential frontend upgrade to a framework like React.
