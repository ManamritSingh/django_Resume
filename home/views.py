from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    #return HttpResponse("Lets see if this can work")
    return render(request, 'Resume.html')


def cv_view(request):
    context = {
        'name': 'Manamrit Singh',
        'phone': '+1 (914) 240 3805',
        'email': 'ms16006@nyu.edu',
        'location': 'Brooklyn, NY',
        'linkedin': 'https://www.linkedin.com/in/manamritsingh/',
        'education_list': [
            {'degree': 'MS Computer Science', 'school': 'New York University', 'graduation_year': 'Expected 2026'},
            {'degree': 'B.E. Computer Engineering', 'school': 'Thapar Inst. of Engineering and Technology', 'graduation_year': '2024'}
        ],
        'skill_list': {
            'Technical Skills': ['Python', 'Machine Learning', 'C++', 'NLP'],
            'Soft Skills': ['Problem Solver', 'Conflict Resolution', 'Adaptable'],
            'Misc Skills': ['Photography', 'Music']
        },
        'experience_list': [
            {
                'title': 'Software Engineer Intern',
                'company': 'Reliable Power Alternatives Corp',
                'location': 'Fort Lauderdale, FL',
                'start_date': 'Mar 2024',
                'end_date': 'Jun 2024',
                'responsibilities': [
                    'Automated an internal task reducing run times from 2+ hours to 30 seconds.',
                    'Saved approximately USD 100 on each run of the application.',
                    'Used Python, tkinter, Json Restful APIs, openpyxl, and pypdf.'
                ]
            }
        ],
        'project_list': [
            {
                'name': 'Facial Recognition App using Machine Learning',
                'description': 'An app for marking attendance in large classrooms using facial recognition.',
                'details': [
                    'Fine-tuned VGG model as per requirements.',
                    'Developed interactive mobile app with GPS spoof detection and Firebase Database using Flutter.'
                ]
            },
            {
                'name': 'Music Generation using AI and Genetic Algorithm',
                'description': 'A solution for EDM artists to generate music based on audio clips.',
                'details': [
                    'Takes an audio clip and produces a sound that is similar to the audio clip further used as part of the EDM track.',
                    'Used Siamese networks, Dance diffusion, and Genetic Algorithm to generate new sound tracks.'
                ]
            },
            {
                'name': 'Autonomous Path Detecting Vehicle',
                'description': 'This vehicle is capable of moving on a black line and avoiding obstacles.',
                'details': [
                    'Senses the stations and stops there for the desired period.',
                    'Included appropriate hardware selection and electronic design using CAD tool (EAGLE).'
                ]
            }
        ],
        'certification_list': [
            {'name': 'Fundamentals of TinyML – HarvardX', 'link': 'https://courses.edx.org/certificates/3e3e9e5435d64936b8e601e32f02b1e0'},
            {'name': 'Mastering Data Structures & Algorithms using C and C++', 'link': 'https://www.udemy.com/certificate/UC-421b6dfe-2048-425a-807b-59853629c958/'}
        ],
        'achievement_list': [
            {'description': 'Won USD 200 at TiEU App-a-thon Fall 2022', 'link': 'https://devpost.com/manamritsingh426'}
        ]
    }
    return render(request, 'cv_template.html', context)