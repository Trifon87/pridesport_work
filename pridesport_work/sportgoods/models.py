# from django.db import models
#
#
# class Gear(models.Model):
#     FIGHT = 'fight'
#     FITNESS = 'fitness'
#     CLOTHING = 'clothing'
#     UN = 'unknown'
#     SPORT_TYPES = (
#         (FIGHT, "fight"),
#         (FITNESS, "fitness"),
#         (CLOTHING, 'clothing'),
#         (UN, 'Unknown')
#     )
#     type = models.CharField(max_length=35, choices=SPORT_TYPES, default=UN)
#     name = models.CharField(max_length= 35, blank=False)
#     price = models.FloatField(blank=False)
#     description = models.TextField(blank=True)
#     image_url = models.ImageField(
#         upload_to='gear',
#     )
#
#     def __str__(self):
#         return self.name
#
#
# # class Like(models.Model):
# #     gear = models.ForeignKey(Gear, on_delete= models.CASCADE)
# #     # test = models.CharField(str=())
#
#
# class Comment(models.Model):
#     gear = models.ForeignKey(Gear, on_delete=models.CASCADE)
#     text = models.TextField(blank=False)