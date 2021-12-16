from persistence.repositories.course_module_repository_postgres import CourseModuleRepositoryPostgres
from infrastructure.db.course_module_schema import CourseModule
from application.serializers.course_module_serializer import CourseModuleSerializer
from uuid import uuid4

cmorp = CourseModuleRepositoryPostgres()


def add_module(db, course_id, args):

    new_module = CourseModule(id=uuid4(), course_id=course_id, title=args.title, content=args.content)

    cmorp.add_module(db, new_module)
    return CourseModuleSerializer.serialize(new_module)
