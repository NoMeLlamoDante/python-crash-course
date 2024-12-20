class AnonymousSurvey:
    """Collect anonymouns answers to a survey question."""
    
    def __init__(self, question):
        """Store a question and prepare to store respones."""
        self.question = question
        self.responses = []
    
    def show_question(self):
        """Show the survey question"""
        print(self.question)
    
    def store_response(self, response):
        """Store a single response to the survey."""
        self.responses.append(response)
    
    def show_results(self):
        """Show all the responses that have been given."""
        print("Survey results:")
        for response in self.responses:
            print(f"- {response.title()}")