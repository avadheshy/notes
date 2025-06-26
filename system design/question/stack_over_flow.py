"""
Designing Stack Overflow
Requirements
Users can post questions, answer questions, and comment on questions and answers.
Users can vote on questions and answers.
Questions should have tags associated with them.# completed
Users can search for questions based on keywords, tags, or user profiles.# completed
The system should assign reputation score to users based on their activity and the quality of their contributions.
The system should handle concurrent access and ensure data consistency.


I will give 100 points for answer 10 points for question and 5 points for each comments 2 points for vote
"""

class User:
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.questions = []
        self.answers = []
        self.comments = []
        self.votes = []

    def show_points(self):
        print(f"{self.name} has {self.points} points.")

    def show_questions(self):
        print(f"{self.name}'s questions:")
        for question in self.questions:
            print("-", question.question)

    def show_answer(self):
        print(f"{self.name}'s answers:")
        for answer in self.answers:
            print("-", answer.answer)


class Vote:
    def __init__(self, user):
        self.user = user


class Comment:
    def __init__(self, text, user):
        self.comment = text
        self.user = user


class Answer:
    def __init__(self, answer, user):
        self.answer = answer
        self.user = user
        self.votes = []
        self.comments = []

    def display_ans(self):
        print(f"Answer: {self.answer} (by {self.user.name})")

    def vote_to_answer(self, user):
        vote = Vote(user)
        self.votes.append(vote)
        user.votes.append(vote)
        user.points += 2

    def comment_on_answer(self, comment_text, user):
        comment = Comment(comment_text, user)
        self.comments.append(comment)
        user.comments.append(comment)
        user.points += 5

    def display_comments(self):
        print("Answer Comments:")
        for comment in self.comments:
            print(f"{comment.user.name}: {comment.comment}")

    def total_votes(self):
        print(f"Total votes on answer: {len(self.votes)}")


class Question:
    def __init__(self, text, user, tags=[]):
        self.question = text
        self.tags = tags
        self.votes = []
        self.comments = []
        self.answer = []
        self.user = user
        user.questions.append(self)

    def display_question(self):
        print("##" * 18)
        print(f"Question: {self.question} (by {self.user.name})")

    def display_tags(self):
        print("**" * 18)
        print("Tags:", ", ".join(self.tags))

    def display_comments(self):
        print("$$" * 18)
        print("Comments:")
        for comment in self.comments:
            print(f"{comment.user.name}: {comment.comment}")

    def get_total_votes(self):
        print(f"Total votes for this question: {len(self.votes)}")

    def vote_to_question(self, user):
        vote = Vote(user)
        self.votes.append(vote)
        user.votes.append(vote)
        user.points += 2

    def comment_on_question(self, comment_text, user):
        comment = Comment(comment_text, user)
        self.comments.append(comment)
        user.comments.append(comment)
        user.points += 5

    def answer_question(self, answer_text, user):
        ans = Answer(answer_text, user)
        self.answer.append(ans)
        user.answers.append(ans)
        user.points += 100


class StackOverFlow:
    def __init__(self):
        self.questions = []

    def get_user(self, name):
        return User(name)

    def ask_question(self, text, user, tags=[]):
        question = Question(text, user, tags)
        self.questions.append(question)
        return question

    def search_question(self, tag=None, keyword=None):
        print("Search results:")
        for question in self.questions:
            match = False
            if tag and tag in question.tags:
                match = True
            elif keyword and (keyword in question.question or keyword in question.tags):
                match = True
            if match:
                print("-", question.question)


if __name__ == '__main__':
    stack_over_flow = StackOverFlow()
    
    avadhesh = stack_over_flow.get_user("Avadhesh")
    ayush = stack_over_flow.get_user("Ayush")
    adesh = stack_over_flow.get_user("Adesh")

    avadhesh_question = stack_over_flow.ask_question("Why is Python the best programming language?", avadhesh, ['python', 'coding'])
    ayush_question = stack_over_flow.ask_question("What is an even number?", ayush, ['math', 'numbers'])
    adesh_question = stack_over_flow.ask_question("What is OOPs concept in Python?", adesh, ["python", "OOPS"])

    ayush_question.answer_question("Those numbers which are divisible by 2 are even numbers.", avadhesh)
    ayush_question.answer_question("Every alternate number starting from 2 is even.", adesh)
    
    avadhesh_question.answer_question("Python's syntax is very easy.", ayush)
    avadhesh_question.answer_question("Python is close to natural English.", adesh)

    adesh_question.answer_question("OOPs means Object-Oriented Programming.", ayush)
    adesh_question.answer_question("We solve real-world problems using objects.", avadhesh)

    # Voting and Commenting
    adesh_question.comment_on_question("This is a good question.", avadhesh)
    ayush_question.vote_to_question(adesh)

    # Show user details
    avadhesh.show_points()
    avadhesh.show_answer()

    ayush.show_points()
    ayush.show_answer()

    adesh.show_points()
    adesh.show_answer()

    print("\nSearching questions by tag:")
    stack_over_flow.search_question(tag='python')

    print("\nSearching questions by keyword:")
    stack_over_flow.search_question(keyword='coding')

    print("\nQuestions asked by Avadhesh:")
    
