References for the Gainful project
==================================

Tips and tricks
---------------

-	parsing HTML table with BeautifulSoup:
	-	http://stackoverflow.com/questions/23377533/python-beautifulsoup-parsing-table
-	I think this person did the same thing?
	-	https://charlesleifer.com/blog/saturday-morning-hack-personalized-news-digest-with-boolean-query-parser/
		-	http://huey.readthedocs.org/en/latest/
		-	http://docs.peewee-orm.com/en/latest/

class design for cities
-----------------------

-	class City()
	-	data:
		-	request_url -
		-	soup_find_list[selector name, attrs]
		-	csv_name
	-	methods:
		-	row_parser(primed_csv_lines, table)
-	flow for program:
	-	list of cities
	-	for city in list_of_cities:
	-	parse logic
