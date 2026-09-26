from dao.student_dao import StudentDao
from dao.department_dao import DepartmentDao


class StudentService:
    def get_all_students(self):
        dao = StudentDao()
        students = dao.see_all_students()
        return students

    def get_student_by_id(self, idd):
        dao = StudentDao()
        student = dao.search_student_by_id(idd)
        return student

    def new_student(self, name, number, dept_name):
        stu_dao = StudentDao()
        dept_dao = DepartmentDao()

        if len(number) != 10:
            print("invalid mobile number. plz enter 10 digit mobile number: ")
            return
        
        dept_id = dept_dao.see_dept_id_using_dept_name(dept_name)
        if dept_id is not None:
            dept_id = dept_id[0]

        else:
            dept_dao.add_department(dept_name)
            dept_id = dept_dao.see_dept_id_using_dept_name(dept_name)[0]

        student = stu_dao.add_student(name, number, dept_id) 
        stu_id = stu_dao.find_student_id(name, number, dept_id)
        return stu_id[0]

        

