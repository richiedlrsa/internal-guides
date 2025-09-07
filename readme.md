# Internal Guides and SOPs
    A web application to organize and manage internal policies and procedures.

## Description

This website allows organizations to easily store, organize and manage internal guides and SOPs, minimizing reliance on tribal knowledge. It includes secure user authentication and role-based access control. Users with the _user_ role can look up and view existing guides. Users with the _admin_ role can add, view, delete and update existing guides, as well as manage other users.

## Key Features
* **Secure User Authentication**: Ensures that the information is only accessible by authorized users.
* **Role-based Access Control**: Some functionalities will be disabled/enabled based on permissions (admin vs user).
* **Full Crud Functionality**:  Admins have complete control to **C**reate, **R**ead, **U**pdate and **D**elete existing guides.
* **Dynamic Search**: A powerful search bar allows users to instantly find guides by querying both titles and content.
* **Markdown Support**: Guide is rendered with Markdown, allowing for rich text formatting, including headers, lists, and links.
* **User Management**: Admins have access to a dedicated interface to view all users and manage their roles.

## Requirements
* Python 3.8+
* pip (Package Installer for Python)
* Git

## Set up & Installation
1. **Clone the repository**: 
```git clone https://github.com/richiedlrsa/internal-guides
cd internal-guides
```

2. Create and activate virtual environment (Recommended):
```
# For macOS/Linux
python3 -m venv venv
source venv/bin/activate

# For Windows
python -m venv venv
.\venv\Scripts\active

3. **Install required packages**:
``` 
pip install -r requirements.txt
```

## How to Use
1. **Launch the App**: Run the main python script to start the Falsk web server.
```
python main.py
```
2. **Navigate to the Website**: Open your browser and go to the local address provided (usually http://127.0.0.1:5000)
3. **Create an account**: New users must first register for an account by providing their name, email and a secure password. 
4. **Log in**: Use your credentials to log in. You will be redirected to the home page where you'll find all available SOPs.
5. Using the site:
    * **Search for Guides**: Use the search bar at the top of the home page to filter guides by keywords in their title or content.
    * **View a guide**: Click on a guide's title to view its content
    * **Admin - Add a Guide**: If you are an admin, click the  "➕ Add New Guide" button to access a form where you can create a new guide using Markdown.
    * **Admin - Edit/Delete a Guide**: Admins will see "Edit" and "Delete" buttons next to each guide.
    * **Admin - Manage Users**: Admins can click on the "Users" link in the navigation bar to view a list of all registered users and modify their roles.

## Important
* Standard _users_ have read-only access to guides, while admins have full CRUD permissions.
* The content is parsed as Markdown. Be sure to use proper Markdown syntax when adding a guide's content.
* All fields in the registration, login, and guide creation/editing form are **required**.