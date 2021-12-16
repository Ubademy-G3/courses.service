from persistence.repositories.course_repository_postgres import CourseRepositoryPostgres
from infrastructure.db.course_schema import Course
from application.serializers.course_serializer import CourseSerializer
from uuid import uuid4

crp = CourseRepositoryPostgres()


def add_course(db, args):

    new_course = Course(
        id=uuid4(),
        name=args.name,
        description=args.description,
        category=args.category,
        subscription_type=args.subscription_type,
        location=args.location,
        profile_picture=args.profile_picture,
        duration=args.duration,
        language=args.language,
        level=args.level,
        total_exams=args.total_exams
    )

    crp.add_course(db, new_course)
    return CourseSerializer.serialize(new_course)
