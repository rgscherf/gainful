Gainful
=======

Working toward a customizable daily digest of public service job postings

TODO:
-----

-	data:
	-	figure out date formatting so I know which postings are new
	-	(done!) refactor output lists for HTML templating
-	presentation:
	-	jinja templating to generate HTML
		-	https://realpython.com/blog/python/primer-on-jinja-templating/
		-	http://flask.pocoo.org/docs/0.10/quickstart/
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
		-	metrolinx
		-	TTC
		-	TRCA
	-	Ontario public service
		-	(done!) OPS
		-	Ontario AG
		-	Ontario OIPC
	-	Island municipalities
		-	(done!) victoria
		-	(done!) CRD
		-	saanich
		-	oak bay
		-	view royal
		-	langford
		-	capital regional district
		-	esquimalt
		-	colwood
		-	sidney
		-	sooke
	-	CivicInfo.ca
	-	BC Public Service
		-	Government https://search.employment.gov.bc.ca/cgi-bin/a/searchjobs_quick.cgi?a=search&page=1&search=Search%20Jobs&keywords_or=&region=Greater%20Victoria&order=job_id%20ASC
