import twitter
 
api = twitter.Api()
statuses = api.GetUserTimeline('Ry_iw')
for s in statuses:
    if s.text[0] != '@':
        print s.text , "|" , s.created_at