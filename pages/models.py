from django.db import models

# Create your models here.
class Topic(models.Model):
    """A topic the user is lerning about."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        """Return a string repersentation of the model."""
        return self.text


class Entry(models.Model):
    """Something specific learned about a topic."""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        The Meta class holds the extra information for
        managing a model; here, it allows us to set special attribute
        telling Django to use Entries shen it need to refer to more than 
        one entry. Without this , Django would refer to multiple entries as 
        Entrys. 
        """
        verbose_name_plural = 'entries'

    def __str__(self):
        """Return the string repersentation of the model."""
        return f"{self.text[:50]}..."