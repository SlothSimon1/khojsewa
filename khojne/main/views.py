"""
Views for Khoj Sewa application.
Handles login, service search, request management, and expert dashboard.
"""
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.sessions.models import Session
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from django.conf import settings
from .models import CustomUser, Service, ServiceRequest, Rating, validate_nepali_phone


def register_user(request):
    """
    Handle user registration.
    Regular users who need services.
    """
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        phone = request.POST.get('phone', '').strip()
        password = request.POST.get('password', '').strip()
        confirm_password = request.POST.get('confirm_password', '').strip()
        
        if not all([name, email, phone, password, confirm_password]):
            context = {'error': 'All fields are required', 'role': 'user'}
            return render(request, 'register.html', context)
        
        # Validate phone number (Nepali format)
        if not validate_nepali_phone(phone):
            context = {'error': 'Phone must be a valid Nepali number (97/98 + 8 digits)', 'role': 'user'}
            return render(request, 'register.html', context)
        
        # Check password match
        if password != confirm_password:
            context = {'error': 'Passwords do not match', 'role': 'user'}
            return render(request, 'register.html', context)
        
        # Check password length
        if len(password) < 6:
            context = {'error': 'Password must be at least 6 characters', 'role': 'user'}
            return render(request, 'register.html', context)
        
        # Check if user already exists
        if CustomUser.objects.filter(email=email).exists():
            context = {'error': 'Email already registered', 'role': 'user'}
            return render(request, 'register.html', context)
        
        # Create new user
        user = CustomUser.objects.create(
            name=name,
            email=email,
            phone=phone,
            role='user'
        )
        user.set_password(password)
        user.save()
        
        # Log them in
        request.session['user_id'] = user.id
        request.session['user_email'] = email
        request.session['user_role'] = 'user'
        
        return redirect('dashboard')
    
    context = {'role': 'user'}
    return render(request, 'register.html', context)


def register_expert(request):
    """
    Handle expert registration.
    Experts who provide services.
    """
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        phone = request.POST.get('phone', '').strip()
        expertise = request.POST.get('expertise', '').strip()
        years_experience = request.POST.get('years_experience', '').strip()
        location = request.POST.get('location', '').strip()
        password = request.POST.get('password', '').strip()
        confirm_password = request.POST.get('confirm_password', '').strip()
        
        context = {
            'role': 'expert',
            'locations': ServiceRequest.LOCATIONS,
            'services': ServiceRequest.SERVICE_TYPES
        }
        
        if not all([name, email, phone, expertise, years_experience, location, password, confirm_password]):
            context['error'] = 'All fields are required'
            return render(request, 'register.html', context)
        
        # Validate phone number (Nepali format)
        if not validate_nepali_phone(phone):
            context['error'] = 'Phone must be a valid Nepali number (97/98 + 8 digits)'
            return render(request, 'register.html', context)
        
        # Check password match
        if password != confirm_password:
            context['error'] = 'Passwords do not match'
            return render(request, 'register.html', context)
        
        # Check password length
        if len(password) < 6:
            context['error'] = 'Password must be at least 6 characters'
            return render(request, 'register.html', context)
        
        # Check if user already exists
        if CustomUser.objects.filter(email=email).exists():
            context['error'] = 'Email already registered'
            return render(request, 'register.html', context)
        
        try:
            years = int(years_experience)
        except ValueError:
            context['error'] = 'Years of experience must be a number'
            return render(request, 'register.html', context)
        
        # Create new expert
        user = CustomUser.objects.create(
            name=name,
            email=email,
            phone=phone,
            role='expert',
            expertise=expertise,
            years_experience=years,
            location=location
        )
        user.set_password(password)
        user.save()
        
        # Log them in
        request.session['user_id'] = user.id
        request.session['user_email'] = email
        request.session['user_role'] = 'expert'
        
        return redirect('expert_dashboard')
    
    context = {
        'role': 'expert',
        'locations': ServiceRequest.LOCATIONS,
        'services': ServiceRequest.SERVICE_TYPES
    }
    return render(request, 'register.html', context)


