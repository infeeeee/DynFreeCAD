# Traceback is useful for finding bugs in the code. It's automatically installed with Dynamo. Use it in python nodes this way.

# ...
# Put here imports, global variables, inputs...
# ...

try:
    errorReport = None

    # ...
    # The code is here
    # ...

except:
    import traceback
    errorReport = traceback.format_exc()

if errorReport == None:
    # This will run if no error. 

    OUT = True

else:
    OUT = errorReport