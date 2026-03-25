# Khoj Sewa - Setup & Usage Guide

## 🚀 Getting Started

Your Khoj Sewa application is now set up and running smoothly! Follow this guide to use all features.

---

## 📋 Application Overview

**Khoj Sewa** is a local service matching platform for Nepal where:
- **Users** can request services from verified experts
- **Experts** can accept service requests and build their reputation
- Both can rate and review each other

---

## 🔧 System Requirements

- Python 3.12+
- Django 4.2
- SQLite3 (included with Python)
- Modern web browser

---

## 📁 Project Structure

```
khojne/
├── manage.py           # Django management script
├── db.sqlite3         # Database file
├── requirements.txt   # Python dependencies
├── config/            # Project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── main/              # Main app
│   ├── models.py      # Database models
│   ├── views.py       # View logic
│   ├── urls.py        # URL routing
│   ├── admin.py
│   └── migrations/
└── templates/         # HTML templates
    ├── home.html
    ├── login.html
    ├── register.html
    ├── dashboard.html
    ├── expert_dashboard.html
    ├── rate_expert.html
    └── maps_widget.html
```

---

## 🗄️ Database Models

### CustomUser
- **name**: Full name
- **email**: Unique email (login credential)
- **phone**: Nepali format (97/98 + 8 digits)
- **password**: Hashed password
- **role**: 'user' or 'expert'
- **expertise**: Service type (for experts)
- **years_experience**: Experience count (for experts)
- **location**: Working area (Kathmandu, Pokhara, etc.)

### ServiceRequest
- **user**: Who posted the request
- **accepted_by**: Expert who accepted
- **type**: Service type
- **location**: Service location
- **problem**: Description of what's needed
- **budget**: Optional budget (Rs.)
- **status**: Pending/Accepted/Completed/Cancelled

### Rating
- **user**: Who gave the rating (must be user)
- **expert**: Who received the rating
- **rating**: 1-5 stars
- **comment**: Optional feedback
- **request**: Associated service request

---

## 👤 User Workflows

### 1. **User Registration**
```
1. Click "Register as User" on home page
2. Enter: Name, Email, Phone (97/98-xxxxxxxx), Password (6+ chars)
3. Click "Register as User"
4. Automatically logged into dashboard
```

### 2. **Expert Registration**
```
1. Click "Register as Expert" on home page
2. Enter: Name, Email, Phone, Expertise, Years, Location, Password
3. Select expertise: Tutor, Electrician, Plumber
4. Choose location: Kathmandu, Lalitpur, Bhaktapur, Pokhara, Biratnagar
5. Click "Register as Expert"
6. Automatically logged into expert dashboard
```

### 3. **User Login**
```
1. Click "Login" on home page
2. Select "User" tab
3. Enter email and password
4. Click "Login as User"
5. Redirected to user dashboard
```

### 4. **Expert Login**
```
1. Click "Login" on home page
2. Select "Expert" tab
3. Enter email and password
4. Click "Login as Expert"
5. Redirected to expert dashboard
```

### 5. **User Dashboard Features**
- **POST SERVICE REQUEST**: Fill form with service type, location, description, optional budget
- **VIEW EXPERTS**: See available experts on interactive Google Map
- **MY REQUESTS**: Track your posted requests and their status
- **RATE EXPERT**: After service completion, rate expert (1-5 stars) and leave feedback
- **LOGOUT**: Click logout button to exit safely

### 6. **Expert Dashboard Features**
- **INCOMING REQUESTS**: See requests matching your expertise
- **ACCEPT REQUEST**: Accept jobs you want to take
- **ACTIVE JOBS**: Track accepted requests
- **COMPLETE REQUEST**: Mark job as done when finished
- **VIEW COLLEAGUES**: See other experts in your field on Google Map
- **LOGOUT**: Exit the system

---

## 🗺️ Google Maps Features

Maps are displayed on:
- **Home Page**: Split layout showing all available experts in Nepal
- **User Dashboard**: View all experts with their locations
- **Expert Dashboard**: Complete view of other experts in your specialty

**How to use:**
- Click on any expert marker to see their details
- View: Name, Expertise, Years of Experience, Location, Phone
- Color coding: Blue = Other experts, Green = Current user
- Mobile responsive - works on all devices

---

## 🔐 Security Features

✓ Password hashing with Django's security tools  
✓ Session management (auto-logout on browser close)  
✓ Phone number validation (Nepali format only)  
✓ Email uniqueness enforcement  
✓ Role-based access control (User vs Expert)  
✓ CSRF protection on all forms  

---

## 📱 Phone Number Format

**Valid Examples:**
- 9841234567 (Starts with 98)
- 9741234567 (Starts with 97)

**Format:** 10 digits total, must start with 97 or 98 (Nepal mobile carriers)

---

## 📊 Service Types & Locations

