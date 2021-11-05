from persistence.repositories.course_media_repository_postgres import CourseMediaRepositoryPostgres

cmrp = CourseMediaRepositoryPostgres()

async def delete_all_courses_media():
    return await cmrp.delete_all_courses_media()

async def delete_course_media(course_id, media_id):
    course_media = await cmrp.get_course_media(course_id, media_id)
    if not course_media:
        raise HTTPException(status_code=404, detail="Media not found")
    return await cmrp.delete_course_media(course_id, media_id)