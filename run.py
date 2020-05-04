from predict import create_app
#Imports from the _init__.py file since we are working with packages

app = create_app() #Can take a config instance

if __name__ == '__main__':
    app.run(debug=True)
