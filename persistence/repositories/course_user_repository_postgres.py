from infrastructure.db.course_user_schema import CourseUser
from sqlalchemy import func
import logging

logger = logging.getLogger(__name__)

class CourseUserRepositoryPostgres():

    def add_course_user(self, db, payload):
        db.add(payload)
        db.commit()
        logger.info("Added new user in course %s", payload.course_id)
        logger.debug("ID of the new user: %s", payload.id)


    def get_all_course_users(self, db, course_id, user_type):
        query = db.query(CourseUser).filter(CourseUser.course_id == course_id)
        if user_type != None:
            logger.debug("Get users of course %s with filter user_type %s",
                        course_id, user_type)
            query = query.filter(CourseUser.user_type == user_type.lower())
        
        users_list = query.all()
        logger.debug("Getting all users of course %s", course_id)
        return users_list


    def get_all_user_courses(self, db, user_id, approval_state, user_type):
        query = db.query(CourseUser).filter(CourseUser.user_id == user_id)
        if approval_state != None:
            logger.debug("Get courses of user %s with filter approval_state %s",
                        user_id, approval_state)
            query = query.filter(CourseUser.approval_state == approval_state)

        if user_type != None:
            logger.debug("Get courses of user %s with filter user_type %s",
                        user_id, user_type)
            query = query.filter(CourseUser.user_type == user_type.lower())
            
        user_courses_list = query.all()
        logger.debug("Getting all courses of user %s", user_id)
        return user_courses_list


    def get_course_user(self, db, course_id, user_id):
        user = db.query(CourseUser).filter(CourseUser.course_id == course_id).\
                        filter(CourseUser.user_id == user_id).first()
        return user


    def get_course_metrics(self, db, course_id):
        partial_query = db.query(CourseUser).filter(CourseUser.course_id == course_id)
        if partial_query == None:
            total_users_in_course = 0
            users_approved = 0
            users_currently_in_course = 0
        else:
            total_users_in_course = partial_query.count()
            users_approved = partial_query.filter(CourseUser.approval_state == True).count()
            users_currently_in_course = partial_query.filter(CourseUser.approval_state == False).count()
        logger.debug("Getting metrics of course %s", course_id)
        return {
            "total_users": total_users_in_course,
            "users_approved": users_approved,
            "users_currently_studying": users_currently_in_course
        }



    def update_course_user(self, db):
        db.commit()
        

    def delete_course_user(self, db, user):
        db.delete(user)
        db.commit()
        logger.debug("Delete user %s", user.id)
        logger.info("User deleted")
