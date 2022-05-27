from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from datetime import datetime, timedelta

from mgmt.models import Fine, IssuedBook

# Create your views here.

def calculateFine(issue):
    today = datetime.today().date()

    if today > issue.expiry_date:
        diff = today - issue.expiry_date
        fine,created = Fine.objects.get_or_create(issue=issue,student=issue.student, amount=diff)
        fine.save()
        return diff
    else:
        return False



@login_required(login_url='/login')
def return_book(request,issueID):
    issue=IssuedBook.objects.get(id=issueID)
    amount = calculateFine(issue)
    return HttpResponse(f"fine amount:{amount}")


