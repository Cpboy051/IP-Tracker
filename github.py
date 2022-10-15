import json
from urllib import request

url = "https://api.github.com/users/"

name = str(input("Enter name github users: "))

response = request.urlopen(url + name)

data = json.loads(response.read())

print("\nProgram Profile Github".center(40,"="))
print(f"Login: {data['login']}")
print(f"Id: {data['id']}")
print(f"Name: {data['name']}")
print(f"Avatar: {data['avatar_url']}")
print(f"Gravatar: {data['gravatar_id']}")
print(f"Company: {data['company']}")
print(f"Node id : {data['node_id']}")
print(f"Email: {data['email']}")
print(f"SiteAdmin: {data['site_admin']}")
print(f"Bio: {data['bio']}")
print(f"Type: {data['type']}")
print(f"Hireabel: {data['hireable']}")
print(f"Blog: {data['blog']}")
print(f"Twitter: {data['twitter_username']}")
print(f"Repositories: {data['public_repos']}")
print(f"Location: {data['location']}")
print(f"Followers: {data['followers']}")
print(f"Following: {data['following']}")
print(f"Create github: {data['created_at']}")
print(f"Updated github: {data['updated_at']}")
