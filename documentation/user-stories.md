# User stories
## Normal user
* View all books in a list `SELECT * FROM book`  
* View a single book `SELECT * FROM book WHERE id = ?`
* * And the average score of the book `SELECT avg(score) FROM review WHERE book_id = ?`
* Review a book `INSERT INTO review (user_id, book_id, score, text) values (?, ?, ?, ?)`
* Loan a book `INSERT INTO LOAN (user_id, book_id, start_time, end_time) values (?, ?, current_timestamp, ?)`
* See stats in the front page:
* * Books with best reviews:  
`SELECT book.id, book.title, AVG(review.score) as avg FROM book, review  
                     WHERE review.book_id = book.id   
                     GROUP BY book.title  
                     ORDER BY avg DESC  
                     LIMIT 5 `
* * Books with most loans:  
`SELECT book.id, book.title, COUNT(loan.id) as loans FROM book, loan
                     WHERE loan.book_id = book.id
                     GROUP BY book.title
                     ORDER BY loans desc
                     LIMIT 5`




## Admin
* Add books `INSERT INTO book (title, available ,author_id) values(?, false, ?)
* Add authors `ÌNSERT INTO author (name, birthdate) values(?, ?)`
* Add genres `INSERT INTO genre (name) values(?)`

# My thoughts and what is missing?
To summarize, a lot was is missing. I was too ambitious with the original planning of this project. Combined with the fact that I didn't focus enough on the project, I'm pretty disapointed in it.  
The genre system completely failed, and will not be as fleshed out as I would like it to be. Also missing are a lot of restraints. Users can review or loan a book multiple times.  
The request system was completely scrapped, and other admin priviledges were not implemented.
Users cannot edit or delete their accounts.  
If only I hand focused more on the project, a lot of these could have been implemented.
