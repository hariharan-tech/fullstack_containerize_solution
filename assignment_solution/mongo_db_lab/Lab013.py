import unittest
from mongosetup import *


'''
Description : Complete the below method using MongoDB methods to insert a 'Books' document into
'Library' Database.

Points to note :
Try to use collections.insert_many([dictionaries]) method
The document is available only after it is inserted in the DB


'''


def createBookDocuments():

    # connect to 'Library' data base in MongoDB

    # connect to 'Books' collection
    collection = getCollectionsFromLibraryDB("Books")
    # user insert_many() method to create the document in MongoDB
    books_data = [{"name":"Linear Integrated Circuits", "author":"Roy Choudhry","ISBN":"etho"},
    {"name":"Ennatha Solla1", "author":"Hari","ISBN":"etho2"},
    {"name":"Ennatha Solla2", "author":"Hari","ISBN":"etho3"},
    {"name":"Ennatha Solla3", "author":"Hari","ISBN":"etho4"},
    {"name":"Ennatha Solla4", "author":"Hari","ISBN":"etho5"}]

    inserted_doc_id = collection.insert_many(books_data)
    print(inserted_doc_id)
    return inserted_doc_id


class TestLab11(unittest.TestCase):
    def test_LibraryBooksCollection(self):
        # call create Book document
        createBookDocuments()
        # Test the created record
        books_data = getCollectionsFromLibraryDB(
            "Books").find()
        print(books_data)

        self.assertIsNotNone(
            books_data, "No Books data found. It is suppose to be found.")
        self.assertTrue(len(list((books_data))) >= 5,
                        "Insert Many records failed")


if __name__ == '__main__':
    unittest.main()