from sqlalchemy import func, or_
from infrastructure.db.course_schema import Course

class CourseRepositoryPostgres():

    def add_course(self, db, payload):
        db.add(payload)
        db.commit()        


    def get_all_courses(self, db, category, subscription_type, text):

        partial_query = db.query(Course)

        if category != None:
            partial_query = partial_query.filter(Course.category.in_(category))

        if subscription_type != None:
            partial_query = partial_query.filter(Course.subscription_type.in_(subscription_type))

        if text != None:
            partial_query = partial_query.filter(or_(func.lower(Course.name).contains(text.lower()), func.lower(Course.description).contains(text.lower())))

        courses_list = partial_query.all()
        return courses_list
        

    def get_course_by_id(self, db, course_id):
        course = db.query(Course).get(course_id)
        return course


    def update_course(self, db):
        db.commit()


    def delete_course(self, db, course):
        db.delete(course)
        db.commit()
    
