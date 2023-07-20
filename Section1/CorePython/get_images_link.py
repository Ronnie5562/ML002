import requests

def get_image_links(query, num_images):
    api_key = '37100150-d1d7acd4bb70fe6b74374630f'
    url=f'https://pixabay.com/api/?key={api_key}&q={query}&image_type=photo&per_page={num_images}'

    response = requests.get(url)
    data = response.json()

    return [item['webformatURL'] for item in data['hits']]


search_query = 'house exterior'
num_images = 200

links = get_image_links(search_query, num_images)

with open('image_links.txt', 'a') as file:
    file.writelines('"' + link + '",' + '\n' for link in links)