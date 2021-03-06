# STYLESERVICE #

This submission is for the Code Institute Stream 3 Full Stack Project. 

It is a fictional eCommerce website with a primary focus on subscriptions. It takes both subscriptions and single payments from the store with Stripe and also has User Authentication.
Additionally it houses a blog.

The initial mockups can be seen in the mockups folder. They are handdrawn and lay out how I wished the site to flow.

## LIVE DEMO ##

Follow this link to see the deployed version of the project -https://stejmscott-style-stream3.herokuapp.com/


## BUILT WITH ##

1. Django
2. Python
3. Html
4. CSS
5. JavaScript
6. SQLite database



## Django at a glance ##

Django is a very powerful framework that can greatly cut down on the amount of code one needs to write. It does so by using URLS, VIEWS and TEMPLATES primarily, but also on occasion, FORMS and CONTEXTS.

### URLS ###

At the base level of a Django project we have a urls.py file that contains the url patterns the site will have. 
They are passed in as `urlpatterns = [url(r'^appname/', view_name, name='shortcutfortemplate')]`
URLS from other apps are imported  as follows : `from appname import urls as apps_urls` is placed above the urlpatterns.
Within the urlpatterns we include the imported urls as ` urlpatterns= [url(r'^appname/', include(apps_urls))]`

### VIEWS ###

View are called by the given URLS and undertake a particular function related to the URL in question, ranging from simple rendering a pages Template to a whole host of things, including log in/out, forms to name but a few. 

### TEMPLATES ###

The base.html page in the base level template folder is used as a base for the rest of the pages on a given site. In this project, Index.html was not extended from the base.html as the mobile design I was going for would not work within those confines. 
The base.html is a template that includes all the head elements linking to the likes of bootstrap, jQuery and of course your own CSS.  The sites navbar and footer are also housed here. 
Within the area of the page one would expect content we see
```
{% block content %}
{% endblock content %}
```

This allows all other templates to insert themselves within that space saving time and lines of code, we simply link to the base.html from any template with any of the site  as follows:

```
{% extends 'base.html %}

{% block content %}

All the code for the particular page is placed in here and will be rendered between the Navbar and Footer from 'base.html'

{% endblock content %}

```


## APPS ##

### STYLESERVICE (Home) ###
This is the base of the project and contains the template folder in which 'base.html' is. The base urls.py file is here and the views render the index.html

### Accounts and Packages ###

This app is used for user authentication. Within this app holds all the urls, views and templates for a visitor to the site to register, log in and become a potential customer. They also have the ability to log out. The monthly subscriptions to the styleservice is contained within this app and redirects users to their profile page after they subscribe. From here they can manage/cancel their subscriptions. 

Initially the plan was to hold several subscription types help within the packages app. Due to time constraints these were not implemented but are something that will be updated in the future.

### Products and Categories 

The eCommerce element of this website is contained within these two apps. A small but wide selection of clothing and accessories were added using the admin panel. They can be searched for by category and there is a small menu that filters the categories at the top of 'products.html'

Reviews on products were handled by the Django-Star-Ratings package. After deployment the stars.png was unfortuently not rendering on the heroku page. The mechanism behind the package is still functional and can be observed above the products image in 'product_detail.html'. Investigation showed the star.png was in the S3 bucket and several forums suggested it may refresh and appear within 24hrs. 
If that is not the case...

* What they should look like:<br/>
![Working Star](mockups/starinaction.png)

### Cart and Checkout ###

The cart app uses a 'contexts.py' file to store a users cart contents in a session. The checkout is able to take this session and put the payment through as a one off payment with Stripe.

### BLOG ###

The blog was set up to render posts, or fashion peices. A user is not able to create their own posts as I wished that to be just for "Stylists" but they can comment under posts. 
The 'posts.html' page has the beginning of each posts contents truncated so as the user needs to click in to read the rest. 


## Deployment and Hosting ##
This Project was deployed and is hosted on Heroku with automatic deploys from GitHub. 

## Databases and Static ##
### Databases ###
Running locally a SQLite database was used. When Deployment occured a Heroku Postgres database was used.
### Static ###
Running locally static and media files were stored locally. On Deployment an Amazon S3 bucket was used. 

The settings.py file had to be changed to facilitate the switch over. 


## Installation

To clone this project take the following steps:

* Click the green "Clone or Download" button from the top right of this repository.
* Copy the link into your clipboard, or take it from here - https://github.com/StephenJMScott/finalproject.git
* Within your terminal ensure you are in the folder you wish to contain the project
* Create a virtualenv : `virtualenv -p python3`
* Activate virtualenv: `source bin/activate`
* Type the following into the command line: `$ git clone "https://github.com/StephenJMScott/finalproject.git`
* The entire project should be now contained within your desired folder. 
* Ensure all project dependancies are installed using : `$ pip install -r requirements.txt`
* Within your bash.rc file or equivilant you will need to create the following :
```
export SECRET_KEY=''
export DEBUG='True'

export STRIPE_PUBLISHABLE_KEY=''
export STRIPE_SECRET_KEY=''

export EMAIL_HOST_USER='your@gmail.com'    
export EMAIL_HOST_PASSWORD='yourPassword'

```
Follow this link to create a new Secret Key- https://www.miniwebtool.com/django-secret-key-generator/

Follow this [link](https://stripe.com
), create a Stripe account and paste the STRIPE_PUBLISHABLE_KEY, and STRIPE_SECRET_KEY in.


Within the settings.py file, line 28 contains `USE_S3 = os.environ.get("USE_S3", True)`
When False you are running locally, when true you're running from the S3 buckets ect. 


## TESTING ##

Throughout this project manual testing was undertaken as well as automated testing. 

`$ python3 manage.py test APPNAME`

### Products ###

`$ python3 manage.py test products` - Will pass. A product requested will be the product returned.
 
### Packages ###

`$ python3 manage.py test packages` - Will pass. A package requested will be the package returned.

### Cart ###
`$ python3 manage.py test cart` - Will pass. The url for '/cart/' resolves to the 'cart' function in views.py

### Blog ###
`$ python3 manage.py test packages` - Will pass. The post title requested will be the post returned.

### Accounts ###

`$ python3 manage.py test accounts` - Unfortuently this will not pass as Django is failing to load "the parent '' module. "

I believe this issue is to do with the enviroment not the actual application, as manual testing on all account functions are working as should. 


## A note on development ##

The initial commit of this project is further in than I would have liked. This is primarily down to Django updating to 2.0 over a weekend that I ran into critical errors and had to restart numerous times. 
The repos "stream3project" , "styleservicestream3", "stream3styleservice" and "stream3styleproj" have been kept intact both as a reminder to keep updates in mind and to show my first steps if you so wish to look.  On the bright side as a result of this I can get a very simple ecommerce app up and running now in about 90 minutes if not less.
