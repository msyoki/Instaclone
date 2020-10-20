# Instaclone

This python/django web-app is an academic project of an Instagram clone app. 
Developer: Musyoki Mutua

## Description
The web-app allows a user to create a profile,post images on the timeline,view posted images on the timeline,comment and like on posts and also search for a user via the search bar and view their profile.

## Setup/Installation Requirements
* Live site can be accessed from the following link 


### Behaviour Driven Development
* The program should return all users posts on the home page<br>
Given:All image posts<br>
When: Url is changed to home page<br>
Then: All Posts are displayed<br>

* Modal should be displayed when the user clicks on any post and have the post's details<br>
Given:A Post<br>
When: User cicks on the post <br>
Then: A modal with the post's details is displayed<br>

* Admin site should be displayed when "admin/" url is chosen<br>
Given: An admin url<br>
When: User enters admin url in browser<br>
Then: Admin Login is displayed<br>

* User authentication occurs when Admin tries to Login<br>
Given:Admin page is accessed<br>
When: User tries to login<br>
Then: User details are authenticated to confirm if user is an admin<br>

* User session should end when logout url is chosen<br>
Given:Logout option is given<br>
When: User chooses logout option<br>
Then: User session is ended<br>


### Technologies Used
* Python 
* Django framework
* Heroku for deployment

### Get started on the app


### Known Bugs
* No know bugs at the moment,please get in touch incase of any challenge.

### License
Copyright (c)2020 **Instagram by Musyoki Mutua**