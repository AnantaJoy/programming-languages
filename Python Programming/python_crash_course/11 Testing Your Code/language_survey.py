from testing_a_class import AnonymousSurvey

# Define a question and make a survey
question = "What language did you learn to speak?"
my_survey = AnonymousSurvey(question)

# Show the question, and store responses to the question.
my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)

# Show the survey result
print("\nThank you everyone who participated in the survey!")
my_survey.show_result()