def login_view(request):
    """
    Handle login for both users and experts.
    """
    if request.method == 'POST':
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '').strip()
        role = request.POST.get('role', 'user').strip()
        
        if not email or not password:
            context = {'error': 'Email and password are required', 'role': role}
            return render(request, 'login.html', context)
        
        # Find user by email
        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            context = {'error': 'User not found. Please register first.', 'role': role}
            return render(request, 'login.html', context)
        
        # Check if role matches
        if user.role != role:
            context = {'error': f'This email is registered as {user.role}, not {role}', 'role': role}
            return render(request, 'login.html', context)
        
        # Check password
        if not user.check_password(password):
            context = {'error': 'Invalid password', 'role': role}
            return render(request, 'login.html', context)
        
        # Log them in
        request.session['user_id'] = user.id
        request.session['user_email'] = email
        request.session['user_role'] = role
        request.session['user_name'] = user.name
        
        if role == 'expert':
            return redirect('expert_dashboard')
        else:
            return redirect('dashboard')
    
    # If already logged in, redirect to appropriate dashboard
    if 'user_id' in request.session:
        role = request.session.get('user_role', 'user')
        if role == 'expert':
            return redirect('expert_dashboard')
        else:
            return redirect('dashboard')
    
    context = {'role': 'user'}
    return render(request, 'login.html', context)


def logout_view(request):
    """
    Handle user logout.
    """
    request.session.flush()
    return redirect('home')


def home(request):
    """
    Home page with options to register or login.
    """
    import json
    
    if 'user_id' in request.session:
        role = request.session.get('user_role', 'user')
        if role == 'expert':
            return redirect('expert_dashboard')
        else:
            return redirect('dashboard')
    
    # Get all experts for map display
    experts = CustomUser.objects.filter(role='expert')
    
    location_coords = {
        'Kathmandu': {'lat': 27.7172, 'lng': 85.3240},
        'Lalitpur': {'lat': 27.6408, 'lng': 85.3197},
        'Bhaktapur': {'lat': 27.6722, 'lng': 85.4288},
        'Pokhara': {'lat': 28.2096, 'lng': 83.9856},
        'Biratnagar': {'lat': 26.4535, 'lng': 87.2705},
    }
    
    experts_data = []
    for expert in experts:
        loc = location_coords.get(expert.location, {'lat': 28.3949, 'lng': 84.1240})
        experts_data.append({
            'id': expert.id,
            'name': expert.name,
            'expertise': expert.expertise,
            'location': expert.location,
            'phone': expert.phone,
            'lat': loc['lat'],
            'lng': loc['lng'],
            'years_experience': expert.years_experience,
        })
    
    context = {
        'experts_json': json.dumps(experts_data) if experts_data else '[]',
        'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY,
    }
    return render(request, 'home.html', context)


def dashboard(request):
    """
    Main user dashboard.
    Shows available requests and allows creating new ones.
    """
    import json
    
    # Check if user is logged in
    if 'user_id' not in request.session:
        return redirect('home')
    
    user_id = request.session.get('user_id')
    user = get_object_or_404(CustomUser, id=user_id)
    
    # Only allow regular users
    if user.role != 'user':
        return redirect('home')
    
    # Get all available experts
    experts = CustomUser.objects.filter(role='expert')
    
    # Get user's service requests
    user_requests = ServiceRequest.objects.filter(user=user)
    
    # Get available requests (pending only)
    available_requests = ServiceRequest.objects.filter(status='Pending').exclude(user=user)
    
    # Prepare expert data for Google Maps
    experts_data = []
    location_coords = {
        'Kathmandu': {'lat': 27.7172, 'lng': 85.3240},
        'Lalitpur': {'lat': 27.6408, 'lng': 85.3197},
        'Bhaktapur': {'lat': 27.6722, 'lng': 85.4288},
        'Pokhara': {'lat': 28.2096, 'lng': 83.9856},
        'Biratnagar': {'lat': 26.4535, 'lng': 87.2705},
    }
    
    for expert in experts:
        loc = location_coords.get(expert.location, {'lat': 28.3949, 'lng': 84.1240})
        experts_data.append({
            'id': expert.id,
            'name': expert.name,
            'expertise': expert.expertise,
            'location': expert.location,
            'phone': expert.phone,
            'lat': loc['lat'],
            'lng': loc['lng'],
            'years_experience': expert.years_experience,
        })
    
    context = {
        'user': user,
        'experts': experts,
        'experts_json': json.dumps(experts_data),
        'user_requests': user_requests,
        'available_requests': available_requests,
        'service_types': ServiceRequest.SERVICE_TYPES,
        'locations': ServiceRequest.LOCATIONS,
        'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY,
    }
    
    return render(request, 'dashboard.html', context)


