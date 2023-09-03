from medical_information import MedicalInformation

class ToolManager():
    def __init__(self):
        self.med_information = []

    def add_med_info(self, item_description, view_search, prob_questions, key_word):
        content = MedicalInformation(item_description, view_search, prob_questions, key_word)
        self.med_information.append(content)

    def search_med_info(self, key_word):
        for content in self.med_information:
            if content.key_word == key_word:
                return content
            return None

    def list_med_info(self):
        for content in self.med_information:
            print(content)