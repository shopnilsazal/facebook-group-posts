# Facebook Group Posts

![alt Screenshot](https://github.com/shopnilsazal/facebook-group-posts/raw/master/screenshot.png "Screenshot")

## Setting Up

Install the dependencies from `requirements.txt` file.

`pip install -r requirements.txt`

Run the migration:

`python manage.py migrate `

We need to update the values for `FB_APP_ID` , `FB_APP_SECRET` and `FB_GROUP_ID` in `settings.py`. You can get the API Key and the Secret from [Facebook Developers portal](https://developers.facebook.com/apps/).

Once we have run the migrations and set the API keys, we can run the Django dev server: 

`python manage.py runserver`

Now visit the url - `http://localhost:8000` to see the app.
