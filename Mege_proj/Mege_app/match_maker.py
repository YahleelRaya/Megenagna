from db_manager import DatabaseManager
class Match_maker:
    
     def __init__(self, db_manager):
        self.db_manager = db_manager
    
     def calculate_compatibility_score(self, worker, employer):
        # Same logic as your provided compatibility score calculation
        score = 0
        weights = {
            'job_type': 0.3,
            'schedule': 0.2,
            'language': 0.15,
            'experience': 0.15,
            'salary': 0.1,
            'special_requirements': 0.1
        }

        # Job type matching
        if worker['job_type'] in employer['required_job_types']:
            score += weights['job_type']

        # Schedule matching
        if worker['schedule'] == employer['schedule']:
            score += weights['schedule']

        # Language matching
        worker_languages = set(worker['languages'])
        employer_languages = set(employer['language_requirements'])
        if worker_languages & employer_languages:
            score += weights['language'] * (len(worker_languages & employer_languages) / len(employer_languages))

        # Experience matching
        if employer['requires_experience'] == 'Yes' and worker['experience'] == 'Yes':
            score += weights['experience']
        elif employer['requires_experience'] == 'No':
            score += weights['experience']

        # Salary matching
        employer_salary = employer['salary_budget']
        worker_salary = worker['expected_salary']
        salary_difference = abs(employer_salary - worker_salary)
        max_possible_difference = max(employer_salary, worker_salary)
        salary_score = 1 - (salary_difference / max_possible_difference) if max_possible_difference > 0 else 1
        score += weights['salary'] * salary_score

        # Special requirements matching
        if employer['special_requirements'] in worker.get('skills', ''):
         score += weights['special_requirements']

        return score
 
     def find_best_matches(self,employer_id, top_n=5):
         employer = self.employers_collection.find_one({'_id': employer_id})
         if not employer:
          return []

         workers = self.workers_collection.find()
         compatibility_scores = []
# Calculate compatibility score for each worker
         
         for worker in workers:
          score = self.calculate_compatibility_score(worker, employer)
          compatibility_scores.append((worker, score))

    # Sort workers by compatibility score in descending order
          compatibility_scores.sort(key=lambda x: x[1], reverse=True)

    # Return the top N matches
         return [worker for worker, score in compatibility_scores[:top_n]]
