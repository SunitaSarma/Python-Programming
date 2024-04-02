# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 21:57:54 2024

@author: sarma
"""

tasks = []

def add_task(task):
    tasks.append(task)
    print("Task added successfully.")

def view_tasks():
    if tasks:
        print("To-Do List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    else:
        print("No tasks found.")

def complete_task(index):
    if index >= 1 and index <= len(tasks):
        del tasks[index - 1]
        print("Task completed successfully.")
    else:
        print("Invalid task index.")

while True:
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        task = input("Enter task: ")
        add_task(task)
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        index = int(input("Enter task index to complete: "))
        complete_task(index)
    elif choice == '4':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please choose again.")