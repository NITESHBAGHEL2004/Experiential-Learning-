
from django.shortcuts import render,redirect
from django.http import JsonResponse ,HttpResponse
from .models import academic_year,school, program, branch, semester, section, subject, faculty, pbl,PBLActivity


def get_schools(request, academic_year_id):
    try:
        schools = school.objects.filter(academic_year_id=academic_year_id).values('id', 'name')
        return JsonResponse(list(schools), safe=False)
    except Exception as e:
        print(f"Error in get_schools: {e}") 
        return JsonResponse({"error": "An error occurred while fetching schools."}, status=500)


def get_programs(request, school_id):
    try:
        programs = program.objects.filter(school_id=school_id).values('id', 'name')
        return JsonResponse(list(programs), safe=False)
    except Exception as e:
        print(f"Error in get_programs: {e}")  
        return JsonResponse({"error": "An error occurred while fetching programs."}, status=500)

def get_branches(request, program_id):
    try:
        branches = branch.objects.filter(program_id=program_id).values('id', 'name')
        return JsonResponse(list(branches), safe=False)
    except Exception as e:
        print(f"Error in get_branches: {e}")
        return JsonResponse({"error": "An error occurred while fetching branches."}, status=500)

def get_facultys(request, branch_id):
    try:
        facultys =faculty.objects.filter(branch_id=branch_id).values('id', 'name')
        return JsonResponse(list(facultys), safe=False)
    except Exception as e:
        print(f"Error in get_faculty: {e}")
        return JsonResponse({"error": "An error occurred while fetching faculty."}, status=500)


def get_semesters(request, faculty_id):
    try:
        semesters = semester.objects.filter(faculty_id=faculty_id).values('id', 'name')
        return JsonResponse(list(semesters), safe=False)
    except Exception as e:
        print(f"Error in get_faculty: {e}")
        return JsonResponse({"error": "An error occurred while fetching faculty."}, status=500)

def get_sections(request, semester_id):
    try:
        sections = section.objects.filter(semester_id=semester_id).values('id', 'name')
        return JsonResponse(list(sections), safe=False)
    except Exception as e:
        print(f"Error in get_sections: {e}")
        return JsonResponse({"error": "An error occurred while fetching sections."}, status=500)

def get_subjects(request, section_id):
    try:
        subjects = subject.objects.filter(section_id=section_id).values('id', 'name')
        return JsonResponse(list(subjects), safe=False)
    except Exception as e:
        print(f"Error in get_subjects: {e}")
        return JsonResponse({"error": "An error occurred while fetching subjects."}, status=500)

def get_pbls(request, subject_id):
    try:
        pbls = pbl.objects.filter().values('id', 'name')
        return JsonResponse(list(pbls), safe=False)
    except Exception as e:
        print(f"Error in get_pbls: {e}")
        return JsonResponse({"error": "An error occurred while fetching PBLs."}, status=500)



def dropdown_page(request):
    academic_years = academic_year.objects.all()
    
    if request.method == "POST":
        print(request.POST)
        
        lms_links = request.POST.getlist('lms_links') 
        l1, l2, l3, l4, l5 = (lms_links + [None] * 5)[:5]
        
        pbl_activity = PBLActivity(
            academic_year=academic_year.objects.get(id=request.POST.get('academic_year')).name if request.POST.get('academic_year') else None,
            school=school.objects.get(id=request.POST.get('school')).name if request.POST.get('school') else None,
            program=program.objects.get(id=request.POST.get('program')).name if request.POST.get('program') else None,
            branch=branch.objects.get(id=request.POST.get('branch')).name if request.POST.get('branch') else None,
            faculty=faculty.objects.get(id=request.POST.get('faculty')).name if request.POST.get('faculty') else None,
            semester=semester.objects.get(id=request.POST.get('semester')).name if request.POST.get('semester') else None,
            section=section.objects.get(id=request.POST.get('section')).name if request.POST.get('section') else None,
            subject=subject.objects.get(id=request.POST.get('subject')).name if request.POST.get('subject') else None,
            pbl=pbl.objects.get(id=request.POST.get('pbl')).name if request.POST.get('pbl') else None,
            description=request.POST.get('description'),
            activitydocument=request.FILES.get('activitydocument'),
            opening_date=request.POST.get('opening_date'),
            closing_date=request.POST.get('closing_date'),
            document_upload_1=request.FILES.get('document_upload_1'),
            document_upload_2=request.FILES.get('document_upload_2'),
            document_upload_3=request.FILES.get('document_upload_3'),
            lms_links1=l1,
            lms_links2=l2,
            lms_links3=l3,
            lms_links4=l4,
            lms_links5=l5,
            marks=request.POST.get('marks'),
            other_activity=request.POST.get('other-activity')
        )
        
        pbl_activity.save()
        
        messages.success(request, "Activity submitted successfully!")  # ✅ Add this
        return redirect('index')  # ✅ Messages work best after redirect
    
    return render(request, 'myapp/index.html', {'academic_years': academic_years})



#second part  edit part


from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from .models import academic_year, school, program, faculty, PBLActivity


from django.shortcuts import render, get_object_or_404
from .models import academic_year, school, program, faculty, PBLActivity

