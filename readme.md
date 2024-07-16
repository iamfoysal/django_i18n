first install the required packages by running the following command:

```bash
pip install -r requirements.txt
```

Then, run the following command to start the server:

```bash
sudo apt-get install gettext
python manage.py makemigrations

python manage.py migrate
python manage.py runserver
```

The server will start running at `http://localhost:8000/` by default. You can access the server by opening this link in your browser.

### Translations

To create translations for a new language, run the following commands:

```bash
django-admin makemessages -l <language_code>
```
###  Translations for the language code specified will be created in the `locale` directory. You can then translate the strings in the `.po` files in the `locale/<language_code>/LC_MESSAGES` directory.

After translating the strings, compile the translations by running the following command:

```bash
django-admin compilemessages
```
### The translations will be compiled and will be available in the corresponding `.mo` files in the `locale/<language_code>/LC_MESSAGES` directory.

### To switch the language of the application, you can change the `LANGUAGE_CODE` setting in the `settings.py` file to the language code of the language you want to use. or you can change the language from the admin panel.
