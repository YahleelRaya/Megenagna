from pymongo import MongoClient
class DatabaseManager:
    def __init__(self, db_url, db_name): 
        self.client = MongoClient(db_url) 
        self.db = self.client[db_name]
        self.employers_collection = self.db['Employer_Coll']
        self.workers_collection = self.db['Worker_Coll']
        self.matches_collection = self.db['Matches'] 
    
    def get_employer(self, employer_id):
        return self.employers_collection.find_one({'_id': employer_id})
    
    def get_worker(self,worker_id):
        return self.workers_collection.find_one({'_id': worker_id})
    
    def save_match(self, employer_id, worker_id, score):
        if not employer_id or not worker_id or score is None:
         raise ValueError("Invalid match data provided.")
        # Store match result in a separate collection, if desired
        self.matches_collection.insert_one({
            'employer_id': employer_id,
            'worker_id': worker_id,
            'score': score
        })
    
