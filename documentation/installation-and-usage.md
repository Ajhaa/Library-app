## Installation
* Install python 3 and pip.  
* Clone the repository or download the zipped version and unzip it.  
* Install venv in to the project root with the command `python3 venv venv`.  
* Activate venv using the command `source venv/bin/activate`.  
* Install dependencies: `pip install -r requirements.txt`  
* The app can now be run with python: `python run.py`.

## Usage
If you are not logged in, you can only view books and authors. Currently both admins and normal users can be created freely.
Normal users, in addition to viewing, can also loan books and review them. the loan system is currently work in progress, and you
can only views your loans in user information page, which is also work in progress. The user information page can be accessed by going
to `/user/<user_id>`.  
Reviews can be written from the view book-page.  
Admins can create new books and authors, and also delete them. The delete button can be found from the individual view page of authors
and books. Admins can also change the availability of books, which currently has no effect.
