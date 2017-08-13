# Python-Offline-Judge(POJ)

An offline judge app for python, working on Windows.

## User Guide - Part-I:

### How to Create a Problem Set
To create a problem set, you need to create a folder in /problems.

The folder should start exactly with 'Set'.

There should be a file named 'setinfo', containing one line, where records
the name of the problem set.

### How to Create a Problem
To create a problem, you need to create a folder under a problem set folder.

The folder should start exactly with 'Prob'

In the folder, there must be 2 files.

1.probinfo.

    * This file contains at least 4 lines.

    * The 1st line is the name of your problem.

    * The 2nd line should be like 'datagen true|false', which suggest whether
    the problem has a data generator.

    * The 3rd line should be like 'stdprog true|false', which suggets whether
    the problem has a standard program. We suggest there always be a standard
    program.
    
    * The 4th line is the id number of the problem.

2.probdescribe.
    This file contains the description to the problem.

    Typically, there are 5 parts of a description file.

    They are problem introduction, input format, output format, sample input
    and sample output.

If you don't have a data generator, then make sure there is a file named
'stdinput', which contains the input data.

If you have a data generator, name it 'datagen.py'

If you don't have a standard program, then make sure there is a file named
'stdoutput', which contains the output data.

If you have a standard program, name it 'stdprog.py'

If you have a data generator, make sure there is a standard program
