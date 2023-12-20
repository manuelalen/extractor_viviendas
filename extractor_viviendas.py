import requests
from bs4 import BeautifulSoup
from datetime import datetime
import csv
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    # Aquí el usuario puede añadir más headers si fuese necesario, pero teniendolo en ejecución durante 8-10 horas al día no he tenido problemas
}

# Reemplaza 'tu_cookie_name' y 'tu_cookie_value' con tus propias cookies
cookies = {
    'tu_cookie_name': 'tu_cookie_value',
    # Agrega más cookies si es necesario
}

def get_properties_data(url, headers, cookies):
    response = requests.get(url, headers=headers, cookies=cookies)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        property_listings = soup.find_all('div', class_='item-info-container')

        properties_data = []
        for listing in property_listings:
            location = listing.find('a', class_='item-link').text.strip()
            price = listing.find('span', class_='item-price').text.strip()
            date_found = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            property_data = {
                'location': location,
                'price': price,
                'date_found': date_found
            }
            properties_data.append(property_data)

            # Introduce un tiempo de espera entre solicitudes para evitar bloqueos
            time.sleep(5)  # ajusta según tu propio caso, pero con esto no he visto problemas y la respuesta, aúne xtrayendo 1.000 registros es relativamente rápido

        return properties_data
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        return None

def save_to_csv(properties, filename='properties.csv'):
    with open(filename, 'a', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['location', 'price', 'date_found']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        for property_data in properties:
            writer.writerow(property_data)

if __name__ == "__main__":
    for page_num in range(2, 60):  # Cambie el rango para que vaya de la página 2 a la 60
        url = f"https://www.idealista.com/alquiler-viviendas/malaga-provincia/pagina-{page_num}.htm"
        properties = get_properties_data(url, headers, cookies)

        if properties:
            for index, property_data in enumerate(properties, start=1):
                print(f"Property {index} from page {page_num}:")
                print(f"Location: {property_data['location']}")
                print(f"Price: {property_data['price']}")
                print(f"Date Found: {property_data['date_found']}")
                print("-" * 30)

            # Guarda los datos en un archivo CSV
            save_to_csv(properties)
            print(f"Data from page {page_num} saved to properties.csv")
        else:
            print(f"No data available on page {page_num}")

        # Introduce un tiempo de espera entre páginas para evitar bloqueos
        time.sleep(5)  # ajusta según sea necesario
