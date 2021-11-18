from infrastructure.db.course_user_schema import CourseUser
from sqlalchemy import func

class CourseUserRepositoryPostgres():

    def add_course_user(self, db, payload):
        db.add(payload)
        db.commit()


    def get_all_course_users(self, db, course_id, user_type):
        query = db.query(CourseUser).filter(CourseUser.course_id == course_id)
        if user_type != None:
            query = query.filter(CourseUser.user_type == user_type.lower())
        
        users_list = query.all()
        return users_list


    def get_all_user_courses(self, db, user_id, aprobal_state, user_type):
        query = db.query(CourseUser).filter(CourseUser.user_id == user_id)
        if aprobal_state != None:
            query = query.filter(CourseUser.aprobal_state == aprobal_state)

        if user_type != None:
            query = query.filter(CourseUser.user_type == user_type)
            
        user_courses_list = query.all()
        return user_courses_list


    def get_course_user(self, db, course_id, user_id):
        user = db.query(CourseUser).filter(CourseUser.course_id == course_id).\
                        filter(CourseUser.user_id == user_id).first()
        return user


    def update_course_user(self, db):
        db.commit()
        

    def delete_course_user(self, db, user):
        db.delete(user)
        db.commit()
