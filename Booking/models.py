from django.db import models
from django.conf import settings



# Create your models here.
class Appointment(models.Model):
    
    TIMESLOT_LIST = (
        (0, '09:00 – 09:30 AM'),
        (1, '10:00 – 10:30 AM'),
        (2, '11:00 – 11:30 AM'),
        (3, '12:00 – 12:30 PM'),
        (4, '01:00 – 01:30 PM'),
        (5, '14:00 – 14:30 PM'),
        (6, '15:00 – 15:30 PM'),
        (7, '16:00 – 16:30 PM'),
        (8, '17:00 – 17:30 PM'),
    )
    date = models.DateField()
    slot = models.IntegerField(choices=TIMESLOT_LIST)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    def __str__(self):
        return 'Time :{} , Slot: {} By : {}'.format(self.date, self.TIMESLOT_LIST[self.slot][1], self.user.username)
    
    @property
    def time(self):
        return self.TIMESLOT_LIST[self.timeslot][1]