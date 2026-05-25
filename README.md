# Django Photo Album Management System

A production-ready Django photo album application built with:
- Django class-based views (CBVs) for all album and photo CRUD operations
- Role-based access control using Django authentication and groups
- Cloudinary cloud storage for image uploads and media management
- PostgreSQL database support for Render deployment

## Features

- Album listing, detail, create, update, delete
- Photo upload, edit, and delete per album
- RBAC enforcement via `Album Administrator` group and admin/staff users
- Cloudinary-backed media storage in production
- Secure configuration with environment variables only

## Installation

1. Clone the repository.
2. Create a Python environment.
3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Copy `.env.example` to `.env` and configure keys.

5. Run migrations:

```bash
python manage.py migrate
```

6. Create a superuser:

```bash
python manage.py createsuperuser
```

7. Provision the RBAC group:

```bash
python manage.py setup_roles
```

8. Start the development server:

```bash
python manage.py runserver
```

## Deployment

This application is configured for Render. The `render.yaml` manifest defines a Python web service and a PostgreSQL database.

### Render setup

- Add `DJANGO_SECRET_KEY`
- Add `DATABASE_URL`
- Add `CLOUDINARY_CLOUD_NAME`, `CLOUDINARY_API_KEY`, `CLOUDINARY_API_SECRET`
- Set `DJANGO_DEBUG=False`
- Set `DJANGO_ENV=production`

### Start command

```bash
gunicorn photo_album.wsgi:application --bind 0.0.0.0:$PORT
```

## RBAC

- Standard users can browse albums and view photos.
- Only users in the `Album Administrator` group or staff users can create, update, or delete albums and photos.

## File structure

- `photo_album/` — Django project settings and URLs
- `albums/` — main application logic, models, views, forms, templates
- `templates/` — shared templates and auth views
- `render.yaml` — Render service manifest
- `requirements.txt` — Python dependencies

## Testing

Run the app tests with:

```bash
python manage.py test
```

## Notes

- Media files are uploaded to Cloudinary in production via `DEFAULT_FILE_STORAGE`.
- Local media storage is disabled for production.
- PostgreSQL is used via `DATABASE_URL`.
