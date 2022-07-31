import shodan
#If the queries use quote marks wrap that in ''
SHODAN_API_KEY = "1SDmQiIM9Pejrt03gE3VTGVUdNz4eEZG"

api = shodan.Shodan(SHODAN_API_KEY)#Setup API
country = ["US","AR","BO","BR","CL","CO","CR","CU","EC","SV","GT","HN","MX","NI","PA","PY","PE","PR","DO","UY","VE"]#LATAM+US
query = ["port:502","port:161"]
# Wrap the request in a try/ except block to catch errors
#try:
        # Search Shodan
total_results = open("results.txt","w")
for i in country:
    for j in query:
        results = api.search("country:"+i+" "+j)#returns a dictionary 
    # Save the results in a text file
        total_results.write('Results found: {}'.format(results['total']))
        for result in results['matches']:
            total_results.write('IP: {}'.format(result['ip_str']))
            total_results.write(result['data'])
            total_results.write('')
            print("SOMETHING")
#except (shodan.APIError, e):
 #       print('Error: {}'.format(e))