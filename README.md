# Body Building Application
 
## Contents

## Brief
 My overall objective during the completin of this project is to create a CRUD(create, Read, update and delete) application with utilisation of supporting tools, methodologies and technologies that encapsulate all core modules covered during training.

 This enables the trainers to assess our capabilty of using the technologies and concepts that have been taught to us.

 ### Requirements And Constraints For Minimum Viable Product
 The requirements set out below are what's needed to create a mininum viable product for our project.
 The requirements of the project are as follows:

* A kanban board for the aid of creating and tracking project.
* A relational database, of atleast 2 tables, used to store data persistently for the project. A modelled relationship is also required between these two databases.
* Clear documentation from a design phase describing the architecture used for the project. Along with this a detailed risk assessment.
* A functional CRUD application created in python which meet requirements set out on kanban board.
* Fully designed test suites for the application being created, as well as automated tests for the validation of the application. High test coverage must be provided in the backend. Consistent reports and evidence must be provided to support a TDD(Test Driven Development) approach.
* A functioning front-end website and integrates API's(Application Programming Interface), using Flask.
* Code fully integrated into a Version Control System using the Feature-Branch model which will subsequently be built through a CI(Continuous Integration) server and deployed to a cloud-based virtual machine.



 ### My approach
 Considering all this information, I have decided on creating a bodybuilding app which satisfies all the requirements above. The app will allow the user to do the following:
 
 * Create a post of their workout (satisfies 'Create') which contains the following:
    * The workout muscle group
    * The duration of the workout
*  View all their workouts (satisfies 'Read') and the following:
    * The workout ID
    * The workout muscle group
    * The workout duration 
    * Whether or not the workout is completed (completed:True/False)
*   Update any of their workouts (satisfies 'Update').
*   Delete any of their workouts (satisfies 'Delete').
*  Create a post of their exercises within the workout (satisfies 'Create') which contains the following:
    * Workout ID
    * Exercise name
    * Sets per exercise
    * Reps per set
*  View all of their exercises and see which workouts they belong to (satisfies 'Read').

In the future I would like the user to be able to:
* Create a user account, which allows them to login, that contains the following:
    * Username
    * First name
    * Last name
    * Email 
    * Password
* Update their exercises.
* Delete their exercises.

## Design
### Database Structure
The following image is an entitiy relationship diagram (ERD) which depicts the database structure.

![erd1 (4)](https://user-images.githubusercontent.com/101716216/163208757-c1924820-b62d-42dd-a9d3-ba21d8adb143.jpg)

The ERD models a one and only one to many relationship between the two databases. This means that a workout can have many exercises, however an exercise can only belong to one workout.

If the application was to be developed further, implementing user login, the proposed ERD is as follows.

![erd2](https://user-images.githubusercontent.com/101716216/163207805-0a4a3126-bb4d-48d6-b377-2923d93593cf.jpg)

This ERD builds upon the initial ERD by adding a user database which models a one and only one to many relationship between user and workouts. This means that a user can have many workouts but a workout can only belong to one user.



### CI pipeline
### Stage View???

## Project Tracking
Epic (user stories to tasks)
Trello kanban board

## Risk Assessment

https://docs.google.com/spreadsheets/d/1JIp9C9an2-_RyMoEPWRPlTL4jtTo7_CW/edit?usp=sharing&ouid=109921713876439168912&rtpof=true&sd=true

## Testing

## Front-End Design

## Known Issues

## Future improvements

## Licensing
This app will be licensed with the Apache License 2.0. Under this license, the users are allowed to:

* Use the code commercially.
* Alter the code.
* Distribute ay copies or modifications of the code.
* Sublicense the code.
* Use patent claims.
* Place warranty.

Copyright [yyyy] [name of copyright owner]

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

## Author
Nasir Shariff
