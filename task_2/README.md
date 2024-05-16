Ось список команд, які підтримує цей програмний бот:

add [ім'я] [телефон]: Додає новий контакт з вказаним ім'ям та телефонним номером або додає телефонний номер до вже існуючого контакту.

change [ім'я] [старий телефон] [новий телефон]: Змінює телефонний номер для вказаного контакту зі старого на новий.

phone [ім'я]: Показує всі телефонні номери для вказаного контакту.

all: Показує всі контакти в адресній книзі.

add-birthday [ім'я] [дата народження]: Додає дату народження для вказаного контакту.

show-birthday [ім'я]: Показує дату народження для вказаного контакту.

birthdays: Показує користувачів, яких потрібно привітати по днях наступного тижня.

hello: Отримати вітання від бота.

close або exit: Закрити програму.

Add Contacts: First, let's add some contacts with their phone numbers and birthdays.
View Contacts: Next, we'll view all contacts to verify they've been added correctly.
Show Birthday: We'll check the birthday of one of the contacts.
Upcoming Birthdays: Then, we'll check for upcoming birthdays to ensure the functionality works.
Invalid Command: Finally, we'll try an invalid command to see if the program handles it correctly.
Let's start:

Add Contacts:

Command: add John 1234567890
Command: add John 5555555555
Command: add-birthday John 05.12.1985
Command: add Jane 9876543210
Command: add-birthday Jane 12.05.1990
View Contacts:

Command: all
Expected Output:
Contact name: John, phones: 1234567890; 5555555555, birthday: 05.12.1985
Contact name: Jane, phones: 9876543210, birthday: 12.05.1990
Show Birthday:

Command: show-birthday John
Expected Output: John: 05.12.1985
Upcoming Birthdays:

Command: birthdays
Expected Output: 
John: 1985-12-05
Jane: 1990-05-12
Invalid Command:

Command: invalid-command
Expected Output: Invalid command.


Enter a command: hello
How can I help you?
Enter a command: add John 1234567890
Contact added.   
Enter a command: add John 5555555555
Contact updated. 
Enter a command: add-birthday John 05.12.1985
Birthday added.  
Enter a command: add Jane 9876543210
Contact added.   
Enter a command: add-birthday Jane 12.05.1990
Birthday added.
Enter a command: all
Contact name: John, phones: 1234567890; 5555555555, birthday: 05.12.1985
Contact name: Jane, phones: 9876543210, birthday: 12.05.1990
Enter a command: show-birthday John
John: 05.12.1985
Enter a command: birthdays
John: 1985-12-05
Jane: 1990-05-12
Enter a command: invalid-command
Invalid command.
Enter a command: close
Good bye!
