"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""

TESTS = {
    "Basics": [
        {
            "input": "The quick brown fox jumps over the lazy dog.",
            "answer": True,
        },
        {
            "input": "ABCDEF",
            "answer": False,
        },
        {
            "input": "abcdefghijklmnopqrstuvwxyz",
            "answer": True,
        },
        {
            "input": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
            "answer": True,
        },
        {
            "input": "abcdefghijklmnopqrstuvwxy",
            "answer": False,
        },
        {
            "input": "Bored? Craving a pub quiz fix? Why, just come to the Royal Oak!",
            "answer": True,
        },
        {
            "input": "As quirky joke, chefs won’t pay devil magic zebra tax.",
            "answer": True,
        },
        {
            "input": "Six big devils from Japan quickly forgot how to walt.",
            "answer": False,
        },
    ],
    "Extra": [
        {
            "input": [6, 3],
            "answer": 9,
            "explanation": "6+3=?"
        },
        {
            "input": [6, 7],
            "answer": 13,
            "explanation": "6+7=?"
        }
    ]
}
