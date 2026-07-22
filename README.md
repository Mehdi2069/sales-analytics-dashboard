
# Sales Analytics Dashboard

A professional Business Intelligence (BI) dashboard built with Python and Streamlit for analyzing sales performance, customer behavior, and business insights. The application includes secure authentication, role-based access control, audit logging, and report generation in multiple formats.


##  Live Demo


👉 [https://your-live-app-link.com](https://your-live-app-link.com)



## Project Overview

The **Sales Analytics Dashboard** is a Python-based Business Intelligence application designed to help organizations monitor sales performance, analyze customer behavior, and generate actionable business insights through an intuitive web interface.

Originally developed as a data analysis project, the application evolved into a modular dashboard with enterprise-oriented features including secure authentication, user management, role-based permissions, audit logging, and professional reporting capabilities.

The dashboard enables users to explore sales data through interactive visualizations, filter information by region, product, and date range, monitor key performance indicators (KPIs), and export filtered results to CSV, Excel, and PDF formats.

The project emphasizes clean software architecture, modular design, maintainability, and security. Throughout its development, particular attention was given to separating business logic from presentation, organizing the codebase into reusable modules, and applying software engineering best practices.

This repository demonstrates practical experience in Python application development, Business Intelligence dashboards, data visualization, authentication systems, reporting, and project organization using Git and GitHub.

## Key Features

### 📊 Interactive Sales Dashboard

* Real-time business performance overview
* Key Performance Indicators (KPIs) including:

  * Total Revenue
  * Total Profit
  * Total Orders
  * Profit Margin
  * Average Order Value
* Interactive charts and visualizations
* Dynamic filtering by:

  * Region
  * Product
  * Date Range

### 👥 Customer Analytics

* Customer Segmentation
* Customer Lifetime Value (CLV) analysis
* Repeat Customer Analysis
* Top Customer identification
* Customer-focused visualizations

### 📈 Business Insights

* Automated business insights generation
* Sales trend analysis
* Revenue and profit analysis
* Product performance evaluation
* Regional performance comparison

### 📄 Report Generation

* Export filtered data to CSV
* Export filtered data to Microsoft Excel (.xlsx)
* Export dashboard summary to PDF
* Professional report formatting
* Filter-aware exports

### 🔐 Authentication & Security

* Secure user authentication
* Password hashing using bcrypt
* Password strength validation
* User password change functionality
* Administrator password reset
* Forced password change after password reset
* Session-based authentication

### 👤 User Management

* Create new users
* Delete existing users
* Assign user roles
* Assign regional access
* Activate or deactivate user accounts

### 🛡️ Role-Based Access Control

The application supports multiple permission levels:

* **Administrator**

  * Full system access
  * User management
  * Password reset
  * Access to all sales data

* **Manager**

  * Access limited to assigned region
  * Dashboard and analytics access
  * Personal password management

* **Analyst**

  * Analytics and reporting access
  * Read-only permissions

* **Viewer**

  * Dashboard viewing with restricted functionality

### 📝 Audit Logging

* Successful login tracking
* Failed login tracking
* Security event recording
* User activity logging
* SQLite-based audit database

### 🏗️ Modular Architecture

* Modular Python package structure
* Separated business logic
* Reusable reporting modules
* Dedicated authentication package
* Independent audit logging module
* Organized testing and developer tools

### ⚙️ Developer-Friendly Design

* Virtual environment support
* Requirements-based dependency management
* Git version control
* Clean project organization
* Easily extensible architecture

---

## Tech Stack

## Technology Stack

The Sales Analytics Dashboard is built using a modern Python ecosystem focused on data analysis, business intelligence, security, and maintainability.

| Category                    | Technology         | Purpose                                                |
| --------------------------- | ------------------ | ------------------------------------------------------ |
| **Programming Language**    | Python 3.11        | Core application development                           |
| **Web Framework**           | Streamlit          | Interactive Business Intelligence dashboard            |
| **Data Processing**         | Pandas             | Data cleaning, transformation, filtering, and analysis |
| **Data Visualization**      | Plotly             | Interactive charts and business visualizations         |
| **Excel Reporting**         | OpenPyXL           | Export filtered data to Microsoft Excel (.xlsx)        |
| **PDF Reporting**           | ReportLab          | Generate professional PDF reports                      |
| **Authentication**          | bcrypt             | Secure password hashing and verification               |
| **Database**                | SQLite             | User management and audit logging                      |
| **Version Control**         | Git & GitHub       | Source code management and collaboration               |
| **Development Environment** | Visual Studio Code | Development, debugging, and project management         |
| **Operating System**        | Windows            | Development and testing environment                    |

### Python Libraries

The application makes use of several Python libraries to provide analytics, reporting, and security features.

| Library       | Purpose                                      |
| ------------- | -------------------------------------------- |
| **streamlit** | Interactive web application framework        |
| **pandas**    | Data manipulation and analysis               |
| **plotly**    | Interactive charts and dashboards            |
| **openpyxl**  | Excel report generation                      |
| **reportlab** | PDF report generation                        |
| **bcrypt**    | Password hashing                             |
| **sqlite3**   | Embedded database for users and audit logs   |
| **pathlib**   | Cross-platform file and directory management |
| **datetime**  | Date and time operations                     |
| **io**        | In-memory file generation for downloads      |

### Software Engineering Practices

The project follows several software engineering principles throughout its design and implementation:

* Modular application architecture
* Separation of concerns
* Role-based access control (RBAC)
* Secure password management
* Audit logging for critical events
* Reusable reporting modules
* Organized project structure
* Git version control
* Incremental development with regular testing and refactoring

---

## Project Structure

The project is organized into modular packages, with each directory having a clearly defined responsibility. This structure improves maintainability, readability, and future scalability.

```text
sales_analytics_project/
│
├── app/                        # Streamlit dashboard and user interface
│   ├── __init__.py
│   ├── sales_dashboard.py
│   └── user_management.py
│
├── authentication/             # Authentication and authorization
│   ├── auth.py
│   ├── login.py
│   ├── logout.py
│   ├── password_management.py
│   ├── password_utils.py
│   ├── permissions.py
│   ├── data_permissions.py
│   └── ...
│
├── audit/                      # Audit logging system
│   ├── database.py
│   ├── logger.py
│   └── audit.db
│
├── reports/                    # Report generation modules
│   ├── export_excel.py
│   ├── export_pdf.py
│   └── __init__.py
│
├── scripts/                    # Data processing and analytics
│   ├── clean.py
│   ├── analysis.py
│   ├── visualize.py
│   ├── customer_segmentation.py
│   ├── customer_visualize.py
│   ├── customer_lifetime_value.py
│   ├── repeat_customers.py
│   ├── insights.py
│   └── ...
│
├── config/                     # Configuration files
│
├── data/                       # Source datasets
│
├── docs/                       # Project documentation
│
├── tests/                      # Test scripts
│
├── tools/                      # Development and maintenance utilities
│
├── archive/                    # Archived development files
│
├── output/                     # Generated reports and charts
│
├── main.py                     # Application entry point
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
└── .gitignore                  # Git ignore rules
```

### Directory Overview

* **app/** – Contains the Streamlit user interface and dashboard pages.
* **authentication/** – Handles user authentication, password management, authorization, and role-based access control.
* **audit/** – Records security-related events such as successful and failed logins.
* **reports/** – Generates downloadable reports in PDF and Excel formats.
* **scripts/** – Contains the business logic for data processing, analytics, visualizations, and customer analysis.
* **config/** – Stores configuration files and application settings.
* **data/** – Holds the source datasets used by the dashboard.
* **docs/** – Contains project documentation and technical references.
* **tests/** – Includes scripts used to verify application functionality during development.
* **tools/** – Utility scripts for maintenance, migrations, and administrative tasks.
* **archive/** – Stores legacy files retained for historical reference.
* **output/** – Stores generated reports and visualizations created by the application.


---

## ## Installation Guide

Follow the steps below to set up the Sales Analytics Dashboard on your local machine.

### 1. Clone the Repository

```bash
git clone https://github.com/Mehdi2069/sales-analytics-dashboard.git
cd sales-analytics-dashboard
```

### 2. Create a Virtual Environment

Using a virtual environment is recommended to isolate the project's dependencies.

**Windows**

```bash
python -m venv .venv
```

### 3. Activate the Virtual Environment

**Windows (PowerShell)**

```powershell
.venv\Scripts\Activate.ps1
```

**Windows (Command Prompt)**

```cmd
.venv\Scripts\activate.bat
```

### 4. Install Project Dependencies

Install all required Python packages using the provided `requirements.txt` file.

```bash
pip install -r requirements.txt
```

### 5. Verify the Installation (Optional)

You can confirm that Streamlit has been installed correctly by running:

```bash
python -m streamlit --version
```

If the installation was successful, Streamlit will display its installed version.

### 6. Launch the Application

Start the dashboard using:

```bash
python -m streamlit run main.py
```

Your default web browser should automatically open the application.

If it does not, open the URL displayed in the terminal, which is typically:

```text
http://localhost:8501
```

### Troubleshooting

If you encounter missing module errors such as:

* `ModuleNotFoundError: No module named 'streamlit'`
* `ModuleNotFoundError: No module named 'plotly'`
* `ModuleNotFoundError: No module named 'bcrypt'`

verify that:

* The virtual environment is activated.
* All dependencies have been installed using `pip install -r requirements.txt`.
* You are running the application with the same Python interpreter used to create the virtual environment.

You can verify the active Python interpreter with:
---
## Running the Application

After completing the installation steps and activating the virtual environment, start the Sales Analytics Dashboard with:

```bash
python -m streamlit run main.py
```

Streamlit will start the local web server and open the application in your default browser.

If the browser does not open automatically, navigate to:

```text
http://localhost:8501
```

### Application Startup Flow

When the application starts, the following process takes place:

1. The Streamlit application is initialized.
2. The authentication system checks the user session.
3. Users are prompted to log in with their credentials.
4. After successful authentication:

   * User permissions are loaded.
   * Access restrictions are applied based on the assigned role.
   * The dashboard interface becomes available.
5. Available features are displayed according to the user's permissions.

### Default User Setup

The application supports multiple user roles:

* **Administrator** – Full system access, including user management.
* **Manager** – Access to dashboard features with regional data restrictions.
* **Analyst** – Access to analytical features based on assigned permissions.
* **Viewer** – Limited dashboard access.

### Development Mode

For development or testing purposes, the application can be started with:

```bash
streamlit run main.py
```

The application will automatically reload when source files are modified, making development and debugging easier.

## User Roles & Permissions

The Sales Analytics Dashboard implements a **Role-Based Access Control (RBAC)** system to manage user access and ensure that each user can only access the features and data appropriate for their responsibilities.

User permissions are determined by:

* Assigned user role
* Regional access restrictions
* Application permissions
* Authentication status

The system supports the following user roles:

| Role              | Description                         | Permissions                                                                                    |
| ----------------- | ----------------------------------- | ---------------------------------------------------------------------------------------------- |
| **Administrator** | Full system administrator access    | Complete access to all dashboard features, user management, password reset, and all sales data |
| **Manager**       | Regional business management access | Dashboard access, analytics, reporting, and access limited to the assigned region              |
| **Analyst**       | Business analysis access            | Access to analytical features, reports, and authorized data                                    |
| **Viewer**        | Dashboard viewing access            | Limited access for viewing approved dashboard information                                      |

---

### Administrator

Administrators have full control over the application.

Permissions include:

* Access to all dashboard features
* View all sales data across regions
* Create new user accounts
* Delete user accounts
* Assign user roles
* Assign regional access
* Reset user passwords
* Manage application users

---

### Manager

Managers have business-level access with regional restrictions.

Permissions include:

* View dashboard analytics
* Analyze sales performance
* Generate reports
* Access only assigned regional data
* Change personal password

Example:

A Manager assigned to the **Europe** region can only access sales data belonging to Europe.

---

### Analyst

Analysts are focused on data analysis and reporting activities.

Permissions include:

* View analytical dashboards
* Explore available business insights
* Analyze customer and sales performance
* Generate authorized reports

---

### Viewer

Viewers have restricted access designed for users who only need to monitor information.

Permissions include:

* View approved dashboard content
* Access limited analytical information
* No administrative functionality

---

## Data-Level Security

In addition to feature permissions, the application implements **data-level access control**.

Regional filtering ensures that users only see information they are authorized to access.

Example:

```text
Administrator
    ↓
All Regions

Manager (Europe)
    ↓
Europe Data Only

Manager (Asia)
    ↓
Asia Data Only
```

This approach provides an additional layer of security by controlling not only **what users can do**, but also **what data they can access**.

---

## Authentication Security

The authentication system includes:

* Secure password hashing using bcrypt
* Password validation rules
* User session management
* Password change functionality
* Administrator password reset capability
* Forced password change after administrator reset
* Audit logging of security events



## Dashboard Features

The Sales Analytics Dashboard provides an interactive Business Intelligence interface that enables users to explore sales performance, analyze customer behavior, and generate meaningful business insights.

The dashboard is designed with a focus on usability, allowing users to filter data, visualize key metrics, and export results for further analysis.

---

## Overview Dashboard

The Overview page provides a high-level summary of business performance through interactive KPIs and visualizations.

### Key Performance Indicators (KPIs)

The dashboard displays important business metrics including:

* **Total Revenue**

  * Overall sales revenue generated during the selected period

* **Total Profit**

  * Total profit generated from completed sales

* **Total Orders**

  * Number of sales transactions processed

* **Profit Margin**

  * Percentage relationship between profit and revenue

* **Average Order Value**

  * Average revenue generated per order

---

## Interactive Data Filtering

Users can dynamically filter dashboard information using:

* Region selection
* Product selection
* Date range selection

All dashboard metrics, visualizations, and exports are updated based on the selected filters.

---

## Sales Performance Analysis

The dashboard provides analytical views including:

* Revenue analysis by product
* Revenue analysis by region
* Product performance comparison
* Regional sales performance
* Profitability analysis

Interactive visualizations help users identify trends, opportunities, and areas requiring attention.

---

## Customer Analytics

The customer analytics features provide deeper insight into customer behavior.

Capabilities include:

### Customer Segmentation

Customers are grouped into meaningful segments based on purchasing behavior, helping identify:

* High-value customers
* Medium-value customers
* Low-value customers

### Customer Lifetime Value (CLV)

The dashboard calculates customer lifetime value to help understand long-term customer contribution.

### Repeat Customer Analysis

The application identifies repeat purchasing behavior and helps analyze customer retention patterns.

### Top Customer Analysis

Users can identify the most valuable customers based on sales contribution.

---

## Business Insights

The dashboard includes automated insight generation to support decision-making.

Insights include:

* Sales performance observations
* Product trends
* Regional comparisons
* Customer behavior patterns
* Business opportunities

---

## User Experience Features

The dashboard provides:

* Interactive visualizations
* Responsive layout
* Role-based feature availability
* Secure session handling
* Downloadable reports
* Clear navigation between analytical sections

---

## Available Dashboard Sections

Depending on user permissions, the application provides access to:

| Section                 | Purpose                               |
| ----------------------- | ------------------------------------- |
| **Overview**            | Business performance summary and KPIs |
| **Customers**           | Customer analytics and segmentation   |
| **Insights**            | Automated business insights           |
| **User Management**     | User administration (Admin only)      |
| **Password Management** | Personal password updates             |


## Reporting & Export

The Sales Analytics Dashboard includes integrated reporting capabilities that allow users to export filtered business data and analytical summaries in multiple formats.

Reports are generated based on the user's selected filters, ensuring that exported information matches the current dashboard view.

Supported export formats include:

* CSV
* Microsoft Excel (.xlsx)
* PDF

---

## CSV Export

The CSV export functionality allows users to download filtered sales data in a lightweight, portable format.

Features:

* Export filtered datasets
* Compatible with spreadsheet applications
* Suitable for further data analysis
* Easy integration with other business tools

Example use cases:

* Additional analysis in Excel
* Data sharing between departments
* Import into other analytical systems

---

## Excel Export

The Excel reporting module provides structured spreadsheet exports using the `.xlsx` format.

Features:

* Export dashboard-filtered data
* Preserves structured tabular information
* Compatible with Microsoft Excel
* Suitable for business reporting and further processing

Technology used:

* OpenPyXL

---

## PDF Export

The PDF reporting functionality generates professional summary reports containing key business information.

PDF reports include:

* User information
* Selected filters
* Sales summary metrics
* Revenue information
* Profit information
* Order statistics
* Profit margin
* Average order value

Technology used:

* ReportLab

---

## Filter-Aware Reporting

All reports respect the active dashboard filters.

Example:

```text id="f4sv9q"
User selects:

Region: Europe
Product: Laptop
Date Range: January - March

          ↓

Generated Report:

Europe Laptop Sales
January - March Analysis
```

This ensures that users receive reports relevant to their current analytical context.

---

## Reporting Architecture

The reporting system is separated into dedicated modules:

```text id="psn9na"
reports/

├── export_excel.py
├── export_pdf.py
└── __init__.py
```

This modular design allows additional reporting formats to be added in the future without affecting the dashboard logic.

---

## Future Reporting Improvements

Potential future enhancements include:

* Automated scheduled reports
* Email report delivery
* Custom report templates
* Advanced financial summaries
* Integration with external reporting systems
## Security Features

Security is an essential component of the Sales Analytics Dashboard. The application implements multiple layers of protection to ensure that user accounts, business data, and system activities are managed securely.

The security design follows the principle of **defense in depth**, combining authentication, authorization, password security, and audit tracking.

---

## User Authentication

The application includes a secure login system that verifies user identity before granting access to dashboard functionality.

Features:

* Username and password authentication
* Secure password verification
* User session management
* Authentication state handling
* Protection against unauthorized access

Only authenticated users can access the dashboard.

---

## Password Security

User passwords are never stored as plain text.

The application uses:

* **bcrypt password hashing**
* Secure password verification
* Password validation rules
* Protected password updates

Password-related functionality includes:

* User password change
* Administrator password reset
* Password confirmation validation
* Forced password change after administrator reset

---

## Role-Based Access Control (RBAC)

The application controls access based on user roles.

Security decisions are made by checking:

* User identity
* Assigned role
* Application permissions
* Regional data access

Example:

```text id="9jz7ps"
User Login
     ↓
Authentication Check
     ↓
Role Identification
     ↓
Permission Validation
     ↓
Dashboard Access
```

---

## Data Access Security

The system implements data-level permissions to prevent unauthorized access to business information.

Regional restrictions ensure that users only access data they are allowed to view.

Example:

```text id="57ft5r"
Administrator
    → All Regions

Manager (Europe)
    → Europe Sales Data Only

Manager (Asia)
    → Asia Sales Data Only
```

This provides protection not only at the feature level but also at the data level.

---

## User Management Security

Administrative user management functionality includes:

* Creating user accounts
* Assigning roles
* Assigning regional permissions
* Activating or deactivating users
* Resetting user passwords

Additional safeguards include:

* Preventing administrators from deleting protected accounts
* Validating user permissions before administrative actions

---

## Audit Logging

Security-related activities are recorded through an integrated audit logging system.

Tracked events include:

* Successful logins
* Failed login attempts
* Password changes
* Password resets
* Administrative actions

Audit information is stored in a dedicated SQLite database.

This provides:

* Security monitoring
* User activity tracking
* Troubleshooting capability
* Accountability for important actions

---

## Security Architecture

The security components are separated into dedicated modules:

```text id="q5hlgy"
authentication/

├── auth.py
├── login.py
├── logout.py
├── password_utils.py
├── password_management.py
├── permissions.py
└── data_permissions.py


audit/

├── database.py
└── logger.py
```

This modular approach improves maintainability and allows future security enhancements.

---

## Future Security Improvements

Possible future enhancements include:

* Multi-factor authentication (MFA)
* Password expiration policies
* Advanced user activity monitoring
* External identity providers
* Cloud-based authentication services


## Audit Logging

The Sales Analytics Dashboard includes an integrated audit logging system designed to record important security and user activity events.

Audit logging improves system transparency, supports security monitoring, and provides traceability for important actions performed within the application.

---

## Purpose of Audit Logging

The audit system provides:

* User activity tracking
* Security event monitoring
* Troubleshooting support
* Accountability for important actions
* Historical records of system events

By recording relevant activities, administrators can review what happened, when it happened, and which user performed the action.

---

## Logged Events

The system records important events including:

### Authentication Events

* Successful login attempts
* Failed login attempts
* User authentication activities

Example:

```text id="5g4l7m"
LOGIN_SUCCESS
User logged in successfully
```

---

### Password Management Events

The system tracks password-related activities such as:

* Password changes
* Administrator password resets
* Security-related password actions

---

### Administrative Events

Administrative activities can be recorded, including:

* User management actions
* Account-related changes
* Permission modifications

---

## Audit Database

Audit information is stored in a dedicated SQLite database.

Database structure:

```text id="kwkq4n"
audit/

├── database.py
├── logger.py
└── audit.db
```

The audit table stores information such as:

| Field       | Description                    |
| ----------- | ------------------------------ |
| ID          | Unique event identifier        |
| Timestamp   | Date and time of the event     |
| Username    | User associated with the event |
| Event Type  | Category of the event          |
| Description | Human-readable event details   |
| IP Address  | Source address when available  |
| Details     | Additional event information   |

---

## Audit Logging Architecture

The audit workflow follows this process:

```text id="t6n7q3"
User Action
     ↓
Application Event
     ↓
Audit Logger
     ↓
SQLite Audit Database
     ↓
Security Review
```

This design keeps audit functionality separate from the main application logic.

---

## Benefits

The audit system provides:

* Improved security visibility
* Easier investigation of problems
* Better accountability
* Support for future compliance requirements
* Foundation for advanced monitoring features

---

## Future Enhancements

Possible future improvements include:

* Audit log viewer inside the dashboard
* Advanced filtering and searching
* Exporting audit reports
* Automated security alerts
* Integration with centralized logging platforms


## Project Architecture

The Sales Analytics Dashboard follows a modular application architecture designed to separate user interface, business logic, security, reporting, and data processing responsibilities.

The architecture follows the principle of **separation of concerns**, allowing each component to be developed, tested, and maintained independently.

---

## High-Level Architecture

The application consists of several major layers:

```text
┌─────────────────────────────┐
│        User Interface       │
│       Streamlit App         │
│          app/               │
└──────────────┬──────────────┘
               │
               ↓
┌─────────────────────────────┐
│    Authentication Layer     │
│ authentication/             │
│ Login, Roles, Permissions   │
└──────────────┬──────────────┘
               │
               ↓
┌─────────────────────────────┐
│     Business Logic Layer    │
│ scripts/                    │
│ Cleaning, Analysis, Insights│
└──────────────┬──────────────┘
               │
               ↓
┌─────────────────────────────┐
│       Reporting Layer       │
│ reports/                    │
│ CSV, Excel, PDF Generation  │
└──────────────┬──────────────┘
               │
               ↓
┌─────────────────────────────┐
│        Data Layer           │
│ data/ + SQLite Databases    │
└─────────────────────────────┘
```

---

## Application Flow

When a user starts the application, the following workflow takes place:

```text
Application Startup
        ↓
User Authentication
        ↓
Session Initialization
        ↓
Permission Validation
        ↓
Data Loading
        ↓
Data Filtering
        ↓
Analytics Processing
        ↓
Dashboard Visualization
        ↓
Report Export (Optional)
```

---

## Component Responsibilities

### User Interface Layer (`app/`)

Responsible for:

* Streamlit dashboard pages
* Navigation
* User interaction
* Displaying metrics and charts
* Triggering reports and analytics

Main components:

```text
app/

├── sales_dashboard.py
└── user_management.py
```

---

### Authentication Layer (`authentication/`)

Responsible for:

* User login
* Password verification
* Password management
* Role permissions
* Data access rules

This layer protects the application from unauthorized access.

---

### Analytics Layer (`scripts/`)

Responsible for:

* Data cleaning
* Sales analysis
* Customer segmentation
* Customer lifetime value calculation
* Repeat customer analysis
* Business insight generation
* Visualization preparation

This separation keeps analytical logic independent from the user interface.

---

### Reporting Layer (`reports/`)

Responsible for:

* CSV exports
* Excel generation
* PDF report generation

Reporting functionality is isolated from dashboard code to improve maintainability.

---

### Audit Layer (`audit/`)

Responsible for:

* Recording security events
* Maintaining audit history
* Supporting activity tracking

---

## Design Principles Applied

The project follows several software engineering principles:

### Separation of Concerns

Each module has a clearly defined responsibility.

Example:

* Dashboard displays information
* Scripts analyze data
* Reports generate files
* Authentication controls access

---

### Modular Design

The application is divided into independent components that can be extended or replaced without affecting the entire system.

---

### Maintainability

The project structure supports:

* Easier debugging
* Independent testing
* Future feature additions
* Clear collaboration between developers

---

### Scalability Considerations

The current architecture provides a foundation for future improvements such as:

* Migration from SQLite to PostgreSQL
* REST API integration
* Cloud deployment
* Advanced authentication systems
* Automated data pipelines


## Learning Outcomes

The development of the Sales Analytics Dashboard provided practical experience across multiple areas of software engineering, data analytics, and application development.

Through the implementation of this project, the following skills and concepts were developed:

---

## Python Application Development

* Building a complete Python-based application
* Creating modular and reusable code components
* Organizing a project using professional package structures
* Managing dependencies with `requirements.txt`
* Working with virtual environments
* Debugging and resolving application errors

---

## Data Analysis & Business Intelligence

* Data cleaning and preparation using Pandas
* Exploratory data analysis
* KPI calculation and business metric development
* Sales performance analysis
* Customer segmentation
* Customer Lifetime Value (CLV) analysis
* Business insight generation

---

## Dashboard Development

* Building interactive dashboards with Streamlit
* Creating user-friendly navigation
* Implementing dynamic filters
* Displaying business metrics and visualizations
* Integrating analytical modules into a web application

---

## Data Visualization

* Designing interactive charts with Plotly
* Creating meaningful business visualizations
* Presenting analytical results in an understandable format
* Transforming raw data into actionable information

---

## Application Security

* Implementing user authentication
* Understanding password security principles
* Using bcrypt for password hashing
* Creating role-based access control (RBAC)
* Applying data-level permissions
* Implementing secure password management workflows

---

## Database & Logging Systems

* Working with SQLite databases
* Designing user and audit data storage
* Creating audit logging functionality
* Tracking security-related events
* Understanding application traceability

---

## Reporting Systems

* Generating CSV exports
* Creating Excel reports with OpenPyXL
* Creating PDF reports with ReportLab
* Designing reusable reporting modules

---

## Software Engineering Practices

* Applying separation of concerns
* Refactoring project structure
* Managing code using Git and GitHub
* Organizing tests and development tools
* Improving project maintainability
* Writing technical documentation

---

## Problem Solving & Debugging

Throughout development, practical experience was gained in:

* Resolving dependency issues
* Debugging Python import problems
* Managing package structures
* Troubleshooting environment configuration
* Improving application reliability through testing

---

## Overall Experience

This project represents a transition from developing individual data analysis scripts toward building a complete software application with:

* A user interface
* Security layer
* Data processing pipeline
* Reporting system
* Database integration
* Professional project organization

The project demonstrates the combination of **data analytics skills and software engineering practices** required to build practical business applications.



## Table of Contents

- [Project Overview](#project-overview)
- [Key Features](#key-features)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Installation Guide](#installation-guide)
- [Running the Application](#running-the-application)
- [User Roles & Permissions](#user-roles--permissions)
- [Dashboard Features](#dashboard-features)
- [Reporting & Export](#reporting--export)
- [Security Features](#security-features)
- [Audit Logging](#audit-logging)
- [Project Architecture](#project-architecture)
- [Future Enhancements](#future-enhancements)
- [Learning Outcomes](#learning-outcomes)
- [Author](#author)
- [License](#license)

# Sales Analytics Dashboard

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Streamlit](https://img.shields.io/badge/Framework-Streamlit-red)
![Pandas](https://img.shields.io/badge/Data-Pandas-green)
![Plotly](https://img.shields.io/badge/Visualization-Plotly-purple)
![SQLite](https://img.shields.io/badge/Database-SQLite-lightgrey)
![License](https://img.shields.io/badge/License-MIT-green)



(image-1.png)

docs/
└── images/
    └── architecture.png


## Demo

The application provides:

- Secure login
- Role-based dashboard access
- Interactive analytics
- Customer insights
- Report generation

Live Demo:
https://your-demo-url.com

## Author

**Mehdi Latifaj**

Python Developer | Data Analytics | Business Intelligence

GitHub:
https://github.com/Mehdi2069

## License

This project is licensed under the MIT License.

## Main Section

### Subsection

