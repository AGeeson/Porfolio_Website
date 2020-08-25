from django.shortcuts import render, redirect
from .forms import ContactForm, ContactForm2
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect


"""def index(request):
    name=''
    email=''
    comment=''

    form=ContactForm(request.POST or None)
    if form.is_valid():
        name=form.cleaned_data.get("name")
        emaail=form.cleaned_data.get("email")
        comment=form.cleaned_data.get("comment")
        subject="A Visitor's Form"

        comment=name + "with the email," + email + ", sent the following message:\n\n" + comment;
        send_mail(subject, comment, 'alexanderwgeeson@gmail.com', [email])

        context={'form':form}

        return render(request, 'index.html', context)

    else:
        context={'form':form}
        return render(request, 'index.html', context)


from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm"""

def index(request):
    if request.method == 'GET':
        form = ContactForm2()
    else:
        form = ContactForm2(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, email, ['alexanderwgeeson@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "index.html", {'form': form})

def successView(request):
    return render(request, 'success.html')