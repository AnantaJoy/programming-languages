# assertEqual(x,y)
# assertNotEqual(x,y)
# assertTrue(x)
# assertFalse(x)
# assertIn(item, list)
# assertNotIn(item, list)

class AnonymousSurvey():
    """Collect anonymous answers to a survey question."""

    def __init__(self,question):
        """Store a question, and prepare to store response."""
        self.question = question
        self.responses = []
    
    def show_question(self,new_response):
        """Show the survey question."""
        print(question)
    
    def store_response(self, new_response):
        """Store a single response to the survey."""
        self.responses.append(new_response)

    def show_result(self):
        """Show all the responses that have been given."""
        print("Survey results:")
        for response in responses:
            print('-'+response)

