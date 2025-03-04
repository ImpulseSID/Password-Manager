# Password Manager

A simple password manager that allows users to store passwords along with their associated username and website. It features a **React frontend**, a **Flask backend**, and a **MySQL database** for storage.

## Features

- 🔑 Generate random passwords.
- 💾 Store passwords with username and website information.
- 🔍 Retrieve stored passwords.

## Technologies Used

- **Frontend**: React, Vite
- **Backend**: Flask
- **Database**: MySQL

## Setup Instructions

### Prerequisites

Ensure you have the following installed:

- [Node.js](https://nodejs.org/)
- [Python](https://www.python.org/)
- [MySQL](https://www.mysql.com/)

### 1️⃣ Set Up the Frontend

```sh
# Navigate to the frontend directory
cd password-manager

# Install dependencies
npm install

# Start the development server
npm run dev
```

The frontend will be available at [**http://localhost:5173/**](http://localhost:5173/).

### 2️⃣ Set Up the Backend

```sh
# Navigate to the backend directory
cd backend

# Install dependencies
pip install flask mysql-connector-python flask-cors

# Start the Flask server
python backend.py
```

The backend will be available at [**http://localhost:5000/**](http://localhost:5000/).

### 3️⃣ Set Up the MySQL Database

Run the following SQL commands to create the database and table:

```sql
CREATE DATABASE password_manager;
USE password_manager;
CREATE TABLE credentials (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    website VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
);
```

### 4️⃣ Update MySQL Credentials

Edit `backend.py` and replace `your_username` and `your_password` with your actual MySQL credentials.

## Stopping the Application

- **Frontend**: Press `Ctrl + C` in the terminal where `npm run dev` is running.
- **Backend**: Press `Ctrl + C` in the terminal where `python backend.py` is running.

## 🚀 Future Improvements

- 🔐 User authentication.
- 🔏 Password encryption.
- 🖥️ UI for managing stored passwords.

## 📜 License

This project is open-source and free to use.

