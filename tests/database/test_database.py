import unittest
from pymongo import MongoClient

class TestMongoDB(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        # Set up the MongoDB client and connect to the database
        cls.client = MongoClient('mongodb://localhost:27017/')
        cls.db = cls.client['test_database']

    @classmethod
    def tearDownClass(cls):

        # Close the MongoDB client connection
        cls.client.close()

    def setUp(self):

        # Set up the collection for each test
        self.collection = self.db['test_collection']
        self.collection.delete_many({})  # Clear the collection before each test

    def tearDown(self):

        # Clean up after each test
        self.collection.delete_many({})

    def test_insert_document(self):

        # Test inserting a document into the collection
        document = {'username': 'johndoe', 'password': '12345'}
        result = self.collection.insert_one(document)
        self.assertIsNotNone(result.inserted_id)  # Check that the document was inserted

    def test_find_document(self):

        # Test finding a document in the collection
        document = {'username': 'janedoe', 'password': 'abcde'}
        self.collection.insert_one(document)
        result = self.collection.find_one({'username': 'janedoe'})
        self.assertIsNotNone(result)  # Check that the document was found
        self.assertEqual(result['username'], 'janedoe')  # Verify the username
        self.assertEqual(result['password'], 'abcde')  # Verify the password

    def test_update_document(self):

        # Test updating a document in the collection
        document = {'username': 'johnsmith', 'password': '54321'}
        self.collection.insert_one(document)
        self.collection.update_one({'username': 'johnsmith'}, {'$set': {'password': '67890'}})
        result = self.collection.find_one({'username': 'johnsmith'})
        self.assertIsNotNone(result)  # Check that the document was found
        self.assertEqual(result['password'], '67890')  # Verify the updated password

    def test_delete_document(self):

        # Test deleting a document from the collection
        document = {'username': 'janesmith', 'password': 'qwerty'}
        self.collection.insert_one(document)
        self.collection.delete_one({'username': 'janesmith'})
        result = self.collection.find_one({'username': 'janesmith'})
        self.assertIsNone(result)  # Check that the document was deleted

    def test_insert_multiple_documents(self):

        # Test inserting multiple documents into the collection
        documents = [
            {'username': 'user1', 'password': 'pass1'},
            {'username': 'user2', 'password': 'pass2'},
            {'username': 'user3', 'password': 'pass3'}
        ]
        result = self.collection.insert_many(documents)
        self.assertEqual(len(result.inserted_ids), 3)  # Check that all documents were inserted

    def test_find_nonexistent_document(self):

        # Test finding a document that does not exist in the collection
        result = self.collection.find_one({'username': 'nonexistent'})
        self.assertIsNone(result)  # Check that no document was found

    def test_update_nonexistent_document(self):

        # Test updating a document that does not exist in the collection
        result = self.collection.update_one({'username': 'nonexistent'}, {'$set': {'password': 'newpass'}})
        self.assertEqual(result.matched_count, 0)  # Check that no document was matched

    def test_delete_nonexistent_document(self):

        # Test deleting a document that does not exist in the collection
        result = self.collection.delete_one({'username': 'nonexistent'})
        self.assertEqual(result.deleted_count, 0)  # Check that no document was deleted

    def test_find_all_documents(self):
        
        # Test finding all documents in the collection
        documents = [
            {'username': 'user1', 'password': 'pass1'},
            {'username': 'user2', 'password': 'pass2'},
            {'username': 'user3', 'password': 'pass3'}
        ]
        self.collection.insert_many(documents)
        result = list(self.collection.find({}))
        self.assertEqual(len(result), 3)  # Check that all documents were found

if __name__ == '__main__':
    unittest.main()