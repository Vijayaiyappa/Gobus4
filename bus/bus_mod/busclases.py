from datetime import datetime

class busmod:
    @staticmethod
    def convertime(time12hr):
        t=datetime.strptime(time12hr,'%I:%M %p')
        return (t.time())
       

