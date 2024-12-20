from datetime import  datetime,timedelta

class Task:
    def __init__(self, name="", description="", deadline = None,status=False, startdate=datetime.now().strftime("%Y-%m-%d")):
        self.name = name
        self.description = description
        self.startdate = datetime.strptime(startdate, "%Y-%m-%d")
        if deadline is not None:
            self.enddate = self.startdate + timedelta(days=deadline)
        else:
            self.enddate = None
        self.status = status


    def __str__(self):
        return f"Name: {self.name}\tDescription: {self.description}\tDeadline: {self.enddate.strftime('%Y-%m-%d')}\tStatus: {self.status}"

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
        print(f"+++ Task\n{task}\n+++ Added")

    def removetask(self, taskname):
        for task in self.tasks:
            if task.name == taskname:
                print(f"--- Task\n{task}\n--- Removed")
                self.tasks.remove(task)
                break


    def displaytasks_by_status(self, status=False):
        for task in self.tasks:
            if task.isready() == status:
                print(task)

    def displaytasks(self):
        print("Tasks:")
        for task in self.tasks:
            print(task)

    def counttasks(self,status = "All"):
        if status == "Ready":
            return len([task for task in self.tasks if task.isready()])
        elif status == "Not Ready":
            return len([task for task in self.tasks if not task.isready()])
        return len(self.tasks)

