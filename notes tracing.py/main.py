#Avery bowman

#What is tracing?
    #Degbugging method that lets you find any bugs and improve your code
#python -m trace --trace C:\Users\avery.bowman\.vscode\CP2-Projects\notes tracing.py
"""
--trace (displays function lines as they are executed)
--count
--listfuncs (displays the function in the project...)
--trackcalls (displays relationships between the functions)
"""
import trace
import sys

tracer = trace.Trace(count=False, trace=True)
def trace_calls(frame, event, arg):
    if event == 'call':
        print(f'calling functions: (frame.f_code.co_name)')
    elif event == 'line':
        print(f'Executing line: {frame.f_lineno} in (frame.f_code.co_name)')
    elif event == 'return':
        print(f'{frame.f_code.co_name} returned {arg}')
    elif event == 'exception':
        print(f'Exception in {frame.f_code.co_name}: {arg}')
        return trace_calls
    
sys.settrace(trace_calls)
"""
Event types:
call - when the function is called
line - when a new line is executed
return - when the function returns a value
exception - when there is an exception raised
"""

#What are some ways we can debug by tracing?
    #Make a function that lets us see how our functions are interacting and running

#How do you access the debugger in vs code?
    #F5

#What is testing?
    #Going though the code trying to break it, have testers be not the person who wrote the code

#What are boundary conditions?
    #User conditions that are strange and/or likely to cause issues
    #You can check this one by your self
age = 18
if age >= 18:
    print("You can vote")
elif age >= 16:
    print("You can drive")
elif age >= 15:
    print("You can get your learners permit")
elif age >= 5:
    print("You can go to school")
else:
    print("To young for everything")

#How do you handle when users give strange inputs?
    #You can use a conditional, try and accept and then make sure you loop back to the question

def add(num_one, num_two):
    print(num_one, num_two)
    return num_one + num_two

def sub(num_one, num_two):
    return num_one - num_two

print(add(5,4))
print(sub(5,4))

tracer.run('sub')
