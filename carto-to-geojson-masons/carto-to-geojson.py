import requests
from csv import DictReader
from json import dump

featuresList = []

with open('crosswalks.csv','r+') as crosswalksRaw:

	crosswalks = DictReader(crosswalksRaw)

	for row in crosswalks:

		apiUrl = "https://bpl-maps.carto.com/api/v2/sql?q=select * from {}&format=GeoJSON".format(row['carto_table_name'])

		r = requests.get(apiUrl)

		j = r.json()



		for feature in j['features']:

			featuresList.append({'type': 'Feature', 'geometry': feature['geometry'], 'properties': {'name': feature['properties']['name'], 'folder': row['canonical_folder_name']}})



with open('all-mason.geojson','w+') as outFile:

	dump({'type': 'FeatureCollection', 'features': featuresList}, outFile)