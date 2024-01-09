import requests

print('GitHub Users\n')

username = input('What is the username? ')

url = f'https://api.github.com/users/{username}'

response = requests.get(url)
data = response.json()

if response.status_code == 200:
    print(f'\nName: {data["name"]}')
    print(f'Bio: {data["bio"]}')
    print(f'id: {data["id"]}')
    print(f'Location: {data["location"]}')
    print(f'avatar_url: {data["avatar_url"]}')
    print(f'Followers: {data["followers"]}')
    print(f'Following: {data["following"]}')
    print(f'email: {data["email"]}')
    print(f'location: {data["location"]}')
else:
    print('Could not find user!')