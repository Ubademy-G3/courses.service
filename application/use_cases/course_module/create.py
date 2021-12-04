from persistence.repositories.course_module_repository_postgres import CourseModuleRepositoryPostgres
from infrastructure.db.course_module_schema import CourseModule
from application.serializers.course_module_serializer import CourseModuleSerializer
from uuid import uuid4

cmorp = CourseModuleRepositoryPostgres()

def add_module(db, args):

    new_module = CourseModule(
        id = uuid4(),
        title = args.title,
        media_id = args.media_id,
        content = args.content
    )

    cmorp.add_module(db, new_module)
    return CourseModuleSerializer.serialize(new_module)