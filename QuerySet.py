entry.objects.filter(body__text__contains="Music").filter(pub_date__year__gte=2010)
entry.objects.filter(pub_date__month=4)
entry.objects.filter(blog__name = "Technology")
entry.objects.all()[:10]
entry.objects.filter(blog__name = "Art").filter(number_of_comments__gte=15)