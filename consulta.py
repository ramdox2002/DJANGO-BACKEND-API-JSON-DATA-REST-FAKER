import requests

url = "http://localhost:8000/api/v0/analitycs/view-create"

data = {
    'ip': "192.168.1.1",
    'country_of_origin': "United States",
    'browser_language': "en-US",
    'device_type': "Desktop",
    'operating_system': "Windows 10",
    'screen_resolution': "1920x1080",
    'time_on_site': "00:15:30",
    'actions_taken': "Clicked on homepage, viewed product page"
}

response = requests.post(url, data=data)
