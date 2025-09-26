# Property Management App with LiveComponents

A Django application for managing real estate properties, demonstrating the LiveComponents library.

## What it does

- **Property Grid**: Displays properties in a responsive grid layout
- **Interactive Cards**: Each property card has 3 modes:
  - **Overview**: Image, title, price
  - **Detail**: Complete information (city, creation date, etc.)
  - **Edit**: Inline property editing
- **Live Search**: Filter the grid by typing into the search bar 
- **Create Properties**: Create new listings with the inline create form
- **State Management**: LiveComponents for reactive UI without page reloads

## Tech Stack

- Django 5.2.6
- LiveComponents 
- HTMX 
- Tailwind CSS 
- UV (package manager)

## Setup & Start

### 1. Install dependencies
```bash
uv sync
```

### 2. Run migrations
```bash
python manage.py migrate
```

### 3. Start development server
```bash
python manage.py runserver
```

### 4. Open the app
Go to `http://localhost:8000`
