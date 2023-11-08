from django.shortcuts import render,get_object_or_404 , redirect
import datetime

from conversation.forms import ConversationMessageForm
from .models import Item  , Conversation , ConversationMessage
# from .forms import NewItemForm , EditItemForm
from django.contrib.auth.decorators import login_required

from django.db.models import Q
# Create your views here.


@login_required
def convo(request , item_pk):
    item = get_object_or_404(Item , pk=item_pk)
    form = ConversationMessageForm()

    if item.created_by == request.user:
        return redirect('dashboard:index')

    conversations = Conversation.objects.filter(item=item).filter(members__in=[request.user.id]) #all convos realted with the item where user is a part of

    if conversations.exists():
        first_conversation = conversations.first()
        if first_conversation:
            return redirect('conversation:detail', pk=first_conversation.id)
        
    if request.method== 'POST':
        form = ConversationMessageForm(request.POST)


        if form.is_valid():
            conversation = Conversation.objects.create(item = item)
            conversation.members.add( request.user , item.created_by)
            # conversation.modified_at = currentTime
            conversation.save()

            # conversation_msg = ConversationMessage.objects.create(conversation = conversation)
            conversation_msg = form.save(commit=False)
            conversation_msg.conversation = conversation
            conversation_msg.created_by = request.user
            conversation_msg.save()

            return redirect('item:detail' , pk = item_pk)
        else:
            form = ConversationMessageForm()

    return render(request , 'conversation/new.html', {
        'form' : form
    })

@login_required
def inbox(request):
    conversations = Conversation.objects.filter(members__in=[request.user.id]) #all convos realted with the item where user is a part of

    return render(request , 'conversation/inbox.html', {
        'conversations' : conversations
    })


@login_required
def detail(request , pk):
    conversation = Conversation.objects.filter(members__in=[request.user.id]).get(pk=pk)
    form = ConversationMessageForm()

    if request.method== 'POST':
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            conversation.save()
            return redirect('conversation/detail.html' , pk= pk)
        else:
            form = ConversationMessageForm()


    return render(request , 'conversation/detail.html', {
        'conversation' : conversation,
        'form' : form,
    })
    
