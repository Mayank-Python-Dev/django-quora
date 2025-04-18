import uuid, textwrap
from django.db import models
from django.contrib.auth.models import User

"""
Note : 

1. models.CASCADE: If the Post is deleted, all Comment objects related to that Post will also be deleted automatically.

2. models.PROTECT: If the Post has any related Comment objects, you will not be able to delete the Post without first deleting the related comments.

3. models.SET_NULL: If the Post is deleted, the post field in all related Comment objects will be set to NULL. (This requires null=True on the post field.)

4. models.SET_DEFAULT: If the Post is deleted, the post field in all related Comment objects will be set to its default value (if specified).

5. models.SET(): You can provide a callable or value to set the post field to when the Post is deleted (e.g., you could set it to a default Post or another value).

6. models.DO_NOTHING: Django won’t take any action when the Post is deleted. It’s your responsibility to handle the deletion behavior manually, e.g., by using Django signals or custom logic.

"""

# Create your models here.

class BaseModel(models.Model):
    uid = models.UUIDField(default = uuid.uuid4, editable = False, blank = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Question(BaseModel):
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "question")
    question = models.TextField(blank = True, null = False, help_text = "Write the main content of the post here.")

    class Meta:
        verbose_name_plural = "Questions"
    
    def __str__(self):
        return "{} - {}".format(self.author.username, textwrap.shorten(self.question, width=25, placeholder="..."))

    
class Answer(BaseModel):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name = "answer")
    user = models.ForeignKey(User, on_delete = models.CASCADE,related_name = "user")
    answer = models.TextField(blank = True, null = False, help_text = "Write the answer to main content of the post..")
    likes = models.ManyToManyField(User, related_name = "likes")

    class Meta:
        verbose_name_plural = "Answers"
    
    def __str__(self):
        return "{} - {}".format(textwrap.shorten(self.question.question, width=25, placeholder="..."),textwrap.shorten(self.answer, width=25, placeholder="..."))