**Service Types:**
- Tutor (Education)
- Electrician (Electrical work)
- Plumber (Plumbing work)

**Locations:**
- Kathmandu (27.7172°N, 85.3240°E)
- Lalitpur (27.6408°N, 85.3197°E)
- Bhaktapur (27.6722°N, 85.4288°E)
- Pokhara (28.2096°N, 83.9856°E)
- Biratnagar (26.4535°N, 87.2705°E)

---

## 💾 Database Management

### Create superuser (admin):
```bash
python manage.py createsuperuser
# Follow prompts, then access /admin/ in browser
```

### Make migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

### Reset database:
```bash
# Delete db.sqlite3 file, then:
python manage.py migrate
```

### Backup database:
```bash
# Copy db.sqlite3 to safe location
# Or use: python manage.py dumpdata > backup.json
```

---

## 🖥️ Server Management

### Start server:
```bash
python manage.py runserver
# Or with custom port:
python manage.py runserver 0.0.0.0:8000
```

### Stop server:
```
Press Ctrl+C in terminal
```

### Development vs Production:
- **Development**: Default settings, DEBUG=True, SQLite
- **Production**: Change DEBUG=False in settings.py, use PostgreSQL, set ALLOWED_HOSTS

---

## 🧪 Testing the App

1. **Home Page**: http://127.0.0.1:8000/
   - View Google Map with expert locations
   - Click register/login buttons

2. **Register User**: http://127.0.0.1:8000/register/user/
   - Test with valid Nepali phone

3. **Register Expert**: http://127.0.0.1:8000/register/expert/
   - Test with different expertise and location

4. **Login**: http://127.0.0.1:8000/login/
   - Test user and expert login

5. **User Dashboard**: http://127.0.0.1:8000/dashboard/
   - Post service request
   - View experts on map
   - Rate experts

6. **Expert Dashboard**: http://127.0.0.1:8000/expert/dashboard/
   - View incoming requests
   - Accept requests
   - See colleague experts on map

---

## 🐛 Troubleshooting

### Issue: "No modules named 'main'"
```bash
# Solution: Ensure you're running from project root
cd c:\Users\Simon\Desktop\khojne
python manage.py runserver
```

### Issue: "Failed to load Google Maps"
```
# Solution: Check internet connection
# Maps require active internet to load
# Markers will still work with cached data
```

### Issue: "Database locked" error
```bash
# Solution: Delete db.sqlite3 and remigrate
python manage.py migrate
```

### Issue: "Port 8000 already in use"
```bash
# Solution: Use different port
python manage.py runserver 8001
```

---

## 📚 API Endpoints

| URL | Method | Purpose |
|-----|--------|---------|
| `/` | GET | Home page with map |
| `/login/` | GET/POST | Login page |
| `/logout/` | GET | Logout and clear session |
| `/register/user/` | GET/POST | User registration |
| `/register/expert/` | GET/POST | Expert registration |
| `/dashboard/` | GET | User dashboard |
| `/expert/dashboard/` | GET | Expert dashboard |
| `/request/post/` | POST | Create service request |
| `/request/<id>/accept/` | POST | Accept request (expert) |
| `/request/<id>/complete/` | POST | Complete request (expert) |
| `/request/<id>/rate/` | GET/POST | Rate expert (user) |
| `/request/<id>/cancel/` | POST | Cancel request |

---

## 📝 Session Management

- Sessions stored in database
- Auto-logout after browser close
- Session timeout configurable in settings.py
- User ID stored in session (not database login)

---

## 🎨 Frontend Technologies

- **HTML5**: Semantic markup
- **CSS3**: Responsive design with flexbox/grid
- **JavaScript**: Google Maps integration
- **Tailwind CSS**: Already loaded (optional enhancement)

---

## 🚀 Performance Tips

1. **Enable DEBUG=False in production**
2. **Use PostgreSQL instead of SQLite**
3. **Add caching with Redis**
4. **Serve static files with CDN**
5. **Use HTTPS in production**
6. **Optimize database queries with select_related/prefetch_related**

---

## 📞 Features Summary

✅ User & Expert authentication with passwords  
✅ Service request management  
✅ Expert-user matching by specialty  
✅ Real-time status updates  
✅ Google Maps with expert locations  
✅ 5-star rating system  
✅ Nepali phone number validation  
✅ Responsive mobile design  
✅ Session security  
✅ Request lifecycle (Pending → Accepted → Completed)  

---

## 🔄 Next Steps

1. **Customize**: Edit templates, colors, and copy
2. **Test**: Create accounts and test workflows
3. **Deploy**: Use Heroku, AWS, or DigitalOcean
4. **Enhance**: Add SMS notifications, payments, more service types
5. **Monitor**: Track usage, get user feedback

---

**Your app is ready to go! 🎉**

For questions or issues, refer to Django documentation: https://docs.djangoproject.com/
