from sqlalchemy import func
from infrastructure.db.course_schema import Course

class CourseRepositoryPostgres():

    def add_course(self, db, payload):
        db.add(payload)
        db.commit()        


    def get_all_courses(self, db, category, subscription_type):

        partial_query = db.query(Course)
        if category == None and subscription_type == None:
            pass

        elif category != None and subscription_type == None:
            partial_query = partial_query.filter(Course.category in category)

        elif category == None and subscription_type != None:
            partial_query = partial_query.filter(Course.subscription_type in subscription_type)
       
        else:
            partial_query = partial_query.filter((Course.category in category) & 
                                                 (Course.subscription_type in subscription_type))

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
    
