# My Resume Site
The ultimate goal in creating this website is to not only showcase my skills but also advertise myself and my quest to find a software developer postion. The website uses Django for the back-end and Bootstrap for the front-end with some custom CSS here and there.

## Back-end
The back-end side of the website uses Django and SQL to power it. From the Django admin back-end I have added all the necassary admin pages to be able to dynamically update the information on the website making it extremely quick and easy to keep current.

## Front-end
The front-end of the website uses Boostrap as well as a few custom CSS files and Django to give it the appearence that I am going for. While it may seem like a simple Bootstrap site with static HTML for the display of my resume it is actually a lot more complex than that. Every single item on my resume page is pulled directly from a database and rendered out in a pleasing fashion for people to view it. The custom CSS allows me to have total control over exactly how the website is viewed by the end user.

The template for my resume page can be found at: 
`templates > resume > resume.html` and is an extension of `templates > base.html` which means it inherits all of the code from `base.html` and makes use of the blocks contained within `base.html`. 

The view for my resume page can be located in my git repository at `resume > views`. In this file you will find the database queries that are necassary for my site to run properly and be able to display the correct information where it is needed. 

The view for the resume page is in `psite > urls.py` and is called using namespace `v_resume` since that is what it was assigned in the view file.

## Hosting
The website is hosted on a Heroku Dyno that automatically redploys it every time a change is uploaded to this Github Repository which makes it extremely streamlined and automated as far as keeping it up to speed.

In order for this to work I had to use a Procfile that can be found in the base folder and is titled `Procfile`. This file is necassary to use for deploying Django to Heroku because it tells Heroku the specific processes and related information needed to run the app.

There is also an initialization shell script that is run every time that the project is re-deployed on Heroku. This file is located in `bin > heroku_init.sh` and is called in the Procfile so Heroku knows that it needs to run the script as well so it all plays nicely.

## Live Site
[Resume Website](https://prtsite.herokuapp.com/ "Resume Website")