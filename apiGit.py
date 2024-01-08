import requests

print('GitHub Users\n')

username = input('What is the username? ')

url = f'https://api.github.com/users/{username}'

response = requests.get(url)
data = response.json()

if response.status_code == 200:
    print(f'\nFull name: {data["name"]}')
    print(f'Bio: {data["bio"]}')
    print(f'Location: {data["location"]}')
    print(f'Followers: {data["followers"]}')
    print(f'Following: {data["following"]}')
else:
    print('Could not find user!')