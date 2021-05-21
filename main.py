from notifypy import Notify
import uiucapi.query as ua
import time

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    current_semester = "FA21"

    notification = Notify()
    notification.application_name = "UIUC Registration Bot"
    notification.icon = "illinoisIcon.png"  # icons might not work on mac
    notification.audio = "Sound2.wav"

    # double and triple check that the CRN is correct
    # enter the the courses in this format ("SUBJECT NUMBER", CRN)
    # EX: courses_you_want  = [("CS 233",63735), ("CS 233", 63733), ("CS 361", 66305)]
    courses_you_want = [("CS 233",63735)]

    while (True):
        for course in courses_you_want:
            section = ua.get_course(course[0] + " " + current_semester).sections
            cour = ua.get_course(course[0] + " " + current_semester)
            for sec in section:
                if sec.crn == course[1] and 'open' in sec.registration_status.lower():
                    notification.title = cour.name + " OPEN"
                    notification.message = "The class" + " with this CRN" + str(sec.crn) + " is now OPEN!!"
                    notification.send(block=False)


        # Enter the time interval that the code searches for the class in second
        # 4 hours = 60 * 60 * 4
        # 5 minute = 60 * 5
        # 10 sec = 10
        time.sleep(5)
