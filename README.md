# Project-4 ReadMe

Project-4-Giftshop


ReadMe Sections

Description
 Project - 4: A Flask + React App

The Giftshop app is an online shop for all gift lovers who enjoy treating themselves and their loved ones. It is for all of them who believe that buying a present occasionally or regularly can be a life-changer for some of us and a thoughtful gesture towards people we love and care about. It is a place where each one can share comments, ideas and suggestions about gifts. 







 

Deployment link

https://giftshopapp.netlify.app/






Getting Started/Code Installation


Commands and installation to complete before starting:

Backend:

Install:  pip install pipenv
Install:   pipenv install flask
Install:  pipenv install flask-sqlalchemy
Install: pipenv install psycopg2-binary
Run it: pipenv run flask run
Run : pipenv run python seed.py
Install: pipenv install flask-crypt
Install: pipenv install pyjwt
Frontend
Create Project-4-Frontend
Open Project-4  in my code editor
cd into the root directory
run 'npm i' to install the dependencies
run 'npm run build' to build the JavaScript files in the dist
run 'npm run dev' to run the program
Preview the index.ts in the browser






Timeframe & Working Team (Solo/Pair/Group)


Timeframe: 19 days, but due to being sick at the time, I only had 12 days left to complete it. It was a solo project.





Technologies Used


Python
Python Decorators
React
TypeScript
JSX
Bulma
SASS
SCSS
Flask
SQL
TablePlus
Netlify
Fly.io
Git and GitHub
Excalidraw
Insomnia


Brief
Technical Requirements


Build a full-stack application by making your own backend and your own front-end
Use a Python Flask API using a Flask REST Framework to serve your data from a Postgres database
Consume your API with a separate front-end built with React
Be a complete product which most likely means multiple relationships and CRUD functionality for at least a couple of models
Implement thoughtful user stories/wireframes that are significant enough to help you know which features are core MVP and which you can cut
Have a visually impressive design to kick your portfolio up a notch and have something to wow future clients & employers. ALLOW time for this.
Be deployed online so it's publicly accessible.

Necessary Deliverables
A working app hosted on the internet
A link to your hosted working app in the URL section of your GitHub repo
A git repository hosted on GitHub, with a link to your hosted project, and frequent commits dating back to the very beginning of the project
A readme.md file with:
An embedded screenshot of the app
Explanations of the technologies used
A couple of paragraphs about the general approach you took
Installation instructions for any dependencies
Link to your user stories/wireframes – sketches of major views/interfaces in your application, if applicable
Descriptions of any unsolved problems or major hurdles you had to overcome





Planning

I originally planned to build an online shop with the basket and payment option but because I was sick at that time, I started the project later than originally planned, so decided to build a simpler version with the main tasks which were signup, login and posting. 
I used Excalidraw to help me plan. I tried to keep it simple and functional, but the temptation to add more features was strong enough to make me add them to the plan. 










Build/Code Process

I started by instantiating Flask in app.py. In my controllers I created a decorator route to test: I gave it a dummy name”/hello”.  I created the .env file and added the port to it. These were the first things to do to check whether I had an URL running on a port so I could start coding my project with my real data.  



I imported and instantiated Blueprint with a unique name as shown below.



I created a controller and model folder called gift.py and added a file gift_data.py with some data to begin with. In gift.py controller. 









The rest of the code is making sure I have all the models, controllers and all files needed in the backend, being the place where all data for building a responsive frontend is going to live such as gift.py, user.py, user_gift.py, basket.py and comment.py. Making sure I have established all the relationships based on the models and schema as planned. 



Challenges

Creating many-to-one and many-to-many relationships was the hardest part on the backend. It was difficult to decide on what to call my models as they could clash with each other. 
Another confusion was whether to use backref in relationship or back_populate. It was hard to understand the difference between them. I was referring to the same model twice using backref,  when it should have only been referred to once, and ended up understanding them better during this project.

Wins


My big blockers were making the relationships between the Basket and Customers as it was giving me errors. Fixing them was my biggest win. I definitely can say that if you solve relationships in a project, you have done half of the job.
Another thing I would consider a win during this project was solving the confusion that backref and back_populates gave me.








I had to pay attention to what the relationship would be: is it many-to-one or many-to-many? - have I checked if it's plural or singular? This is something to check when creating relationships in order to fix blockers.
 




Key Learnings/Takeaways

Building a full stack app using Python, Flask and React summarised my learnings on the course and was the big takeaway from the SEI course with the GA.
It was the very first time I applied Python to my projects and reading docs helped me out in many situations, so definitely going back to documentation before and during every project is an important key learning for me. 

This project was an excellent opportunity to learn Python, Python decorators and Flask. I also gained a good approach to SQL, learned to manipulate data and understood TablePlus better during this project. 
Another important thing I learned is making mistakes, challenging my fears, breaking the code and fixing it again in order to understand what I was doing.

To conclude, I would say that practising makes your code better, keep practising!


Bugs

When clicking on the GiftList it takes a long time to upload the GiftsList page and that’s something I have to fix. The project is not finished so the Basket page and Show gift page are not functional because I didn’t have time to build them.

Future Improvements


My future improvements will consist in making a full giftshop app where people can buy and sell gifts online and implementing my stretch goals.

Users can use the basket feature with a payment method form to complete if they want to buy gifts.
Users can delete/take items out of the basket.
Adding the admin signup and more social features for people to be able to reach out to the Giftshop admin. 
Adding more styling features such as fonts and colours.



