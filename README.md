
# Folio — Blog Website

Folio is a blog website built with Python and Django. It allows visitors to explore blog posts, browse categories, view writers, and read comments.

## Features

- Browse blog posts and read full articles.
- Explore different blog categories.
- View registered users.
- Read comments associated with blog posts.
- Responsive, clean interface inspired by Medium.
- Sample database containing 10 records for each model.

## Technologies Used

- Python
- Django
- HTML5
- CSS3
- SQLite

## Database Models

The project includes four models:

- **User:** Stores user information.
- **Category:** Organizes blog posts by topic.
- **Post:** Stores blog articles and their categories.
- **Comment:** Stores comments associated with users and posts.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Raghad795/folio-blog.git
   ```

2. Navigate to the project folder containing `manage.py`.

3. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment on Windows:

   ```bash
   venv\Scripts\activate
   ```

5. Install Django:

   ```bash
   pip install "Django>=5.2,<5.3"
   ```

6. Run the development server:

   ```bash
   python manage.py runserver
   ```

7. Open:

   http://127.0.0.1:8000/

## Project Pages

- Home
- Stories
- Story Details
- Topics
- Writers
- Comments

## Sample Data

The repository includes a SQLite database containing sample users, categories, posts, and comments for demonstration purposes.

## Project Purpose

This project was developed to practice Django fundamentals, database modeling, relationships, views, templates, and static files.
