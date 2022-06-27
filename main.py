# coding=utf-8


class Student:
    """
    学生信息类
    """
    def __init__(self, name, id, gender):
        self.name = name
        self.id = id
        self.gender = gender


class StudentClass:
    """
    班级信息类
    """
    def __init__(self, class_name, head_teacher, chinese_teacher, math_teacher, english_teacher):
        self.class_name = class_name
        self.head_teacher = head_teacher
        self.chinese_teacher = chinese_teacher
        self.english_teacher = english_teacher
        self.math_teacher = math_teacher
        self.students = []

    def _get_student_ids(self):
        ids = [stu.id for stu in self.students]
        return ids

    def add_student(self, student):
        """
        将某一学生添加到班级
        :param student: 需要加入班级的学生
        :return:
        """
        ids = self._get_student_ids()
        if student.id in ids:
            print("ID: %s has already been added to this class." % student.id)
            return
        self.students.append(student)
        print("Add student %s successfully." % student.name)

    def show_class_members(self):
        """
        打印班级里面所有成员的信息
        :return:
        """
        print("Welcome to %s class" % self.class_name)
        print("Our head teacher is : %s" % self.head_teacher)
        print("Our chinese teacher is : %s" % self.chinese_teacher)
        print("Our english teacher is : %s" % self.english_teacher)
        print("Our math teacher is : %s" % self.math_teacher)
        print("Students are : \n")
        for student in self.students:
            print("name: %s id: %s gender: %s" % (student.name, student.id, student.gender))

    def search_student(self, id):
        """
        根据指定id查询该学生
        :param id: 待查询学生ID
        :return: 返回查询到的学生所有信息，否则返回None
        """
        for student in self.students:
            if student.id == id:
                return student
        return None

    def del_student(self, id):
        """
        :param id: 需要删除的学生id
        :return
        """
        ori_len = len(self.students)
        self.students = [student for student in self.students if student.id != id]
        new_len = len(self.students)
        if ori_len == new_len:
            print("ID：%s is not in this class." % id)


if __name__ == '__main__':
    myClass = StudentClass("一年级二班", "张英华", "李佳丽", "江疏影", "胡蓝")
    stu1 = Student("张三", "10001", "男")
    myClass.add_student(stu1)
    stu2 = Student("李四", "10002", "女")
    myClass.add_student(stu2)
    stu3 = Student("王五", "10003", "男")
    myClass.add_student(stu3)
    stu4 = Student("马六", "10004", "女")
    myClass.add_student(stu4)
    stu5 = Student("黄七", "10005", "男")
    myClass.add_student(stu5)
    stu6 = Student("高八", "10006", "女")
    myClass.add_student(stu6)
    myClass.show_class_members()
    myClass.del_student(stu5.id)
    myClass.show_class_members()

