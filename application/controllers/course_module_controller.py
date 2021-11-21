from application.use_cases.course_module import (create, get, delete, update)

class CourseModuleController:

    @classmethod
    def create_module(self, db, args):

        return create.add_module(db, args)


    @classmethod
    def get_module(self, db, module_id):

        return get.get_module(db, module_id)


    @classmethod
    def delete_module(self, db, module_id):

        return delete.delete_module(db, module_id)


    @classmethod
    def update_module(self, db, module_id, update_args):

        return update.update_module(db, module_id, update_args)