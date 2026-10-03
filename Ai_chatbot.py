print("=" * 50)
print("      COLLEGE ADMISSION AI CHATBOT")
print("=" * 50)

courses = [
    "B.E Computer Science and Engineering",
    "B.E Electronics and Communication Engineering",
    "B.E Mechanical Engineering",
    "B.E Electrical and Electronics Engineering",
    "B.Tech Information Technology",
    "B.Sc Computer Science"
]

documents = [
    "10th Mark Sheet",
    "12th Mark Sheet",
    "Transfer Certificate",
    "Community Certificate",
    "Aadhaar / Government ID",
    "Passport-size photographs"
]


def chatbot(user_input):

    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! Welcome to the College Admission Chatbot."

    elif "course" in user_input or "courses" in user_input:
        result = "Available Courses:\n"

        for i, course in enumerate(courses, 1):
            result += f"{i}. {course}\n"

        return result

    elif "eligibility" in user_input or "eligible" in user_input:
        return "Students must satisfy the required educational qualification and admission rules for the selected course."

    elif "fee" in user_input or "fees" in user_input:
        return "Course fees depend on the selected program and admission category. Contact the admission office for current fees."

    elif "document" in user_input:
        result = "Required Documents:\n"

        for i, document in enumerate(documents, 1):
            result += f"{i}. {document}\n"

        return result

    elif "admission process" in user_input or "how to apply" in user_input:
        return """Admission Process:
1. Select a course
2. Check eligibility
3. Fill application form
4. Submit documents
5. Pay applicable fee
6. Attend verification/counselling
7. Confirm admission"""

    elif "scholarship" in user_input:
        return "Scholarships may be available according to government and college rules."

    elif "hostel" in user_input:
        return "Hostel facilities may be available depending on accommodation capacity."

    elif "transport" in user_input or "bus" in user_input:
        return "College transport may be available on selected routes."

    elif "placement" in user_input:
        return "The college may provide placement training and recruitment opportunities."

    elif "contact" in user_input:
        return """Contact Information:
Phone: 9876543210
Email: admission@abccollege.edu
Address: College Road, Tamil Nadu"""

    elif "bye" in user_input or "exit" in user_input:
        return "Thank you for using the College Admission Chatbot. Goodbye!"

    else:
        return "Sorry, I don't understand. Please ask about courses, fees, eligibility, documents, hostel, scholarship, or admission process."


while True:

    user = input("\nYou: ")

    response = chatbot(user)

    print("\nAI Bot:", response)

    if "bye" in user.lower() or "exit" in user.lower():
        break