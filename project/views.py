from django.shortcuts import render
import requests
import re
from bs4 import BeautifulSoup 

def home(request):
    return render(request, 'home.html')

#=========  Task 1 ==========

suspecious_pattern = ["failed login", "unauthorized access", "malicious activity detected"]

def get_time(line):
    regex = re.search(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}", line)
    return regex.group(0) if regex else None

def check_log(log_file):
    alerts = []
    try:
        for line in log_file:  # Read file line by line
            line = line.decode("utf-8")  # Convert bytes to string
            for word in suspecious_pattern:
                if word in line.lower():
                    time = get_time(line)
                    if time:
                        alerts.append(f"Alert: {word} attempt detected at {time}")
                    else:
                        alerts.append(f"Alert: {word} attempt detected")
    except Exception as e:
        alerts.append(f"Error: {str(e)}")
    
    return alerts

def scan_log(request):
    messages = []
    if request.method == "POST" and request.FILES.get('log_file'):
        log_file = request.FILES['log_file']
        messages = check_log(log_file)
    
    return render(request, 'task1.html', {'messages': messages})

# ============== Task 2 ==============

missing_headers = ["X-Content-Type-Options", "Strict-Transport-Security"]
vuln_software = ["Apache/2.2.0", "nginx/1.18.0", "Mysql/5.2.0"]

def check_headers(url):
    try:
        response = requests.get(url)
        headers = []
        for header in missing_headers:
            if header not in response.headers:
                headers.append(header)
        return headers
    except Exception as e:
        return [f"Error checking headers: {str(e)}"]

def check_outdated_software(url):
    try:
        response = requests.get(url)
        outdated_software = []
        for software in vuln_software:
            if software.lower() in response.text.lower():
                outdated_software.append(software)
        return outdated_software
    except Exception as e:
        return [f"Error checking software: {str(e)}"]

def check_forms(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        forms_data = soup.find_all('form')
        insecure_forms = []
        for form in forms_data:
            action = form.get('action')
            method = form.get('method')
            if not action or method != "POST":
                insecure_forms.append(action)
        return insecure_forms
    except Exception as e:
        return [f"Error checking forms: {str(e)}"]

def scan_web(request):
    scan_results = None
    if request.method == "POST":
        url = request.POST.get('url')
        if url:
            missing_header = check_headers(url)
            outdated_software = check_outdated_software(url)
            insecure_forms = check_forms(url)
            
            scan_results = {
                "url": url,
                "missing_headers": missing_header,
                "outdated_software": outdated_software,
                "insecure_forms": insecure_forms,
            }
    
    return render(request, 'task2.html', {"scan_results": scan_results})