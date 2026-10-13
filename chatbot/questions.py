"""
questions.py

Stores the interview questions used by Course Compass.

The questions are intentionally conversational. Clickable answer chips
appear under each question (except name and JAMB). Students can also
type their own answer in the text box.
"""


QUESTIONS = [

    {
        "id": "name",
        "question": (
            "Before we get started, what's your name? 😊"
        )
    },

    {
        "id": "interests",
        "question": (
            "Now tell me about the things you genuinely enjoy.\n\n"
            "What kinds of things do you like doing, learning "
            "about or talking about?\n\n"
            "Tap the options that fit you (you can choose more than one), "
            "or type your own answer."
        )
    },

    {
        "id": "subjects",
        "question": (
            "What school subjects do you enjoy the most?\n\n"
            "Tap the subjects you enjoy (you can choose more than one), "
            "or type your own answer."
        )
    },

    {
        "id": "skills",
        "question": (
            "Your interests tell me what you enjoy, but "
            "your strengths tell me what you can actually do well.\n\n"
            "What skills are you confident in?\n\n"
            "Tap the skills that fit you (you can choose more than one), "
            "or type your own answer."
        )
    },

    {
        "id": "personality",
        "question": (
            "We're getting closer to your course profile. 😊\n\n"
            "How would you describe yourself when you work or learn?\n\n"
            "Tap the traits that sound like you (you can choose more than one), "
            "or describe yourself in your own words."
        )
    },

    {
        "id": "career_goal",
        "question": (
            "There's one more thing I want to understand about "
            "your direction.\n\n"
            "If you could choose any career, what would you "
            "love to become?\n\n"
            "Tap a career below, or type your own answer. "
            "Don't worry if it doesn't perfectly match your "
            "hobbies — people can have many interests and still "
            "have a clear career goal."
        )
    },

    {
        "id": "jamb_score",
        "question": (
            "Almost there! 🎓\n\n"
            "What is your JAMB score?\n\n"
            "Type your score, or type 'skip' if you haven't written JAMB yet."
        )
    },

    {
        "id": "additional_information",
        "question": (
            "Before I calculate your course recommendations, "
            "let's make sure I haven't missed anything important.\n\n"
            "Is there anything you forgot to tell me earlier?\n\n"
            "You could add another interest, subject, skill, "
            "personality trait or career goal.\n\n"
            "If you've already told me everything, just type "
            "'No' or 'That's all'."
        )
    }
]
