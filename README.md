# Welcome to Predict - adventures with python, tensorflow and flask

- Use pipenv to build: ```pipenv install```
- To init db write this in your shell:

```
    from predict import db
    db.create_all()
```

- To add some data:

```
    from predict import User, Post
    user_1 = User(username='Svante', email='s@s.se', password='password')
    db.session.commit()
```

- Verify that your db has some data in it:

```
    User.query.all()
```

- To clear your db from all data and tables:
```
    db.drop_all()
 ```

- To make the email part work you need to set the following environment variables
    - EMAIL_SERVER
    - EMAIL_USER
    - EMAIL_PASS