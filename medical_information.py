class MedicalInformation():

    def __init__(self, item_description, view_search, prob_questions, key_word):
        self.item_description = item_description
        self.view_search = view_search
        self.prob_questions = prob_questions
        self.key_word = key_word


    def __str__(self):
        return f"Description: {self.item_description},\nSearch: {self.view_search},\nProbing questions: {self.prob_questions},\nKey word: {self.key_word}"