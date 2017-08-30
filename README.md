I wrote this simple command line utility to speed up the process of checking the
fastest route home from work for me using the Google Maps Directions API

Feel free to use and modify this- the file apikey.yml.dist is a sample file so
I don't need to post my Google Maps API key publically. Rename the file to
apikey.yml and add your personal API key in the appropriate spot.

Thank you to MassDOT and the City of Boston traffic engineers for necessitating
this utility! Have fun avoiding traffic!

Future updates:
- Add a configuration script to write APIKEY.yml and copy executable to the
user's PATH, and choose default origin and destination
- Add support for tolls (choose whether or not to avoid them)
- Add command line support for different orgin and destination
