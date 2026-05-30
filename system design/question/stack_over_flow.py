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
from threading import Lock
from enum import Enum


class VoteType(Enum):
    UPVOTE = 1
    DOWNVOTE = -1



POINTS = {
    'ask_question':      5,
    'answer_question': 100,
    'comment':           5,
    'upvote_received':  10,   
    'downvote_received': -2,
}


class Vote:
    def __init__(self, user, vote_type: VoteType):
        self.user = user
        self.vote_type = vote_type


class Comment:
    def __init__(self, text: str, user):
        self.text = text
        self.user = user


class Answer:
    def __init__(self, text: str, user):
        self.text = text
        self.user = user
        self.votes: list[Vote] = []
        self.comments: list[Comment] = []
        self._lock = Lock()

    def vote(self, voter, vote_type: VoteType):
        with self._lock:
            for v in self.votes:
                if v.user == voter:
                    print(f"  {voter.name} already voted on this answer.")
                    return
            v = Vote(voter, vote_type)
            self.votes.append(v)
            if vote_type == VoteType.UPVOTE:
                self.user.reputation += POINTS['upvote_received']
            else:
                self.user.reputation += POINTS['downvote_received']

    def comment(self, text: str, commenter):
        with self._lock:
            c = Comment(text, commenter)
            self.comments.append(c)
            commenter.comments.append(c)
            commenter.reputation += POINTS['comment']

    @property
    def vote_score(self) -> int:
        return sum(v.vote_type.value for v in self.votes)

    def display(self):
        print(f"  Answer by {self.user.name} [score: {self.vote_score}]: {self.text}")


class Question:
    def __init__(self, question_id: int, text: str, user, tags: list[str]):
        self.question_id = question_id
        self.text = text
        self.user = user
        self.tags: list[str] = tags         
        self.answers: list[Answer] = []
        self.comments: list[Comment] = []
        self.votes: list[Vote] = []
        self._lock = Lock()

    def vote(self, voter, vote_type: VoteType):
        with self._lock:
            for v in self.votes:
                if v.user == voter:
                    print(f"  {voter.name} already voted on this question.")
                    return
            v = Vote(voter, vote_type)
            self.votes.append(v)
            if vote_type == VoteType.UPVOTE:
                self.user.reputation += POINTS['upvote_received']
            else:
                self.user.reputation += POINTS['downvote_received']

    def answer(self, text: str, user):
        with self._lock:
            ans = Answer(text, user)
            self.answers.append(ans)
            user.answers.append(ans)
            user.reputation += POINTS['answer_question']
            return ans

    def comment(self, text: str, commenter):
        with self._lock:
            c = Comment(text, commenter)
            self.comments.append(c)
            commenter.comments.append(c)
            commenter.reputation += POINTS['comment']

    @property
    def vote_score(self) -> int:
        return sum(v.vote_type.value for v in self.votes)

    def display(self):
        print(f"\nQ[{self.question_id}] by {self.user.name} [score: {self.vote_score}]: {self.text}")
        print(f"  Tags: {', '.join(self.tags)}")
        for ans in self.answers:
            ans.display()


class User:
    def __init__(self, user_id: int, name: str):
        self.user_id = user_id
        self.name = name
        self.reputation = 0
        self.questions: list[Question] = []
        self.answers: list[Answer] = []
        self.comments: list[Comment] = []

    def show_profile(self):
        print(f"\n── {self.name} (id={self.user_id}) | rep={self.reputation} ──")
        print(f"  Questions : {len(self.questions)}")
        print(f"  Answers   : {len(self.answers)}")
        print(f"  Comments  : {len(self.comments)}")




class StackOverflow:
    def __init__(self):
        self.questions: list[Question] = []
        self._users: dict[int, User] = {}       
        self._next_q_id = 1
        self._lock = Lock()                     


    def create_user(self, name: str) -> User:
        with self._lock:
            user_id = len(self._users) + 1
            user = User(user_id, name)
            self._users[user_id] = user
            return user

    def get_user_by_id(self, user_id: int) -> User | None:
        return self._users.get(user_id)


    def ask_question(self, text: str, user: User, tags: list[str] = None) -> Question:
        with self._lock:
            q = Question(self._next_q_id, text, user, tags or [])
            self._next_q_id += 1
            self.questions.append(q)
            user.questions.append(q)
            user.reputation += POINTS['ask_question']
            return q

    
    def search(self, tag: str = None, keyword: str = None, user: User = None) -> list[Question]:
        results = []
        for q in self.questions:
            if tag and tag in q.tags:
                results.append(q)
            elif keyword and (keyword.lower() in q.text.lower()
                              or any(keyword.lower() in t for t in q.tags)):
                results.append(q)
            elif user and q.user == user:      
                results.append(q)
        return results

    def display_search(self, **kwargs):
        results = self.search(**kwargs)
        print(f"\nSearch {kwargs} → {len(results)} result(s):")
        for q in results:
            q.display()




if __name__ == '__main__':
    sof = StackOverflow()

    avadhesh = sof.create_user("Avadhesh")
    ayush    = sof.create_user("Ayush")
    adesh    = sof.create_user("Adesh")

    q1 = sof.ask_question("Why is Python the best language?", avadhesh, ['python', 'coding'])
    q2 = sof.ask_question("What is an even number?",          ayush,    ['math', 'numbers'])
    q3 = sof.ask_question("What is OOPs in Python?",          adesh,    ['python', 'oops'])

    q2.answer("Numbers divisible by 2.", avadhesh)
    q2.answer("Every alternate number starting from 2.", adesh)

    q1.answer("Python syntax is very easy.", ayush)
    q1.answer("Python reads like English.", adesh)

    q3.answer("OOPs = Object-Oriented Programming.", ayush)
    q3.answer("We model real-world problems as objects.", avadhesh)

    q1.vote(ayush, VoteType.UPVOTE)
    q1.vote(adesh, VoteType.UPVOTE)
    q1.vote(ayush, VoteType.UPVOTE)        

    q2.answers[0].vote(ayush, VoteType.UPVOTE)
    q2.answers[1].vote(avadhesh, VoteType.DOWNVOTE)

    # Comments
    q3.comment("Great question!", avadhesh)
    q1.answers[0].comment("Totally agree.", adesh)

    # Search
    sof.display_search(tag='python')
    sof.display_search(keyword='even')
    sof.display_search(user=adesh)          

    # Profiles with reputation
    avadhesh.show_profile()
    ayush.show_profile()
    adesh.show_profile()
    
