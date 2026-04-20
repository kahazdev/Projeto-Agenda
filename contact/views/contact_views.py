from django.shortcuts import render, get_object_or_404, redirect
from contact.models import Contact
from django.db.models import Q
from django.core.paginator import Paginator
from django.http import Http404


def index(request):
    contacts = Contact.objects.filter(show=True).order_by("-id")

    paginator = Paginator(contacts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
        "Site_Title": 'Contatos - '
    }

    return render(
        request,
        "contact/index.html",
        context
    )


def search(request):
    search_value = request.GET.get('q', '').strip()

    if search_value == '':
        return redirect('contact:index')

    contacts = Contact.objects.filter(show=True).filter(
        Q(first_name__icontains=search_value) |
        Q(phone__icontains=search_value) |
        Q(email__icontains=search_value) |
        Q(last_name__icontains=search_value)).order_by("-id")

    paginator = Paginator(contacts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
        "Site_Title": 'Contatos - ',
        "search_value": search_value
    }

    return render(
        request,
        "contact/index.html",
        context
    )


def contact(request, contact_id):
    single_contact = get_object_or_404(
        Contact, pk=contact_id, show=True)

    site_title = f"{single_contact.first_name} {single_contact.last_name} - "

    if single_contact == None:
        raise Http404

    context = {
        "contact": single_contact,
        "Site_Title": site_title
    }

    return render(
        request,
        "contact/contact.html",
        context
    )
