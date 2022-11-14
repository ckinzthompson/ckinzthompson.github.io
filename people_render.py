top = r'''
<html>
	<head>
		<title>People - Kinz-Thompson Lab</title>
		<meta charset="UTF-8"/>

		<!-- bootswatch version - Lux stylesheet -->
		<link href="https://stackpath.bootstrapcdn.com/bootswatch/4.4.1/lux/bootstrap.min.css" rel="stylesheet" integrity="sha384-oOs/gFavzADqv3i5nCM+9CzXe3e5vXLXZ5LZ7PplpsWpTCufB7kqkTlC9FtZ5nJo" crossorigin="anonymous">

		<link href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet" integrity="sha384-wvfXpqpZZVQGK6TAh5PVlGOfQNHSoD2xbE+QkPxCAFlNEevoEH3Sl0sibVcOQVnN" crossorigin="anonymous">

		<link rel="stylesheet" type="text/css" href="css/main.css">
		<meta name="viewport" content="width=device-width, initial-scale=1">
	</head>

	<body>
		<main class="main">
			<!-- header -->
			<script src="js/header.js"></script>

<!-- People ---------------------------------------->
			<section class="jumbotron text-center" id="people">
				<div class="container">
					<h1>People</h1>
				</div>
			</section>

			<div class="row featurette mx-1 px-1">
				<div class="col-md-7 order-md-2">
					<h2 class="featurette-heading"> Our group </h2>
					<p>Are you interested in doing cutting-edge, interdisciplinary science? </p><br>
					<p>We're looking for undergraduate students, graduate students, and post-docs to join the team! If you are in chemistry, biology, physics, computer science, engineering or other areas -- we've got a place for you! Send your C.V. and an explanation of your interests to Colin.</p><br>
					<p> Join us in the <a href="https://sasn.rutgers.edu/academics-admissions/academic-departments/chemistry">Department of Chemistry at Rutgers University-Newark</a>. Learn more about the <a href="https://sasn.rutgers.edu/academics-admissions/academic-departments/chemistry/ms-phd-chemistry">our Ph.D. program in chemistry here</a>.</p>
				</div>
				<div class="col-md-5 order-md-1">
					<img src="img/ppl/ktgroup_nov2022.jpg" class="img-fluid mx-auto featurette-image">
				</div>
			</div>

			<section class="jumbotron text-center" id="past">
				<div class='container'>
					<h1>Current Members</h1>
				</div>
			</section>
			<div class="album py-5 bg-light">
				<div class="container">
					<div class="row">
'''


def render_person(p):
	x = p.findall('name')
	name = x[0].text if len(x) > 0 else ''
	x = p.findall('role')
	role = x[0].text if len(x) > 0 else ''
	x = p.findall('imgsrc')
	imgsrc = x[0].text if len(x) > 0 else ''
	items = p.findall('items')
	istr = ''
	if len(items) > 0:
		items = items[0]
		for item in items:
			if 'fa' in item.attrib:
				istr += '\t\t\t\t\t\t\t\t\t<i class=\"fa %s\"></i>%s <br>\n'%(item.attrib['fa'],item.text)
		istr=istr[:-5]

	s = r'''
						<div class="col-md-4">
							<div class="card mb-4 shadow-sm peoplecard">
								<div class="peoplecard-img d-flex">
									<img class="bd-placeholder-img headshot" src="%s"></img>
								</div>
								<div class="peoplecard-body card-text">
									<h5 style="text-align: center;">%s</h5>
									<p style="text-align: center; ">%s</p>
%s
								</div>
							</div>
						</div>
'''%(imgsrc,name,role,istr)

	return s

mid = r'''
					</div>
				</div>
			</div>
			<section class="jumbotron text-center" id="past">
				<div class='container'>
					<h1>Previous Members</h1>
				</div>
			</section>
			<div class="album py-5 bg-light">
				<div class="container">
					<div class="row">
'''

bottom = r'''
					</div>
				</div>
			</div>
		</main>
	<script src="js/footer.js"></script>
	</body>

	<!-- make sure jquery comes before bootstrap js... -->
	<script src="https://code.jquery.com/jquery-3.4.1.min.js" integrity="sha256-CSXorXvZcTkaix6Yvo6HppcZGetbYMGWSFlBw8HfCJo=" crossorigin="anonymous"></script>
	<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js"></script>
	<script src="js/main.js"></script>


</html>
'''



if __name__ == '__main__':
	import xml.etree.ElementTree as et
	root = et.parse('people.xml').getroot()

	with open('./people.html','w') as f:
		f.write(top)
		for cp in root.findall('current_person'):
			f.write(render_person(cp))
		f.write(mid)
		for cp in root.findall('past_person'):
			f.write(render_person(cp))
		f.write(bottom)
