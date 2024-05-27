from crewai import Task


def answer_question(agent, query):
    return Task(
        description=f"Answer user\'s question {query} related to gene.",
        agent=agent,
        expected_output='A phrase or a short report answering user\'s question.',
    )
