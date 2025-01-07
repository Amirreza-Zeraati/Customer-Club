# Drop a post
# Django Authentication & User Management with Post CRUD

This project showcases a full-featured Django web application with user authentication and a CRUD (Create, Read, Update, Delete) system for posts, inspired by social platforms like Twitter. Users can register, log in, and manage their profiles, as well as create and interact with posts.

## Features
- **User Registration & Authentication**: Secure account creation and login.
- **Profile Management**: Update and manage user details.
- **Post System**: Users can create, edit, delete, and view posts.
- **Feed**: Displays posts in a chronological order, similar to a social media feed.

## Requirements
- Python 3.12.0
- Django 5.0

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Amirreza-Zeraati/drop-a-post.git
   cd drop-a-post
   ```
2. Create a .env file in the root directory with the following format:
   ```env
   POSTGRES_DB=dropapost
   POSTGRES_USER=postgres
   POSTGRES_PASSWORD=postgres
   POSTGRES_HOST=db
   POSTGRES_PORT=5432

   ```
3. Build and start the containers
   for v1 :
   ```bash
   docker-compose -f docker-compose.db.yml up --build -d
   docker-compose -f docker-compose.app.yml up --build -d
   ```
   for v2 :
   ```bash
   docker compose -f docker-compose.db.yml up --build -d
   docker compose -f docker-compose.app.yml up --build -d
   ```
4. Now you can access the application:
   http://localhost:8000

## Usage
- Create a superuser to access the admin side.
- Register or log in to access the post features.
- Create new posts, view all posts in the feed, and manage your own posts with options to edit or delete.
