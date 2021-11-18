from infrastructure.db.course_category_schema import CourseCategory
from sqlalchemy import func

class CourseCategoryRepositoryPostgres():

    def add_course_category(self, db, payload):
        db.add(payload)
        db.commit()


    def get_course_category(self, db, category_id):
        category = db.query(CourseCategory).filter(CourseCategory.id == category_id).first()
        return category


    def get_all_categories(self, db):
        categories = db.query(CourseCategory).all()
        return categories


    def delete_course_category(self, db, category):
        db.delete(category)
        db.commit()