from django import forms
from django.core.exceptions import ValidationError
from chats.models import Chat
from users.models import User
from message.models import Message
from members.models import Member

class ChatForm(forms.Form):
    first_user_id = forms.IntegerField()
    second_user_id = forms.IntegerField()
    topic = forms.CharField()

    def clean_first_username(self):
        first = self.cleaned_data['first_user_id']
        try:
            User.objects.get(id=first)
        except User.DoesNotExist:
            self.add_error('first_user_id', 'User does not exist')
            # raise ValidationError('User does not exist', code='invalid')
        return first

    def clean_second_username(self):
        second = self.cleaned_data['second_user_id']
        try:
            User.objects.get(id=second)
        except User.DoesNotExist:
            self.add_error('second_user_id', 'User does not exist')
            # raise ValidationError('User does not exist', code='invalid')
        return second

    def clean(self):
        if not len(self.errors):
            first = self.cleaned_data['first_user_id']
            second = self.cleaned_data['second_user_id']
            topic = self.cleaned_data['topic']

            try:
                Chat.objects.get(topic=topic)
                self.add_error(None, 'Chat already exist')
            except Chat.DoesNotExist:
                pass

    def save(self):
        first = self.cleaned_data['first_user_id']
        second = self.cleaned_data['second_user_id']
        topic = self.cleaned_data['topic']

        first_user = User.objects.get(id=first)
        second_user = User.objects.get(id=second)

        new_chat = Chat.objects.create(
            topic=topic,
            is_group_chat=False
        )

        Member.objects.create(
            user=first_user,
            chat=new_chat,
            new_messages=0,
        )
        Member.objects.create(
            user=second_user,
            chat=new_chat,
            new_messages=0,
        )
        return new_chat.id


class SendMessageForm(forms.ModelForm):
    def clean(self):
        try:
            member = Member.objects.get(
                user=self.cleaned_data.get('user'),
                chat=self.cleaned_data.get('chat'),
            )
        except Member.DoesNotExist:
            self.add_error('user', 'Forbidden. Member does not exist')

    def save(self):
        message = Message.objects.create(
            chat = self.cleaned_data.get('chat'),
            user = self.cleaned_data.get('user'),
            content = self.cleaned_data.get('content'),
        )
        return message.id

    class Meta:
        model = Message
        fields = ['chat', 'user', 'content']
