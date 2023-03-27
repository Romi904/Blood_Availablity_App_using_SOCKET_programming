## Blood Availability App:

This is a distributed client-server application that helps patients in finding blood banks in their area that have the required blood type. The application has two layers of servers.

In the first layer, there are several servers, each of which is responsible for a specific blood group. These servers connect to three different servers, each of which sends a request to three different blood banks for that particular blood type.

Along with the blood group, the client also sends its location to the server. In the second layer, servers find the blood bank based on the location of the client.

All these servers are operated by a central server, which coordinates the communication between the first and second layer servers.

The application is implemented using the concepts of distributed systems, client-server architecture, and networking. The code is written in a modular and scalable manner, which makes it easy to maintain and extend in the future.

Technologies used: Python, Flask, SQL, and REST APIs.

Contributors: [List of contributors]

## Installation:

Clone the repository
Install the required dependencies using pip
Start the application by running the main.py file
## Usage:

Open the Blood Availability App on your device
Enter the required blood group and location details
Click on the search button to find the blood bank in your area
The application will display the list of blood banks along with their contact details
Choose the blood bank that you want to contact and make a call to them.
License:

This application is licensed under the MIT license. See LICENSE.txt for more details.
