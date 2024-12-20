from datetime import  datetime,timedelta

class Task:
    def __init__(self, name="", description="", deadline = None,status=False):
        self.name = name
        self.description = description
        if deadline is not None:
            self.enddate = datetime.now()+timedelta(days=deadline)
        else:
            self.enddate = None
        self.status = status

    def __str__(self):
        return f"Name: {self.name}\nDescription: {self.description}\nDeadline: {self.enddate.strftime('%Y-%m-%d')}\nStatus: {self.status}"

    def isready(self):
        return self.status

    def markdone(self):
        self.status = True

    def markundone(self):
        self.status = False

    def setenddate(self, deadline):
        self.enddate = datetime.now()+timedelta(days=deadline)


class TaskList:
    def __init__(self):
        self.tasks = []

    def addtask(self, task):
        self.tasks.append(task)

    def removetask(self, taskname):
        for task in self.tasks:
            if task.name == taskname:
                self.tasks.remove(task)
                break


    def displaytasks_by_status(self, status=False):
        for task in self.tasks:
            if task.isready() == status:
                print(task)

    def displaytasks(self):
        for task in self.tasks:
            print(task)

    def counttasks(self):
        return len(self.tasks)

