# 🗺️ Google Maps API Setup Guide - FREE

## Step 1: Get Your FREE Google Maps API Key (5 minutes)

### Go to Google Cloud Console
1. Open: https://console.cloud.google.com/
2. Click "Create Project" or select existing
3. Name it: "Khoj Sewa" (or anything you want)
4. Click "Create"

### Wait for project creation (~2 minutes)

### Enable Google Maps APIs
1. Search for "Maps JavaScript API" in search box
2. Click it, then click "ENABLE"
3. Wait for it to process

### Create API Key
1. Go to "Credentials" (left sidebar)
2. Click "Create Credentials" 
3. Select "API Key"
4. Copy the key that appears
5. Click "RESTRICT KEY" button

### Restrict Your Key (Important for Security)
1. Under "Application restrictions"
2. Select "HTTP referrers (web sites)"
3. Add: `http://127.0.0.1:8000/*`
4. Click "Save"

### Enable API Usage
1. Under "API restrictions"
2. Select "Maps JavaScript API"
3. Click "Save"

---

## Step 2: Add Your Key to Khoj Sewa

### Method 1: Environment Variable (Recommended)

Create `.env` file in project root:
```
GOOGLE_MAPS_API_KEY=your_api_key_here
```

### Method 2: Direct In Code (Easy for Testing)

Edit `config/settings.py`:
```python
# Add at the end:
GOOGLE_MAPS_API_KEY = "your_api_key_here"
```

---

## Step 3: Verify It Works

1. Start your server: `python manage.py runserver`
2. Go to home page: http://127.0.0.1:8000/
3. You should see Google Map with experts
4. Try scrolling and clicking markers

---

## Free Tier Limits

✅ **Free forever:**
- 25,000 map loads/day
- JavaScript Maps API included
- Markers and info windows

🚫 **Paid (not needed):**
- Advanced visualizations
- Priority support

---

## Troubleshooting

### Maps not showing?
1. Check API key is correct
2. Wait 1-2 minutes for API to activate
3. Refresh browser
4. Check browser console for errors (F12)

### Getting "API key not valid" error?
1. Verify key been enabled for Maps JavaScript API
2. Check HTTP referrer restrictions
3. Try disabling key restriction temporarily

### Key shows in URL (security issue)?
1. Never commit key to Git
2. Always use environment variables
3. Restrict key to your domain

---

## Production Setup

For live website:
```python
GOOGLE_MAPS_API_KEY = os.environ.get('GOOGLE_MAPS_API_KEY')
```

Then add key to hosting platform environment variables (Heroku, AWS, etc)

---

**You're ready! Follow the 3 steps above.** 🚀
