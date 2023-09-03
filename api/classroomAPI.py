from .google_auth import getCreds
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

creds = getCreds()
def printCourses():
    try:
        service = build('classroom', 'v1', credentials=creds)

        # Call the Classroom API
        results = service.courses().list().execute()
        courses = results.get('courses', [])

        if not courses:
            print('No courses found.')
            return
        # Prints the names of the first 10 courses.
        print('Courses:')
        for course in courses:
            print(course['name'],course['id'])

    except HttpError as error:
        print('An error occurred: %s' % error)

def printStudents():
    course_id = 620830549055
    service = build('classroom', 'v1', credentials=creds)
    results = service.courses().students().list(courseId=course_id).execute()
    students = results.get('students', [])
    if not students:
        print(f'No students found in course {course_id}.')
    else:
        print(f'Students in course {course_id}:')
        for student in students:
            print(f"{student['profile']['name']['fullName']} ")