def expert_dashboard(request):
    """
    Expert dashboard showing incoming requests and accepted tasks.
    Similar to Yango/InDrive driver dashboard.
    """
    import json
    
    # Check if user is logged in
    if 'user_id' not in request.session:
        return redirect('home')
    
    user_id = request.session.get('user_id')
    expert = get_object_or_404(CustomUser, id=user_id)
    
    # Only allow experts
    if expert.role != 'expert':
        return redirect('home')
    
    # Get requests matching expert's expertise
    incoming_requests = ServiceRequest.objects.filter(
        type=expert.expertise,
        status='Pending'
    ).exclude(user=expert)
    
    # Get accepted requests
    accepted_requests = ServiceRequest.objects.filter(accepted_by=expert)
    
    # Get all experts for map (same specialty)
    other_experts = CustomUser.objects.filter(role='expert', expertise=expert.expertise).exclude(id=expert.id)
    
    # Prepare expert data for Google Maps
    location_coords = {
        'Kathmandu': {'lat': 27.7172, 'lng': 85.3240},
        'Lalitpur': {'lat': 27.6408, 'lng': 85.3197},
        'Bhaktapur': {'lat': 27.6722, 'lng': 85.4288},
        'Pokhara': {'lat': 28.2096, 'lng': 83.9856},
        'Biratnagar': {'lat': 26.4535, 'lng': 87.2705},
    }
    
    experts_data = []
    for other_expert in other_experts:
        loc = location_coords.get(other_expert.location, {'lat': 28.3949, 'lng': 84.1240})
        experts_data.append({
            'id': other_expert.id,
            'name': other_expert.name,
            'expertise': other_expert.expertise,
            'location': other_expert.location,
            'phone': other_expert.phone,
            'lat': loc['lat'],
            'lng': loc['lng'],
            'years_experience': other_expert.years_experience,
        })
    
    # Add current expert
    coord = location_coords.get(expert.location, {'lat': 28.3949, 'lng': 84.1240})
    experts_data.insert(0, {
        'id': expert.id,
        'name': expert.name + ' (You)',
        'expertise': expert.expertise,
        'location': expert.location,
        'phone': expert.phone,
        'lat': coord['lat'],
        'lng': coord['lng'],
        'years_experience': expert.years_experience,
        'is_current': True,
    })
    
    context = {
        'expert': expert,
        'other_experts': other_experts,
        'experts_json': json.dumps(experts_data),
        'incoming_requests': incoming_requests,
        'accepted_requests': accepted_requests,
        'pending_count': incoming_requests.count(),
        'accepted_count': accepted_requests.count(),
        'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY,
    }
    
    return render(request, 'expert_dashboard.html', context)


@require_http_methods(["POST"])
def post_request(request):
    """
    Handle service request submission from user.
    """
    if 'user_id' not in request.session:
        return redirect('home')
    
    user_id = request.session.get('user_id')
    user = get_object_or_404(CustomUser, id=user_id)
    
    if user.role != 'user':
        return redirect('home')
    
    service_type = request.POST.get('type', '').strip()
    location = request.POST.get('location', '').strip()
    problem = request.POST.get('problem', '').strip()
    budget = request.POST.get('budget', '').strip()
    
    # Validate required fields
    if not all([service_type, location, problem]):
        return redirect('dashboard')
    
    # Create service request
    ServiceRequest.objects.create(
        user=user,
        type=service_type,
        location=location,
        problem=problem,
        budget=budget if budget else None,
        status='Pending'
    )
    
    return redirect('dashboard')


