from tasks import TaskList, Task

tasks = TaskList()

tasks.addtask(Task("Task 1", "Description 1", 1, True))
tasks.addtask(Task("Task 2", "Description 2", 2, False))
tasks.addtask(Task("Task 3", "Description 3", 3, True))
tasks.addtask(Task("Task 4", "Description 4", 4, False))
tasks.addtask(Task("Task 5", "Description 5", 5, True))

tasks.displaytasks_by_status(True)
tasks.displaytasks_by_status(False)
tasks.displaytasks()
print("*** Total tasks: ", tasks.counttasks())
print("*** Ready tasks: ", tasks.counttasks(status="Ready"))
print("*** Not Ready tasks: ", tasks.counttasks(status="Not Ready"))

tasks.removetask("Task 1")
tasks.removetask("Task 3")

tasks.displaytasks()

tasks.addtask(Task("Task 6", "Description 6", 6, False))
tasks.addtask(Task("Task 7", "Description 7", 7, False))
tasks.addtask(Task("Task 8", "Description 8", 8, False))
tasks.addtask(Task("Task 9", "Description 9", 9, False))

print("*** Total tasks: ", tasks.counttasks())
print("*** Ready tasks: ", tasks.counttasks(status="Ready"))
print("*** Not Ready tasks: ", tasks.counttasks(status="Not Ready"))

from store import Store, Item
print("\n\n*** Store ***")
test = Store("Test Store", "123 Main St")
test.additem(Item("Oranges", 10))
test.additem(Item("Apples", 20))
test.additem(Item("Bananas", 30))
test.displayitems()
print(test.countitems())
test.removeitem("Oranges")
test.displayitems()
print(test.countitems())




