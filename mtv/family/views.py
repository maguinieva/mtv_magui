from django.shortcuts import render

from family.models import Family_member


def fun_create_family_member(request, name: str, last_name: str, age: int, relationship: str):

    member = Family_member(name=name, last_name=last_name, age=age, relationship=relationship)
    member.save()

    context_dict = {'member': member}
    return render(
        request=request,
        context=context_dict,
        template_name='family/create_family_member.html',
    )

def fun_show_family_members(request):
    
    members = Family_member.objects.all()

    context_dict = {'members': members}

    return render(
        request=request,
        context=context_dict,
        template_name='family/list_family_members.html',
    )