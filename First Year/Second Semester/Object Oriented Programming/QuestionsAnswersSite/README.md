Write an application which simulates a question and answer site (e.g. Stack Overflow), as follows:
1. The information about all the users is in a text file. Each user has a unique name. This file is manually created and it is read when the application starts.
2. Another two files contain information about the questions and answers that already exist on the site.
Each Question has an id, a text describing the question and the name of the user who asked it. Each Answer has its own id, the id or the associated question, the name of the user who answered, the text of the answer and the number of votes. These are read when the application starts.
3. When the application is launched, a new window is created for each user, having as title the user's name.
The window will show a list with all the questions asked so far, sorted descending by the number of answers for each question. (1p)
4. Another window will allow any user to search for a question: as the user types, the results are being shown. The best matching question (similarity score: number of matching letters on identical positions), together with its top three answers will be shown: answers underneath the question, tabbed and sorted descending by the number of votes. (1p)
5. Any user can add a new question, by inputting the question's text. The name of the user in the question will automatically be the name of the user who added it and the question will have no answers. This operation fails if the description is empty. (0.75p)
6. When a question is clicked, all the answers to that question are shown in another list (answer id, name of the user who answered, text, number of votes). The answers given by the current user will be shown with a yellow background. (0.75p)
7. Any user can add a new answer to a selected question. The name of the user who answered will be automatically taken and the number of votes will be 0. This operation fails if the text is empty. (0.75p)
8. Users can up vote and down vote a selected answer using a QSpinBox, which will initially show the current number of votes for the selected question. Users cannot up vote or down vote their own answers (the spinbox will be disabled). (0.75p)
9. When the application closes, the files containing questions and answers will be updated. (0.5p)
