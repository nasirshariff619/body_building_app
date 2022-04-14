# Body Building Application
 
## Contents

*   [Brief](#brief-a-name"brief"a)


## Brief <a name="Brief"></a>

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



### CI Pipeline

![ci pipeline](https://user-images.githubusercontent.com/101716216/163386172-9e676c16-1dc0-4cc5-9840-aebdbb1aa0fc.jpg)

The image above displays the continuous integration (CI) pipeline. The CI pipeline is a vital part of the project. It maintains a single source code repositry to work from to keep everything organised. It possesses a master/main branch which is always ready to deploy and feature branches where developments can be made. Build process and testing are all automated. The CI pipeline also keeps team members informed of every update on the version control system. Overall the CI pipeline encourages smaller and more frequent deployments of code to aid the improvement of a software.

With the body building app in particular, once the source code has been pushed to the version control system and the project tracking has been maintained, the CI server uses a webhook to pull the changes and run automated tests on the updated application. Once the test phase has been passes successfully, the application is deployed onto a live environment

### Feature Branch Model

As learnt in training, when working on a software project, it is good practise to implement the feature branch model. This meant that work carried out on the project was done on a development branch, which meant that the code was tested and deployed from this branch before it was merged into the main branch.

![image](https://user-images.githubusercontent.com/101716216/163400708-0fdc7188-42a9-45b3-a236-273ddb51a88d.png)

## Project Tracking

The overall tracking of the project was carried out on a kanban board website known as Trello.

An epic was created which displayed user stories and converted them into tasks for the project. A screenshot of the epic board can be seen below.

![image](https://user-images.githubusercontent.com/101716216/163407735-f96256a3-d388-4b57-9c4e-c08c3b018448.png)

A separate kanban board was created which tracked the progress of each task throughout the project and processed them through different stages. 

![image](https://user-images.githubusercontent.com/101716216/163407547-21528668-3df2-446a-9d07-a4b59eaaeb9a.png)


## Risk Assessment

The image below shows a quick screenshot of the risk assessment, which was used to assess and analyse the risks that could arise from this project. Here is a link to the full risk assessment:
https://docs.google.com/spreadsheets/d/1JIp9C9an2-_RyMoEPWRPlTL4jtTo7_CW/edit?usp=sharing&ouid=109921713876439168912&rtpof=true&sd=true

![image](https://user-images.githubusercontent.com/101716216/163474349-a0d7020c-7916-4ce0-a310-8a62a19a4e82.png)

## Testing

Unit testing was carried out on the CRUD application. This was done using pytest and pytest coverage and shown by the output below:

![image](https://user-images.githubusercontent.com/101716216/163479685-7eb1c897-5c46-4c9f-a58c-d504c8b623ec.png)

The python files that were successfully tested and had a coverage of 100% were the __  init  __.py, forms.py and models.py. 

Unfortunately, only 35% coverage of the routes.py file was achieved and only 4 tests were passed. These tests included the app creation, set up and teardown. Another two successful tests were the apps ability to view the new workout page and delete a workout. I made many attempts to increase both the number of tests and the coverage, however I was unsuccessful. Overall, I was only able to to achieve 60% total coverage.

Looking forward, due to the fact this was an topic I was not confident in and not succesful in, I aim to increase my knowledge on unit testing so that, in the future I can achieve 100% pytest coverage.

## Front-End Design

## Known Issues

## Future improvements

## Acknowledgements 

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
