![model](https://yuml.me/a778768c.png)  
https://yuml.me/edit/a778768c

The database changed quite a lot from the original plan, but is accurate for the current version. Indexes were not used, partly because of developement time ran out.  

## .schema from sqlite:

CREATE TABLE genre (
        id INTEGER NOT NULL, 
        name VARCHAR NOT NULL, 
        PRIMARY KEY (id)
);
CREATE TABLE author (
        id INTEGER NOT NULL, 
        name VARCHAR NOT NULL, 
        birthdate DATETIME, 
        PRIMARY KEY (id)
);
CREATE TABLE role (
        id INTEGER NOT NULL, 
        role VARCHAR NOT NULL, 
        PRIMARY KEY (id)
);
CREATE TABLE book (
        id INTEGER NOT NULL, 
        title VARCHAR NOT NULL, 
        available BOOLEAN NOT NULL, 
        author_id INTEGER NOT NULL, 
        PRIMARY KEY (id), 
        CHECK (available IN (0, 1)), 
        FOREIGN KEY(author_id) REFERENCES author (id)
);
CREATE TABLE account (
        id INTEGER NOT NULL, 
        date_created DATETIME, 
        date_modified DATETIME, 
        name VARCHAR(144) NOT NULL, 
        username VARCHAR(144) NOT NULL, 
        password VARCHAR(144) NOT NULL, 
        role_id INTEGER, 
        PRIMARY KEY (id), 
        FOREIGN KEY(role_id) REFERENCES role (id)
);
CREATE TABLE review (
        id INTEGER NOT NULL, 
        score INTEGER NOT NULL, 
        text VARCHAR, 
        user_id INTEGER NOT NULL, 
        book_id INTEGER NOT NULL, 
        PRIMARY KEY (id), 
        FOREIGN KEY(user_id) REFERENCES account (id), 
        FOREIGN KEY(book_id) REFERENCES book (id)
);
CREATE TABLE bookgenre (
        book_id INTEGER NOT NULL, 
        genre_id INTEGER NOT NULL, 
        PRIMARY KEY (book_id, genre_id), 
        FOREIGN KEY(book_id) REFERENCES book (id), 
        FOREIGN KEY(genre_id) REFERENCES genre (id)
);
CREATE TABLE loan (
        id INTEGER NOT NULL, 
        start_date DATE NOT NULL, 
        end_date DATE NOT NULL, 
        book_id INTEGER NOT NULL, 
        user_id INTEGER NOT NULL, 
        PRIMARY KEY (id), 
        FOREIGN KEY(book_id) REFERENCES book (id), 
        FOREIGN KEY(user_id) REFERENCES account (id)
);

