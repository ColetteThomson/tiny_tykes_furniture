# Hotel California Booking System

## Purpose
This command line based hotel booking system was created to enable guests to book and select their hotel requirements online, rather than have to phone the Hotel California.  
This booking system is designed to be run through once, with the guest required to call the hotel should they wish to make any changes to their original online booking.
Guests are prompted to enter their name, room type and meal choices and a total bill is displayed with all the guest's details and expected costs.  

The live project can be found [here](https://colettethomson.github.io/Fultum-Wiltshire-Charity/assets/index.html)

<< insert mockups >>

## Features
* A step-by-step booking process allowing the user to only enter relevant information - thereby minimising user input error.
* Validation of entry implemented for all instances of user input.
* **Hotel Room Types Available** section:  Room type (family / twin bed / double / single) is shown with the cost per person or per night.  The user is also prompted to to enter the number of nights they wish to stay at the hotel.  Their choice is printed to the console (for example:  'Your choice: Double room for 2 nights') as way of confirmation of their entry.
* **Meal/s Options** section: Users can select one or more, or none of the meal/s options (dinner / breakfast / lunch) with the cost per person also shown.  The user is also prompted to to enter the number of people for each meal.  Their choice is printed to the console (for example: 'Your choice: Dinner for 2').
* The **Hotel California Bill** section prints to the console a cost breakdown of the user's inputs.  The reservation is the user's first and last names.  The user's check-in date is displayed.  **Room Cost** is a sum of room type x number of nights.  **Meal/s Cost** is a sum of meal type x number of people.  The **Total Final Bill** is a sum of 'Room Cost' + 'Meal/s Cost'.

## Data Model


## Testing
Manual testing of this project included:
* A run through of the entire system with correct user input to ensure all functionality was working as expected.
Validation testing for entry of invalid input:
* strings instead of numbers
* numbers instead of strings
* combinations of alphabet, special characters and numbers where alphabet letters were expected.
* Attempting to 'ignore' steps in the booking process
* Repeated invalid input 

### Bugs


### Validator Testing
* Python code was run through [PEP8online.com](http://pep8online.com/) with no errors returned.

### Project Creation
The following terminal commands were used during this project:
* git add . - this command adds a change in the working directory to the staging area.
* git commit -m "*message*" - this command details the change/s made in the 'message' section and then commits the changes to the local repository.
* git push - this command is used to push all changes to the GitHub repository.

## Deployment
This project was deployed using Code Institute's mock terminal for Heroku.
Steps for deployment:
* Fork or clone this repository
* Create a new Heroku app
* Set the buildbacks to Python and NodeJS in that order
* Link the Heroku app to the repository
* Click on Deploy

## Technologies
* Python - for all code
* Python library import: datetime
* Google.oauth2.service_account for Credentials
* Code Institute's Heroku terminal
* [Git](https://git-scm.com/) - used as version control software to commit and push code to a GitHub repository where all source code is located.

## Credits and References
* Code Institute for the deployment terminal
* The private collaboration and knowledge sharing SaaS platform [Stack Overflow](https://stackoverflow.com/) was an invaluable resource for general coding queries.
* Code Institute tutor support




