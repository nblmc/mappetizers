from csv import DictReader
from shapely.geometry import box, mapping
from json import dump

featuresList = []

with open('./data-raw/DC_all-maps-with-bbox_2019-11-01.csv', 'r+') as csvRaw:

	reader = DictReader(csvRaw)

	for row in reader:


		multiEnvelope = row['subject_bbox_geospatial'].split("),")

		bboxCoords = [float(x) for x in multiEnvelope[0][9:-1].split("\\, ")]
		

		geom = box(bboxCoords[0],bboxCoords[3],bboxCoords[1],bboxCoords[2])

		thisRow = {'type': 'Feature', 'geometry': mapping(geom), 'properties': {'id': row['id'], 'title': row['title_info_primary_tsi'], 'year': row['date_start_tsim'], 'time': row['date_start_dtsi']}}

		featuresList.append(thisRow)


outJson = {'type': 'FeatureCollection', 'features': featuresList }


with open('out.geojson', 'w+') as outFile:


	dump(outJson, outFile)

		