def pbl_activity_view(request):
    academic_years = academic_year.objects.all()
    schools = school.objects.all()
    programs = program.objects.all()
    facultys = faculty.objects.all()

    filtered_activities = None
    selected_academic_year = None
    selected_school = None
    selected_program = None
    selected_faculty = None

    if request.method == "POST":
        # Get selected IDs from form
        selected_academic_year_id = request.POST.get("academic_year")
        selected_school_id = request.POST.get("school")
        selected_program_id = request.POST.get("program")
        selected_faculty_id = request.POST.get("faculty")

        # Get full objects (or 404 if something went wrong)
        selected_academic_year = get_object_or_404(academic_year, id=selected_academic_year_id)
        selected_school = get_object_or_404(school, id=selected_school_id)
        selected_program = get_object_or_404(program, id=selected_program_id)
        selected_faculty = get_object_or_404(faculty, id=selected_faculty_id)

        # Now filter the activities using selected values
        filtered_activities = PBLActivity.objects.filter(
            academic_year=selected_academic_year,
            school=selected_school,
            program=selected_program,
            faculty=selected_faculty
        )

    context = {
        'academic_years': academic_years,
        'schools': schools,
        'programs': programs,
        'facultys': facultys,
        'filtered_activities': filtered_activities,
        'selected_academic_year_name': selected_academic_year.name if selected_academic_year else '',
        'selected_school_name': selected_school.name if selected_school else '',
        'selected_program_name': selected_program.name if selected_program else '',
        'selected_faculty_name': selected_faculty.name if selected_faculty else '',
    }

    return render(request, 'myapp/data.html', context)


@csrf_exempt
def update_activity(request):
    if request.method == 'POST':
        activity_id = request.POST.get('activity_id')
        activity = get_object_or_404(PBLActivity, id=activity_id)

        
        activity.pbl = request.POST.get('activity_name')
        activity.other_activity = request.POST.get('other_activity')
        activity.description = request.POST.get('description')
        activity.marks = request.POST.get('marks')

        if 'activitydocument' in request.FILES:
            activity.activitydocument = request.FILES['activitydocument']
        if 'document_upload_1' in request.FILES:
            activity.document_upload_1 = request.FILES['document_upload_1']
        if 'document_upload_2' in request.FILES:
            activity.document_upload_2 = request.FILES['document_upload_2']
        if 'document_upload_3' in request.FILES:
            activity.document_upload_3 = request.FILES['document_upload_3']

        # Save up to 5 LMS links
        lms_links = request.POST.getlist('lms_links')
        for i in range(5):
            field_name = f"lms_links{i+1}"
            setattr(activity, field_name, lms_links[i] if i < len(lms_links) else None)

        activity.save()
        messages.success(request, "Activity updated successfully.")
        return redirect('pbl_activity_view')

    return redirect('myapp/data.html')



#pert report
import csv

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import academic_year, school, program, faculty, PBLActivity
import csv


def pbl_activity(request):
    academic_years = academic_year.objects.all()
    schools = school.objects.all()
    programs = program.objects.all()
    facultys = faculty.objects.all()

    filtered_activities = None
    selected_academic_year = None
    selected_school = None
    selected_program = None
    selected_faculty = None

    if request.method == "POST":
        selected_academic_year_id = request.POST.get("academic_year")
        selected_school_id = request.POST.get("school")
        selected_program_id = request.POST.get("program")
        selected_faculty_id = request.POST.get("faculty")

        # Only fetch objects if all required IDs are provided
        if selected_academic_year_id and selected_school_id and selected_program_id and selected_faculty_id:
            try:
                selected_academic_year = academic_year.objects.get(id=selected_academic_year_id)
                selected_school = school.objects.get(id=selected_school_id)
                selected_program = program.objects.get(id=selected_program_id)
                selected_faculty = faculty.objects.get(id=selected_faculty_id)

                filtered_activities = PBLActivity.objects.filter(
                    academic_year=selected_academic_year,
                    school=selected_school,
                    program=selected_program,
                    faculty=selected_faculty
                )
            except academic_year.DoesNotExist:
                print("Invalid academic_year ID:", selected_academic_year_id)
            except school.DoesNotExist:
                print("Invalid school ID:", selected_school_id)
            except program.DoesNotExist:
                print("Invalid program ID:", selected_program_id)
            except faculty.DoesNotExist:
                print("Invalid faculty ID:", selected_faculty_id)

    # Handle CSV download request
    if request.method == "POST" and 'download_csv' in request.GET and filtered_activities:
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="Experiential_Learning_Report.csv"'
        writer = csv.writer(response)

        # Write headers
        writer.writerow([
            'Activity_Name', 'Other_Activity', 'Description', 'Activity Opening Date',
            'Activity Closing Date', 'Activity Document', 'Marks', 'Document Upload 1',
            'Document Upload 2', 'Document Upload 3', 'LMS Links 1', 'LMS Links 2',
            'LMS Links 3', 'LMS Links 4', 'LMS Links 5'
        ])

        # Write the filtered activities data
        for activity in filtered_activities:
            writer.writerow([
                getattr(activity, 'subject', ''),
                activity.pbl, activity.other_activity, activity.description,
                activity.opening_date, activity.closing_date,
                activity.activitydocument, activity.marks,
                activity.document_upload_1, activity.document_upload_2,
                activity.document_upload_3, activity.lms_links1,
                activity.lms_links2, activity.lms_links3,
                getattr(activity, 'lms_links4', ''), getattr(activity, 'lms_links5', '')
            ])
        return response

    return render(request, 'myapp/report.html', {
        'academic_years': academic_years,
        'schools': schools,
        'programs': programs,
        'facultys': facultys,
        'filtered_activities': filtered_activities,
        'selected_academic_year_name': selected_academic_year.name if selected_academic_year else '',
        'selected_school_name': selected_school.name if selected_school else '',
        'selected_program_name': selected_program.name if selected_program else '',
        'selected_faculty_name': selected_faculty.name if selected_faculty else '',
    })