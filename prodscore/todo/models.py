from django.db import models


class Task(models.Model):

    NEW = 'NW'
    INPROGRESS = "IP"
    BLOCKED = "BK"
    DONE = "CP"

    STATUS_CHOICES = (
            (NEW, 'New'),
            (INPROGRESS, 'In Progress'),
            (BLOCKED, 'BK'),
            (DONE, 'Done')
        )

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    value = models.PositiveIntegerField(default=1)
    created_date = models.DateTimeField(auto_now_add=True)
    closed_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=2,
                              choices=STATUS_CHOICES,
                              default=NEW)

    def is_complete(self):
        return self.status in (self.DONE)

    def __unicode__(self):
        return self.title