@require_http_methods(["POST"])
def accept_request(request, request_id):
    """
    Expert accepts a service request.
    Similar to accepting order in Yango/InDrive.
    """
    if 'user_id' not in request.session:
        return redirect('home')
    
    user_id = request.session.get('user_id')
    expert = get_object_or_404(CustomUser, id=user_id)
    
    if expert.role != 'expert':
        return redirect('home')
    
    service_request = get_object_or_404(ServiceRequest, id=request_id)
    
    # Check if request matches expert's expertise
    if service_request.type != expert.expertise:
        return redirect('expert_dashboard')
    
    # Accept the request
    service_request.accepted_by = expert
    service_request.status = 'Accepted'
    service_request.save()
    
    return redirect('expert_dashboard')


@require_http_methods(["POST"])
def cancel_request(request, request_id):
    """
    User or expert can cancel a request.
    """
    if 'user_id' not in request.session:
        return redirect('home')
    
    user_id = request.session.get('user_id')
    user = get_object_or_404(CustomUser, id=user_id)
    service_request = get_object_or_404(ServiceRequest, id=request_id)
    
    # Only user who created request or assigned expert can cancel
    if service_request.user != user and service_request.accepted_by != user:
        return redirect('home')
    
    service_request.status = 'Cancelled'
    service_request.save()
    
    if user.role == 'expert':
        return redirect('expert_dashboard')
    else:
        return redirect('dashboard')


@require_http_methods(["POST"])
def complete_request(request, request_id):
    """
    Mark request as completed by expert.
    User can then rate the expert.
    """
    if 'user_id' not in request.session:
        return redirect('home')
    
    user_id = request.session.get('user_id')
    user = get_object_or_404(CustomUser, id=user_id)
    service_request = get_object_or_404(ServiceRequest, id=request_id)
    
    # Only assigned expert can complete
    if service_request.accepted_by != user or user.role != 'expert':
        return redirect('home')
    
    service_request.status = 'Completed'
    service_request.save()
    
    return redirect('expert_dashboard')


def rate_expert(request, request_id):
    """
    User rates an expert after service completion (0-5 scale).
    """
    if request.method == 'GET':
        if 'user_id' not in request.session:
            return redirect('home')
        
        user_id = request.session.get('user_id')
        user = get_object_or_404(CustomUser, id=user_id)
        service_request = get_object_or_404(ServiceRequest, id=request_id)
        
        # Only user who made the request can rate
        if service_request.user != user or user.role != 'user':
            return redirect('home')
        
        # Only rate completed requests
        if service_request.status != 'Completed':
            return redirect('dashboard')
        
        context = {
            'service_request': service_request,
            'expert': service_request.accepted_by,
            'rating_choices': Rating.RATING_CHOICES
        }
        return render(request, 'rate_expert.html', context)
    
    elif request.method == 'POST':
        if 'user_id' not in request.session:
            return redirect('home')
        
        user_id = request.session.get('user_id')
        user = get_object_or_404(CustomUser, id=user_id)
        service_request = get_object_or_404(ServiceRequest, id=request_id)
        
        # Only user who made the request can rate
        if service_request.user != user or user.role != 'user':
            return redirect('home')
        
        rating_value = request.POST.get('rating', '').strip()
        comment = request.POST.get('comment', '').strip()
        
        if not rating_value:
            context = {
                'service_request': service_request,
                'expert': service_request.accepted_by,
                'error': 'Please select a rating',
                'rating_choices': Rating.RATING_CHOICES
            }
            return render(request, 'rate_expert.html', context)
        
        try:
            rating_value = int(rating_value)
            if rating_value < 1 or rating_value > 5:
                raise ValueError
        except ValueError:
            context = {
                'service_request': service_request,
                'expert': service_request.accepted_by,
                'error': 'Rating must be between 1 and 5',
                'rating_choices': Rating.RATING_CHOICES
            }
            return render(request, 'rate_expert.html', context)
        
        # Create or update rating
        rating, created = Rating.objects.update_or_create(
            user=user,
            expert=service_request.accepted_by,
            request=service_request,
            defaults={'rating': rating_value, 'comment': comment}
        )
        
        return redirect('dashboard')
