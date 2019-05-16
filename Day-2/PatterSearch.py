import sys,re
def prompt_delete(i,o):
    with open(i, "r",newline='\n') as input:
        with open(o, "w",newline='\n') as output: 
            for line in input:
                    pattern = '((\s?)|(\s+))prompt(\s+)'
                    result=re.search(pattern,line.strip("\n"),re.IGNORECASE)
                    if result:
                        print(result.group())
                    else:
                        output.write(line)
        output.close()
    input.close()


InputFileName=sys.argv[1]
OutputFileName=sys.argv[2]
prompt_delete(InputFileName,OutputFileName)
