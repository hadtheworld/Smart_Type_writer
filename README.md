"# Smart_type_writer"

This is an extension to the previous project of mine "Type Writer", Which you can visit on :- https://github.com/hadtheworld/TypeWriter

This project has following addtions:-
Now coming to this project:
I have integrated widespread ChatGPT AI from OpenAI with my type writer project using API calls, Now you can :
- Just type your question in the text area provided.
- click "Yes" and wait for the UI window (using python tkinter) to get blur :- "answer is received and save in your input file"
- Place your cursor anywhere you want to type you answers in and press "Ctrl+y" (user defined short cut).
- The type writer will start typing the answer for you (no need to go to change window to Chat GPT for copy - pasting).

** Things to Remember **
- Run "Typer.py" file using "Python typer.py" to run the tool
- install "keyboard" module using "pip install keyboard" in CMD after installing python Interpreter.
- You will be needing your API key for the queries to run which you can get from below link after signing in :-
Get Key: - https://lnkd.in/dqBSmM-b
- Add you key in 'openai.api_key = "[key-given]" ' in file "chat_gpt_bot.py
"
- OpenAI doesn't allow it to leak keys on open platforms so keep in mind to not upload the key to GitHub or host anywhere otherwise the key will get changed.
- You will be needing Python interpreter to run the tool which you can download from :- https://lnkd.in/d4BXWaPB


**Detailed Explaantion of the code**

**Starting with the first file, typer.py:**

 - The keyboard module is imported, which is used to detect keyboard events.
 - The tkinter module is imported and aliased as tk, which is used to create the GUI.
 - The chat_gpt_bot module is imported, which contains the code for communicating with the OpenAI GPT-3.5 language model.
 - A class named check_box is defined. This class is responsible for creating the GUI and detecting user input.
 - An empty list named rec is defined as a class variable.
 - The __init__ method is defined, which is called when an instance of the check_box class is created. It sets up the GUI by creating a tkinter window, canvas, entry box, text box, and buttons.
 - The CheckBox method is defined, which runs the main event loop of the tkinter window.
 - The make_chat method is defined, which takes user input from the text box, sends it to the chat function in the chat_gpt_bot module, and writes the response to a file using the TypeWriter class.
 - The execute method is defined, which is called when the "YES" button is pressed. It gets the user input from the entry box, calls the make_chat method, and starts a loop to detect keyboard events. If the user presses the "ctrl+y" key, it calls the write method of the TypeWriter class to simulate typing the text from the file. If the user presses the "ctrl+k" key, it returns and stops the loop.
 - A class named TypeWriter is defined, which is responsible for writing text to the keyboard.
 - The __init__ method is defined, which takes a parameter b and sets it as the file number.
 - The file_write method is defined, which takes a parameter content and writes it to a file named input[file_number].txt.
 - The write method is defined, which reads the content of the file created by the file_write method and uses the keyboard module to simulate typing the text.


**Moving on to the chat_gpt_bot.py file:**

 - The OpenAI API key is set using the openai module.
 - The chat function is defined, which takes a parameter inp and uses the OpenAI API to communicate with the GPT-3.5 language model. It sends a message to the model with the user input, and returns the response from the model.
**In summary, the typer.py file creates a GUI that allows the user to input text and receive responses from the GPT-3.5 language model. When the user presses the "YES" button, the text is sent to the model and the response is written to a file. When the user presses the "ctrl+y" key, the text from the file is simulated as typing on the keyboard.**
