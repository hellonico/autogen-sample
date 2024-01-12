# preparation

```bash
conda activate autogen
pip install litellm
litellm --model ollama/mistral   
litellm --model ollama/codellama
litellm --model ollama/llama2
```


# example

```
⋊> ~/n/a/autogen python writescript.py                                                                                                                  (autogen) 10:17:10
userproxy (to chat_manager):


Write a python scripts that count from 1 to 10, then get 'Assistant' to execute it.


--------------------------------------------------------------------------------
userproxy (to chat_manager):

 Here's a simple Python script that counts from 1 to 10:

```python
def count_from_one_to_ten():
    for i in range(1, 11):
        print(i)

count_from_one_to_ten()
```

To execute this script using an assistant like me or any other Python interpreter, follow these steps:

1. Save the script as a `.py` file (for example, name it "counter.py").
2. Open your terminal or command prompt and navigate to the directory where you saved the script.
3. Type `python counter.py` and press Enter. The script will run, and you'll see the numbers from 1 to 10 printed in the console.

If you want me to execute the code for you directly, here it is:

```python
def count_from_one_to_ten():
    for i in range(1, 11):
        print(i)

count_from_one_to_ten()
```

However, as a text-based AI, I don't have the ability to save files or execute them directly. You must run this code in your local Python interpreter.

If you need assistance with anything else or want me to help explain concepts, feel free to ask!

Continue.

--------------------------------------------------------------------------------

>>>>>>>> EXECUTING CODE BLOCK 0 (inferred language is python)...
execute_code was called without specifying a value for use_docker. Since the python docker package is not available, code will be run natively. Note: this fallback behavior is subject to change

>>>>>>>> EXECUTING CODE BLOCK 1 (inferred language is python)...
execute_code was called without specifying a value for use_docker. Since the python docker package is not available, code will be run natively. Note: this fallback behavior is subject to change
userproxy (to chat_manager):

exitcode: 0 (execution succeeded)
Code output: 
1
2
3
4
5
6
7
8
9
10

1
2
3
4
5
6
7
8
9
10

```