from .models import Student


def current_student(request):
    sid = request.session.get("student_id")
    student = Student.objects.filter(pk=sid).first() if sid else None
    return {"current_student": student}
