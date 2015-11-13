from django.shortcuts import render, redirect




def index(request):
	return render(request, 'index.html')

def on_demand(request):
	practice_areas = [
		"Antitrust",
		"Banking",
		"Bankruptcy",
		"Business/Corporate Law",
		"Commercial Law/UCC",
		"Criminal Law",
		"Elder Law",
		"Elimination of Bias",
		"Employee Benefits",
		"Employment/Labor Law",
		"Energy",
		"Environment Law",
		"Estate Planning",
		"Ethics",
		"Family Law",
		"Financial Crises",
		"General Practice",
		"Government Affairs",
		"Health Law",
		"Healthcare Reform",
		"Immigration",
		"Insurance",
		"Intellectual Property",
		"Internation Practice",
	]

	states = [
		"Alabama (AL)",
		"Alaska (AK)",
		"California (CA)",
		"Colorada (CO)",
		"Delaware (DE)",
		"Florida (FL)",
		"General (GN)",
		"Georgia (GA)",
		"Hawaii (HI)",
		"Idaho (ID)",
		"Illinois (IL)",
		"Indiana (IN)",
		"Iowa (IA)",
		"Kansas (KS)",
		"Kentucky (KY)",
		"Louisiana (LA)",
		"Maine (ME)",
		"Mississippi(MS)",
		"Missouri (MO)",
		"Montana (MT)",
		"Nebraska (NE)",
		"Nevada (NV)",
		"New Hampshire (NH)",
		"New Jersey (NJ)",
		"New Mexica (NM)",
		"New York (NY)",
		"North Carolina",
		"North Dakota (ND)",
		"Ohio (OH)",
		"Oklahoma (OK)",
		"Oregon (OR)",
		"Pennsylvania (PA)",
		"Puerto Rico (PR)",
		"Rhode Island (RI)",
		"South Carolina (SC)",
		"Tennessee (TN)",
		"Texas (TX)",
		"Utah (UT)",
		"Vermont (VT)",
		"Virgin Islands (VI)",
		"Virginia (VA)",
		"Washington (WA)",
		"West Virginia (WV)",
		"Wisconsin (WI)",
		"Wyoming",
	]
	return render(request, "on_demand.html", 
		{"practice_areas": practice_areas,
		"states": states,})

def live_courses(request):
	return render(request, 'live_courses.html')

def publications(request):
	return render(request, "publications.html")

def news(request):
	return render(request, "news.html")

def webcasts(request):
	return render(request, "webcasts.html")