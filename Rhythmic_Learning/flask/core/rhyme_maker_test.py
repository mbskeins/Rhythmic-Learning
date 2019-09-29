import rhyme_maker_local
import word_prediction_local

def clean_print(lines):
    i = 1
    for line in lines:
        print(str(i)+ ": " + str(line))
        i += 1

rap = rhyme_maker_local.rhyme_it("Facebook")
clean_print(rap)