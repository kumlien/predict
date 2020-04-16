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



You can use the [editor on GitHub](https://github.com/kumlien/predict/edit/master/README.md) to maintain and preview the content for your website in Markdown files.

Whenever you commit to this repository, GitHub Pages will run [Jekyll](https://jekyllrb.com/) to rebuild the pages in your site, from the content in your Markdown files.

### Markdown

Markdown is a lightweight and easy-to-use syntax for styling your writing. It includes conventions for

```
Syntax highlighted code block

# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/kumlien/predict/settings). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://help.github.com/categories/github-pages-basics/) or [contact support](https://github.com/contact) and we’ll help you sort it out.
