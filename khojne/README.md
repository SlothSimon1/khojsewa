# Khoj Sewa - Smart Local Service Finder (Nepal)

A modern Django web application for finding and requesting local services in Nepal.

## Features

✨ **Core Features:**
- 🔐 **Simulated Login System** - Login with any email (admin@khoj.com for admin access)
- 🔍 **Service Search** - Filter services by type and location
- 📋 **Request Services** - Submit service requests with detailed descriptions
- ✅ **Admin Approval** - Admins can accept and manage service requests
- 📞 **Direct Calling** - One-click calling via phone number links
- 🎨 **Modern UI** - Glassmorphism cards with Tailwind CSS
- 🌍 **Multi-location Support** - Kathmandu, Lalitpur, Bhaktapur, Pokhara, Biratnagar

## Project Structure

```
khojne/
├── config/                 # Django configuration
│   ├── settings.py        # Project settings
│   ├── urls.py            # URL routing
│   └── wsgi.py            # WSGI configuration
├── main/                   # Main application
│   ├── models.py          # Service and ServiceRequest models
│   ├── views.py           # View logic
│   ├── urls.py            # App URLs
│   ├── admin.py           # Django admin config
│   └── migrations/        # Database migrations
├── templates/
│   └── index.html         # Main template with modern UI
├── manage.py              # Django management script
├── populate_db.py         # Script to add sample services
├── requirements.txt       # Python dependencies
├── db.sqlite3            # SQLite database
└── README.md             # This file
```

## Database Models

### Service
- `name` - Service provider name
- `type` - Service type (Tutor, Electrician, Plumber)
- `location` - Service location
- `phone` - Contact phone number
- `created_at` - Creation timestamp

### ServiceRequest
- `name` - Requester name
- `type` - Service type
- `location` - Service location
- `problem` - Problem description
- `status` - Request status (Pending, Accepted)
- `created_at` - Creation timestamp
- `updated_at` - Last update timestamp

## Installation & Setup

### 1. Install Dependencies
```bash
pip install Django==4.2.8
```

### 2. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 3. Populate Sample Data
```bash
python populate_db.py
```

### 4. Start Development Server
```bash
python manage.py runserver
```

The application will be available at: **http://localhost:8000**

## Usage

### 1. Login
- Access the homepage
- Enter your email address
- Special email: `admin@khoj.com` - Creates an admin account
- Any other email - Creates a regular user account

### 2. Browse Services
- View all available services in a grid layout
- Filter by service type and location
- Click "Call" button to dial the service provider

### 3. Request a Service
- Fill in your personal details
- Select service type and location
- Describe your problem
- Submit the request

### 4. Admin Features (admin@khoj.com only)
- View all service requests
- Accept pending requests to mark them as "Accepted"
- Accepted requests are highlighted in green
- No delete functionality - requests persist in system

## API Routes

| URL | Method | Description |
|-----|--------|-------------|
| `/` | GET | Main dashboard (requires login) |
| `/login/` | GET/POST | Login page |
| `/request/` | POST | Submit service request |
| `/accept/<id>/` | POST | Accept service request (admin only) |
| `/logout/` | GET | Logout user |

## UI Features

### Design Elements
- **Gradient Background**: Indigo to purple gradient
- **Glassmorphism Cards**: Frosted glass effect with blur
- **Responsive Layout**: Mobile-first design
- **Hover Animations**: Smooth transitions on interactive elements
- **Status Badges**: Color-coded request status indicators

### Color Scheme
- **Primary**: Indigo (#667eea) to Purple (#764ba2)
- **Success**: Green (#10b981)
- **Warning**: Amber (#f59e0b)
- **Info**: Blue (#3b82f6)

## Session Management

- **Session Storage**: Django database backend
- **Session Duration**: 24 hours
- **Session Data**: Email and user role
- **Auto Logout**: Session expires after 24 hours of inactivity

## Search & Filtering

### Case-Insensitive Search
- Service type filtering works with any case variation
- Location filtering matches exact location names
- Empty filters show all available services
- "No services found" message displays when filters return no results

## Running Commands

### Create Admin User (Optional)
```bash
python manage.py createsuperuser
```

Then access admin panel at: http://localhost:8000/admin

### Database Reset
```bash
# Delete database and migrations
rm db.sqlite3
rm -r main/migrations

# Recreate from scratch
python manage.py makemigrations main
python manage.py migrate
python populate_db.py
```

## Troubleshooting

### Port Already in Use
```bash
python manage.py runserver 8001
```

### Database Errors
```bash
python manage.py migrate --run-syncdb
```

### Import Errors
Ensure Django is installed:
```bash
pip install Django==4.2.8
```

## Development Notes

- **Debug Mode**: Enabled (change `DEBUG=False` in settings.py for production)
- **Secret Key**: Not secure - change before deploying
- **Database**: SQLite (good for development)
- **Static Files**: Configured for development

## Future Enhancements

- Real user authentication with passwords
- Service ratings and reviews
- Real location APIs (Google Maps)
- Email notifications
- Payment integration
- Admin dashboard analytics
- Service categories expansion
- User profiles and history

## Technologies Used

- **Backend**: Django 4.2.8
- **Database**: SQLite3
- **Frontend**: HTML5, Tailwind CSS 3
- **Session**: Django Sessions
- **Python**: 3.12+

## License

Educational project for hackathon (Codefest)

## Author

Created as a modern service discovery platform for Nepal.

---

**Start the server and begin exploring Khoj Sewa!**
