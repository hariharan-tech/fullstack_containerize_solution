import unittest
from mongosetup import *


'''
Description : Complete the below method using MongoDB methods to insert a 'Books' document into
'Library' Database.

Points to note :
Try to use collections.insert_one(dictionary) method
The inserted document id is returned as part of insert_one() method.clear
The document is available only after it is inserted in the DB.
The id could be used to query the document later.


'''


def createBookDocument():

    # connect to 'Library' data base in MongoDB

    # connect to 'Books' collection

    collection = getCollectionsFromLibraryDB("Books")
    # user insertOne() method to create the document in MongoDB
    book_data = {"name":"Linear Integrated Circuits", "author":"Roy Choudhry","ISBN":"etho"}
    inserted_doc_id = collection.insert_one(book_data)

    return inserted_doc_id


class TestLab12(unittest.TestCase):
    def test_LibraryBooksCollection(self):
        # call create Book document
        inserted_doc_id = createBookDocument()
        # Test the created record
        book_data = getCollectionsFromLibraryDB(
            "Books").find({"_id": inserted_doc_id})
        print(book_data)
        self.assertIsNotNone(
            book_data, "No Books data found. It is suppose to be found.")


if __name__ == '__main__':
    unittest.main()