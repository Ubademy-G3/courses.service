from infrastructure.db.course_module_schema import CourseModule
from sqlalchemy import func

class CourseModuleRepositoryPostgres():

    def add_module(self, db, payload):
        db.add(payload)
        db.commit()


    def get_module(self, db, module_id):
        module = db.query(CourseModule).filter(CourseModule.id == module_id).first()
        return module

    
    def delete_module(self, db, module):
        db.delete(module)
        db.commit()


    def update_module(self, db):
        db.commit()