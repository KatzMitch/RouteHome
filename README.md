I wrote this simple command line utility to speed up the process of checking the
fastest route home from work for me using the Google Maps Directions API

The install script will have you choose an origin and destination point and
alias the script to be run under the name "routehome". The alias will be set in
the ~/.profile file, be sure that your startup shell script sources from here!
This can be done by adding the line "source ~/.profile" to the ~/.bashrc file
(assuming you are using bash).

Thank you to MassDOT and the City of Boston traffic engineers for necessitating
this utility! Have fun avoiding traffic!

Future updates:
- Add support for tolls (choose whether or not to avoid them)
