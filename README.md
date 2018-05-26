# BookStore-API
RAML api for a simple bookstore, use the go-raml to generate a server and client
## Install

`$ cd c:\user\BookStore`
and type:

`git init`
`git clone https://github.com/BolaNasr/BookStore-API.git`

### Using Python Server
`$  cd BookStore-API\server`

Install needed packages
```
pip install -r requirements.txt
```

You might want to install it inside virtualenv

Run the code
```
python app.py
```

The server will then run in port 5000, you can go to http://localhost:5000 to see default html page as described above

## Viewing and Editing RAML File

There are many ways to view and edit RAML file:

- [API Workbench](http://apiworkbench.com/) is an atom package for designing, building, testing, documenting and sharing RESTful HTTP APIs
- Vim : it is enough for simple purpose
