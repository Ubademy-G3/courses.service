from application.use_cases.course_category import (create, get, delete)

class CourseCategoryController:

    @classmethod
    def create_category(self, db, args):
        
        return create.add_course_category(db, args)

    
    @classmethod
    def get_course_category(self, db, category_id):

        return get.get_course_category(db, category_id)


    @classmethod
    def get_all_course_categories(self, db):

        return get.get_all_categories(db)


    @classmethod
    def delete_course_category(self, db, category_id):

        return delete.delete_course_category(db, category_id)