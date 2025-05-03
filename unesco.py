import json

def get_unesco_sites():
    try:
        # Load data from the local JSON file
        with open('unesco_sample.json', 'r') as file:
            data = json.load(file)

        sites = data.get('features', [])
        print(f"✅ Found {len(sites)} sites")
        return [{
            'name': site['properties']['name_en'],
            'country': site['properties']['states_name_en'],
            'category': site['properties']['category_short'],
        } for site in sites[:10]]

    except Exception as e:
        print("❌ Error loading UNESCO sites:", e)
        return []
