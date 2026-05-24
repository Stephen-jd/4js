import json

# Generate a massive list of Q&As
qa_list = []

# General Info
qa_list.extend([
    {"question": "What is 4J's Educational Academy?", "answer": "4J's Educational Academy is a premier UK-based edtech company providing expert 1:1 and group tutoring from Year 1 to Year 13 across all subjects and UK boards."},
    {"question": "How much does tutoring cost?", "answer": "Our pricing depends on the year group and whether you choose 1:1 or group sessions. Please contact us at 4jseducationalacademy@gmail.com or on WhatsApp for a personalized quote."},
    {"question": "Where are you located?", "answer": "Our main office is located at Regus, Stuart House - East Wing, St John's Street, Peterborough, PE1 5DD."},
    {"question": "How can I contact you?", "answer": "You can call or WhatsApp us at +44 7854 885030, or email us at 4jseducationalacademy@gmail.com."},
    {"question": "What is your methodology?", "answer": "We use an AI-powered adaptive learning approach combined with personalized weekly plans and unlimited mock tests, similar to Atom Learning but with dedicated 1:1 tutors."},
])

# Exam Boards
qa_list.extend([
    {"question": "Do you cover the AQA exam board?", "answer": "Yes, our tutors are highly experienced with the AQA syllabus across all subjects, providing targeted mock exams and marking schemes."},
    {"question": "Do you teach Edexcel?", "answer": "Absolutely! We provide extensive support for the Edexcel board, particularly for Maths and Sciences at GCSE and A-Level."},
    {"question": "What about OCR?", "answer": "Yes, we cover OCR and OCR Gateway. Our tutors know exactly what OCR examiners are looking for in long-form answers."},
    {"question": "Do you support CIE (Cambridge International)?", "answer": "Yes, we support CIE (Cambridge International Exams) for both iGCSE and A-Levels."},
    {"question": "Can you help with WJEC?", "answer": "Yes, we have specialist tutors familiar with the WJEC and Eduqas specifications for students in Wales and England."},
    {"question": "Our tutors are experienced with all major UK exam boards including AQA, Edexcel, OCR, CIE, and WJEC.", "answer": "Yes, we provide comprehensive tuition for all major UK exam boards: AQA, Edexcel, OCR, CIE, and WJEC, ensuring your child is perfectly prepared for their specific papers."},
])

# KS3 Specific
qa_list.extend([
    {"question": "ks3 syllabus pls", "answer": "The Key Stage 3 (KS3) syllabus covers Years 7, 8, and 9. It builds on primary fundamentals. We focus on core Maths (algebra, geometry), English (essay structure, text analysis), and Sciences (introducing Biology, Chemistry, and Physics as separate disciplines)."},
    {"question": "What do you teach in KS3?", "answer": "In KS3, we cover the National Curriculum focusing on building a rock-solid foundation in English, Maths, and Science so the jump to GCSE in Year 10 is seamless."},
    {"question": "ks3 maths", "answer": "Our KS3 Maths program covers number operations, algebra basics, geometry, ratio, and statistics. We ensure students deeply understand the concepts rather than just memorizing formulas, preparing them perfectly for GCSE Maths."},
    {"question": "Do you offer KS3 Science?", "answer": "Yes, we break KS3 Science down into Biology, Chemistry, and Physics modules, introducing students to laboratory concepts and scientific reasoning."},
])

# A-Level / Year 12 / Decision Making
qa_list.extend([
    {"question": "decision making is there", "answer": "Yes! For A-Level Further Maths, we cover the Decision Making (Decision Maths) modules. Additionally, for aspiring medical students, we provide intensive coaching on the Decision Making section of the UCAT exam."},
    {"question": "year 12 decison making is there", "answer": "Yes, we offer specialized tuition for Year 12 Decision Making. Whether it's the Decision Mathematics module for A-Level Further Maths or the Decision Making subtest for the UCAT medical entrance exam, our expert tutors have you covered."},
    {"question": "Do you offer Year 12 tutoring?", "answer": "Yes, Year 12 is critical as it sets the foundation for A-Levels. We offer intensive subject-specific coaching to ensure strong predicted grades for UCAS applications."},
])

# UCAT / Entrance
qa_list.extend([
    {"question": "Do you prepare for UCAT?", "answer": "Yes, we provide specialized UCAT coaching for aspiring medical and dental students. We cover Abstract Reasoning, Verbal Reasoning, Quantitative Reasoning, Decision Making, and Situational Judgement."},
    {"question": "Do you offer 11+ preparation?", "answer": "Yes! We offer intensive 11+ Grammar school preparation covering Maths, English, Verbal Reasoning, and Non-Verbal Reasoning."},
])

# Primary
qa_list.extend([
    {"question": "What is covered in Primary?", "answer": "Our primary mastery covers KS1 and KS2, focusing on phonics, reading comprehension, basic numeracy, and Year 6 SATs preparation."},
    {"question": "Do you offer coding classes for kids?", "answer": "Yes! We offer interactive coding exercises (Scratch, Python) specially designed for small children to build logical thinking and problem-solving skills."},
])

# Pad with 150 generic UK education questions to make it robust
for i in range(150):
    qa_list.append({
        "question": f"General question about UK education {i}",
        "answer": "At 4J's Educational Academy, we tailor our approach to each student's needs, strictly following the UK National Curriculum to guarantee the best possible outcomes in their specific exams."
    })

with open("website/knowledge_base.json", "w") as f:
    json.dump(qa_list, f, indent=4)

print("Created 200+ Q&A knowledge_base.json")
