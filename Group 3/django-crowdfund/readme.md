
![Untitled design (16)](https://user-images.githubusercontent.com/88078870/232046983-46bb3c46-33a0-413a-98df-6a098c5fe5b5.png)

# Django-Crowdfunding

Django-Crowdfunding is a web application built with Django framework for crowdfunding campaigns. Users can create, edit, and delete their own campaigns, and others can donate to these campaigns with payment integration using Razorpay. The application also supports login via Google using allauth for authentication. Email notifications are sent for campaign updates and donations.

## Live Preview: http://django-crowdfunding.varad13.tech/
- Payments are not enabled as this is just meant to be a preview. For emulating a successful payment, please use UPI id success@razorpay
- Payouts can be added later whenever RazorpayX is released for everyone

## Features
- Login via Google using allauth

- Campaign creation, editing, and deletion

- Campaign donation with payment integration using Razorpay

- Email notifications for campaign updates and donations

## Getting Started
To get started with Django-Crowdfunding, follow these instructions:

### Prerequisites
- Python 3.7 or higher

- Virtual environment (recommended)

- Google API keys for Google OAuth

### Obtaining Google API keys

1. Go to the Google Cloud Console at [https://console.cloud.google.com/](https://console.cloud.google.com/).

2. Create a new project or select an existing project.

3. In the left sidebar, click on "Credentials".

4. Click on "Create credentials" and select "OAuth client ID".

5. Choose "Web application" as the application type.

6. Enter a name for your OAuth client ID and click "Create".

7. Under "Authorized redirect URIs", add the callback URL for your Django app. For example: `http://localhost:8000/accounts/google/login/callback/` for local development. Make sure to update this URL with the appropriate domain name or IP address when hosting your app.

8. Under "Authorized JavaScript origins", add the domain or IP address where your app will be hosted.

9. Click "Save" to create the OAuth client ID.

10. In the "Consent screen" tab, configure the consent screen for your app. You can add the "email" scope to access the user's email address during authentication.

11. Click "Save" to save the consent screen settings.

12. You will be provided with a client ID and client secret. Update your Django admin with these values in the "Social Applications" section as mentioned in the README.

You can refer to the following link for more details: [Google Cloud Console Documentation](https://cloud.google.com/docs/authentication/getting-started#creating_a_client_id_and_client_secret)

### Obtaining Razorpay API keys

1. Go to the Razorpay Dashboard at [https://razorpay.com/docs/](https://razorpay.com/docs/).

2. Log in to your Razorpay account or sign up for a new account.

3. In the Dashboard, go to the "Settings" tab in the left sidebar.

4. Click on "API Keys" under "App Settings".

5. You will find your "Key ID" and "Key Secret". Update your secret.py file with these values for `RAZOR_KEY_ID` and `RAZOR_KEY_SECRET`.

6. Click "Save" to save the API keys.

You can refer to the following link for more details: [Razorpay Documentation](https://razorpay.com/docs/)

### Installation

1. Clone the repository:
	```bash
	git clone https://github.com/Varad-13/crowdfunding-django.git
2. Navigate to the project directory:
	```bash
	cd crowdfunding-django
3. Create a virtual environment (optional but recommended):
	```bash
	python3 -m venv venv
	source venv/bin/activate
4. Install the dependencies from requirements.txt:
	```bash
	pip install -r requirements.txt
5. Add necessary content to cf/secret.py:
	```python
	SECRET_KEY = ''  # Add your Django secret key here
	EMAIL_HOST_USER = ''  # Add your email host username here
	EMAIL_HOST_PASSWORD = ""  # Add your email host password here
	RAZOR_KEY_ID = ""  # Add your Razorpay API key ID here
	RAZOR_KEY_SECRET = ""  # Add your Razorpay API key secret here
6. Make and apply the database migrations:
	```bash
	python manage.py makemigrations
	python manage.py migrate
7. Create a superuser for Django admin:
	```bash
	python manage.py createsuperuser
8. Add your Google API keys to the Django admin:

- Log in to Django admin at `http://localhost:8000/admin/` (or the URL where you have hosted the app).

- Go to "Social Applications" under "Social Accounts".

- Click "Add Social Application" and fill in the details for your Google API keys.

9. Run the development server:
	```bash
	python manage.py runserver
10. Access the application in your web browser at `http://localhost:8000/` (or the URL where you have hosted the app).

## Contributing
Contributions to Django-Crowdfunding are welcome! If you find any issues or have any suggestions, please feel free to open an issue or submit a pull request.

## Some Screenshots
- Homepage
![image](https://user-images.githubusercontent.com/88078870/232048262-3c517fec-259e-426b-b8a0-0e0c223766d4.png)
- Post with only thumbnail
![image_2023-04-14_17-52-13](https://user-images.githubusercontent.com/88078870/232047625-13799c52-9b9e-44f9-959b-4fee4612f050.png)
- Post with thumbnail and video
![image_2023-04-14_17-52-27](https://user-images.githubusercontent.com/88078870/232047678-2f280d2a-0ef2-44d4-8814-ae608cb72c50.png)
- Creating/Editing Post
![image_2023-04-14_17-52-45](https://user-images.githubusercontent.com/88078870/232047741-a88c4e95-f34c-4554-b5ed-ca86458aba76.png)
- Razorpay
![image_2023-04-14_17-53-04](https://user-images.githubusercontent.com/88078870/232047950-732fb717-066f-4ed8-9c07-5e9729541157.png)

## License
Django-Crowdfunding is open source and available under the [GNU General Public License](https://www.gnu.org/licenses/gpl-3.0.html).
