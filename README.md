Gainful
=======

Working toward a customizable daily digest of public service job postings

TODO:
-----

-	data:
	-	figure out date formatting so I know which postings are new
		-	**this will require a persistent data solution of some kind**
	-	(done!) refactor output lists for HTML templating
-	presentation:
	-	(kinda done!) jinja templating to generate HTML
		-	https://realpython.com/blog/python/primer-on-jinja-templating/
		-	http://flask.pocoo.org/docs/0.10/quickstart/
	-	**how to make the table look nice?**
	-	sorting the table/only showing new postings?
	-	can this HTML be turned into email digest?
		-	https://charlesleifer.com/blog/saturday-morning-hack-personalized-news-digest-with-boolean-query-parser/
			-	http://huey.readthedocs.org/en/latest/
			-	http://docs.peewee-orm.com/en/latest/
	-	future -> support for multiple users
		-	some kind of frontend (flask?)
-	sites to parse:
	-	more GTA municipalities
		-	region of peel: https://careers-peelregion.icims.com/jobs/search?hashed=-435774142&mobile=false&width=560&height=500&bga=true&needsRedirect=false&jan1offset=-300&jun1offset=-240
		-	york region: http://clients.njoyn.com/cl2/xweb/xweb.asp?page=joblisting&clid=60295
		-	brampton: https://careers-brampton.icims.com/jobs/search?ss=1&searchKeyword=&searchLocation=&searchCategory=19538&searchRadius=5&searchZip=&mobile=false&width=1141&height=500&bga=true&needsRedirect=false&jan1offset=-300&jun1offset=-240
		-	barrie: http://www.barrie.ca/City%20Hall/Employment/Pages/opportunities.aspx
	-	GTA institutions
		-	UofT
		-	Ryerson
		-	York
	-	GTA agencies
		-	AMO
		-	Metrolinx
		-	TTC
		-	TRCA
	-	Ontario public service
		-	(done!) OPS
	-	Island municipalities
		-	(done!) Victoria
		-	(done!) CRD *(is this covered by civicinfo?)*
	-	(done!) CivicInfo.ca
	-	(done!) BC Public Service
