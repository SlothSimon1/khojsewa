# 🚀 KHOJ SEWA - QUICK START

## ⚡ ONE-LINER START
```bash
cd c:\Users\Simon\Desktop\khojne
python manage.py runserver
```

Then open: **http://127.0.0.1:8000/**

---

## 📌 QUICK LINKS & ENDPOINTS

### 🏠 Homepage
- **URL**: http://127.0.0.1:8000/
- **What**: Home page with Google Map of all experts
- **Features**: Register/Login buttons, beautiful split layout

### 👤 User Registration
- **URL**: http://127.0.0.1:8000/register/user/
- **Need**: Name, Email, Phone (97/98-XXXXXXXX), Password
- **Takes you to**: User Dashboard

### 👨‍💼 Expert Registration
- **URL**: http://127.0.0.1:8000/register/expert/
- **Need**: Name, Email, Phone, Expertise, Experience, Location, Password
- **Takes you to**: Expert Dashboard

### 🔐 Login
- **URL**: http://127.0.0.1:8000/login/
- **Need**: Email, Password, Select User/Expert
- **Takes you to**: Appropriate dashboard

### 📊 User Dashboard
- **URL**: http://127.0.0.1:8000/dashboard/
- **Can**: Post requests, view experts on map, rate experts, track requests

### 👨‍💻 Expert Dashboard
- **URL**: http://127.0.0.1:8000/expert/dashboard/
- **Can**: See incoming requests, accept jobs, view colleagues, complete requests

### 📍 Logout
- **URL**: http://127.0.0.1:8000/logout/
- **Does**: Clears session, returns to home

---

## ✅ TESTING CHECKLIST

### 1. Home Page
- [ ] Opens without errors
- [ ] Google Map displays
- [ ] Register/Login buttons visible

### 2. User Registration
```
Name: John Doe
Email: john@example.com
Phone: 9841234567
Password: Test123456
```
- [ ] Registration succeeds
- [ ] Redirects to dashboard

### 3. User Dashboard
- [ ] Map shows experts
- [ ] Can post service request
- [ ] Can view experts
- [ ] Logout works

### 4. Expert Registration
```
Name: Ram Kumar
Email: ram@example.com
Phone: 9741234567
Expertise: Electrician
Experience: 5
Location: Kathmandu
Password: Expert123456
```
- [ ] Registration succeeds
- [ ] Redirects to expert dashboard

### 5. Expert Dashboard
- [ ] Can see incoming requests
- [ ] Can accept requests
- [ ] Can view other experts on map
- [ ] Map shows correct location
- [ ] Logout works

### 6. Service Request Flow
- [ ] User posts request
- [ ] Expert sees request
- [ ] Expert accepts request
- [ ] Expert can complete
- [ ] User can rate expert

---

## 🔑 LOGIN CREDENTIALS (Test Users)

After registering, use email + password to login

**Example Employee:**
- Email: `electrician@khoj.com`
- Password: `Expert123456`

---

## 🗺️ MAP INFORMATION

**Cities with Coordinates:**
- **Kathmandu**: 27.7172°N, 85.3240°E (Capital)
- **Lalitpur**: 27.6408°N, 85.3197°E (South of Kathmandu)
- **Bhaktapur**: 27.6722°N, 85.4288°E (East of Kathmandu)
- **Pokhara**: 28.2096°N, 83.9856°E (Tourism hub)
- **Biratnagar**: 26.4535°N, 87.2705°E (Eastern city)

**Map Features:**
- Click marker = see expert info
- Blue dot = regular expert
- Green dot = you (current user)
- Zoom in/out = use mouse wheel
- Pan = click and drag

---

## 🐛 IF SOMETHING BREAKS

### Issue: Page won't load
```bash
# Stop server (Ctrl+C)
python manage.py check
python manage.py runserver
```

### Issue: Database error
```bash
# Delete old database and remigrate
rm db.sqlite3
python manage.py migrate
# Restart server
```

### Issue: Module not found
```bash
# Reinstall dependencies
pip install -r requirements.txt
```

### Issue: Port already in use
```bash
# Use different port
python manage.py runserver 8001
```

---

## 📋 KEY FEATURES

✅ **User Authentication**: Email + Password  
✅ **Expert Profile**: Specialty, experience, location  
✅ **Service Requests**: Post, accept, complete, rate  
✅ **Google Maps**: See all experts with markers  
✅ **Rating System**: 1-5 stars with comments  
✅ **Phone Validation**: Nepali format only (97/98)  
✅ **Responsive Design**: Works on mobile & desktop  
✅ **Session Management**: Auto-logout on close  

---

## 📞 CONTACT INFO

**For issues:**
1. Check APP_USAGE_GUIDE.md for detailed docs
2. Review error messages carefully
3. Check Django logs in terminal

---

**Happy coding! 🎉**
