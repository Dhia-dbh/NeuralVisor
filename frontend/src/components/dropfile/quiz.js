export const quiz = {
    topic: 'Machine Learning',
    level: 'Beginner',
    totalQuestions: 3,
    perQuestionScore: 5,
    questions: [
        {
            question: 'What is machine learning?',
            choices: [
                'A subset of artificial intelligence',
                'A data storage method',
                'A type of hardware',
                'None of the above'
            ],
            type: 'MCQs',
            correctAnswer: 'A subset of artificial intelligence',
        },
        {
            question: 'How does a machine learn?',
            choices: [
                'By analyzing data and finding patterns',
                'By manual programming of rules',
                'By receiving direct commands from users',
                'None of the above'
            ],
            type: 'MCQs',
            correctAnswer: 'By analyzing data and finding patterns',
        },
        {
            question: 'Which of these is a real-world application of machine learning?',
            choices: [
                'Spam email filtering',
                'Automated ticket booking',
                'Weather forecasting',
                'All of the above'
            ],
            type: 'MCQs',
            correctAnswer: 'All of the above',
        },
    ],
};