# DevClub-Assignment-5
<br /> * This project contains four apps namely  Grades, Quizzes , Documents and users. 
<br />
<br /> * Users-Contains auth logic and models for Instructor, Student, Course, Admin. I have created two groups namely 'Instructors' and 'Students' and given the necessary permissions to users in respective groups. All the users including students, instructors and admin can login using http://localhost:8000/admin/login/?next=/admin/ and perform the allowed tasks.
<br />
<br /> * Quizzes-Contains a Question bank named-"Questions" which contains all the questions from which random questions and be selected to create a quiz. It also contains the answer bank named "Answers" which contains all the options used in all the Questions of MCQ type. I have also made the front end of the quiz. Anyone can attempt the quiz through http://localhost:8000/ .
<br />
<br /> * Documents- It allows instructors to upload documents like lecture notes and students can see them. The instructor can login through the admin portal and then go to file_uploads section to add or delete files. Each file added by instructor gets stored in a folder named 'media' in the 'Documents' folder. The uploaded files can be seen on http://localhost:8000/view or also after logging in to respective accounts.
<br />
<br /> * Grades- Contains logic for sharing grades for any assessment. Students can login through http://localhost:8000/admin/login/?next=/admin/ and see their grades on another tab through http://localhost:8000/grades/ .
<br />
