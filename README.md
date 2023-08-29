# modern-message-board

![Device Mockup Image]()

## by Tadhg Nolan

[Live Site](https://modernmb-45f157023587.herokuapp.com/)

# Table of Contents
1. [Intro](#intro)
2. [Design](#design)
3. [Technologies](#technologies)
4. [Features](#features)
5. [Testing](#testing)
6. [Deployment](#deployment)
7. [Credits](#credits)


## Intro

 - Modern Message Board It is a modern interpretation of 1990's style message boards & forums with some influence drawn from modern websites/apps like Reddit.  

### Design

#### UX

An Agile methodology was used in planning the project utilising Github's Project kanban.
[Issues](https://github.com/users/tadhgnolan/projects/2/views/1) were used to create user stories. When work began on a user story, it was moved to the "In Progress" column. When the task is complete, it is moved to the "Done" column.
Labels were used to mark priority of issue.
Milestones were used to set major project objectives.
A column named Future Features is used for prospective features for the website and for any features that 
were not complete by the project deadline.

#### UI

**Wireframe Images**

---
![Wireframe Image 1]()

![Wireframe Image 1]()

![Wireframe Image 1]()

---

#### **Entity Relationship Diagram**

---
![ERD Image]()

### User Stories

- Account Registration: As a Site User I can register an account so that I can create posts and view other user posts. [#1](https://github.com/tadhgnolan/modern-message-board/issues/1)
- View List of Posts: As a site user I can view a list of posts so that I can select one to read. [#2](https://github.com/tadhgnolan/modern-message-board/issues/2)
- Open a Post: As a Site User I can click on a post to read the full text. [#3](https://github.com/tadhgnolan/modern-message-board/issues/3)
- Manage My Posts: As a Site User I can create , update and delete my posts so that I can manage my content on the website. [#4](https://github.com/tadhgnolan/modern-message-board/issues/4)
- Category List: As a Site User I can view a list of categories so that I can view posts within. [#5](https://github.com/tadhgnolan/modern-message-board/issues/5)
- (Admin) Manage Posts: As an Admin I can create, read, update and delete posts so that I can manage content on the website. [#6](https://github.com/tadhgnolan/modern-message-board/issues/6)
- (Admin) Categories: As a Site Admin I can create, view, update and delete categories on the website. [#7](https://github.com/tadhgnolan/modern-message-board/issues/7)
- Site Navigation: As a Site User I can easily navigate the site using the navbar or get back to the home page by clicking the logo. [#8](https://github.com/tadhgnolan/modern-message-board/issues/8)
- Select a Category: As a Site User I can select a topic category when creating a post. [#9](https://github.com/tadhgnolan/modern-message-board/issues/9)

## Technologies

### Languages

- [Python](https://www.python.org/about/)
- [HTML5](https://dev.w3.org/html5/spec-LC/)
- [CSS](https://www.w3.org/Style/CSS/Overview.en.html)

### Other Technologies and Libraries 

- [GitHub](https://github.com/)
- [GitPod](https://www.gitpod.io/about/)
- [Heroku](https://heroku.com)
- [Django](https://www.djangoproject.com/)
- [PostgreSQL](https://www.postgresql.org/about/)
- [Cloudinary](https://cloudinary.com/documentation)

## Features 

### Existing Features:

#### **Registration Page - allows new users to register an account with username and password.**

![Registration Page Image](https://github.com/tadhgnolan/modern-message-board/blob/main/static/documentation/images/registration.png)

#### **Login Page - registered user can login.**

![Login Page Image](https://github.com/tadhgnolan/modern-message-board/blob/main/static/documentation/images/login.png)

#### **Home Page - users can view list of posts.**

![Home Page Image](https://github.com/tadhgnolan/modern-message-board/blob/main/static/documentation/images/home.png)

#### **Add post - registered users can add new posts, enter a title and select a category from a drop down menu.**

![Add Post Page](https://github.com/tadhgnolan/modern-message-board/blob/main/static/documentation/images/add_post.png)

#### **Update post - registered users can update their existing posts.**

![Update Post Page](https://github.com/tadhgnolan/modern-message-board/blob/main/static/documentation/images/update_post.png)

#### **Delete post - registered users can delete their existing posts.**

![Delete Post Functionality Image](https://github.com/tadhgnolan/modern-message-board/blob/main/static/documentation/images/delete_post.png)

#### **Admin functionality - admins can add, update and delete categories.**

![Admin Functionality Image](https://github.com/tadhgnolan/modern-message-board/blob/main/static/documentation/images/admin.png)

### Features Left to Implement
- User Comments - Allow users to comment on their and other users posts.
- Post Images - Add the ability for users to post images.

## Testing

### Manual testing

- Manually testing each each path. 

---
**Manual Test of post paths**

---
![Manual Test Image](https://github.com/tadhgnolan/modern-message-board/blob/main/static/documentation/images/add_post.gif)

---
- ### Repeated real world testing performed with:

### **Google Pixel 3aXL (2160 × 1080px)**
---  
![Pixel 3aXL Image 1]()
![Pixel 3aXL Image 2]()

---
### **Fairphone 4 (1080 x 2340)**
---
![Fairphone 4 Image 1]()
![Fairphone 4 Image 2]()

---
### **Lenovo Ideapad Duet Chromebook (1080 x 1200px)**
---
**Laptop mode**

![Chromebook Laptop Mode Image 1]()
![Chromebook Laptop Mode Image 2]()

**Tablet mode**

![Chromebook Tablet Mode Image 1]()
![Chromebook Tablet Mode Image 2]()

---
### **Desktop PC (1920 x 1080px + 2560 × 1440) representing a mixture of age plus hardware capability & were readily available.**
---

**1920 x 1080px**

![1920 x 1080px Image 1]()
![1920 x 1080px Image 2]()

---

**2560 x 1440px**

![2560 x 1440px Image 1]()
![2560 x 1440px Image 2]()

---

### In Chrome Dev Tools, tested repeatedly with all available presets

This functionality testing involved:

- Verifying all navbar & other links functioned as expected.

---
**iPhone X**

---
![iPhone X Image]()

---
**Samsung Galaxy S20 Ultra**

---
![Samsung Galaxy S20 Ultra Image]()

---
**iPhone 6/7/8**

---
![iPhone 6/7/8 Image]()

---

- Using Chrome Dev Tools Elements tab to test out small styling changes before adding.

![Dev Tool Styling Image 1]()

![Dev Tool Styling Image 2]()

- Checking that fonts scaled correctly for each display size.

![Font Scaling Image](s)

- Checking for overflow.

**Checked for overflow using [Unicorn Revealer]()**

![Overflow Image]()


### Validator Testing 

- Tested html at https://validator.w3.org.

![HTML Validator Image 1]()
![HTML Validator Image 2]()

- Tested CSS at https://jigsaw.w3.org/css-validator/

![CSS Validator Image]()

### Lighthouse Score
![Lighthouse Score Image]()

### Unfixed Bugs

## Deployment

The live deployed application can be found at [modernmb](https://modernmb-45f157023587.herokuapp.com/).

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

- Select *New* in the top-right corner of your Heroku Dashboard, and select *Create new app* from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), and finally, select *Create App*.
- From the new app *Settings*, click *Reveal Config Vars*, and set the following key/value pairs:
  - `DATABASE_URL` (this comes from the **Resources** tab, you can get your own Postgres Database using the Free Hobby Tier)
  - `SECRET_KEY` (this can be any random secret key)

Heroku needs two additional files in order to deploy properly.
- requirements.txt
- Procfile

You can install this project's requirements (where applicable) using: `pip3 install -r requirements.txt`. If you have your own packages that have been installed, then the requirements file needs updated using: `pip3 freeze --local > requirements.txt`

The Procfile can be created with the following command: `echo web: gunicorn modern-message-board.wsgi > Procfile`

For Heroku deployment, follow these steps to connect your GitHub repository to the newly created app:

Either:
- Select "Automatic Deployment" from the Heroku app.

Or:
- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a <app_name>` (replace app_name with your app, without the angle-brackets)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type: `git push heroku main`

The frontend terminal should now be connected and deployed to Heroku.

### Local Deployment

*Gitpod* IDE was used to write the code for this project.

To make a local copy of this repository, you can clone the project by typing the follow into your IDE terminal:
- `git clone https://github.com/tadhgnolan/modern-message-board`

You can install this project's requirements (where applicable) using: `pip3 install -r requirements.txt`.

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/tadhgnolan/modern-message-board)

Additionally, you'll need to create your own `env.py` file with the following keys:

- `SECRET_KEY` (can be any secret value)
- `DATABASE_URL` (this comes from the "Resources" tab on your Heroku app)
   
   

## Credits 

 - A social media site designed by Tadhg Nolan
 
### Content 

- [Django Blog](https://github.com/Code-Institute-Solutions/Django3blog/tree/master/12_final_deployment) Used and modified code from this Github repository.

### Sites Used

- [Stack Overflow](https://stackoverflow.com/)
- [W3Schools](https://www.w3schools.com/)
- [r/python](https://www.reddit.com/r/Python/)
- [Reddit](https://www.reddit.com/)

### Special Thanks

- Cormac Nolan - Feedback and advice.
- Martina Terlevic & Tim Nelson - Mentors.