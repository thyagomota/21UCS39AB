# CS39AB - Cloud Computing - Summer 2021
# Instructor: Thyago Mota
# Description: Activity 29 - Computes the similarity score of two given sentences

from stemming.porter2 import stem
import re

def sentence_stem(s):
    s = re.sub(r'[^\w\s]', '', s)
    s = re.sub(r' +', ' ', s).lower()
    out = ''
    for w in s.split(' '):
        out += stem(w) + ' '
    return out.strip()

def compute(a, b):
    total = len(a.split(' '))
    common = 0
    for wb in b.split(' '):
        found = False
        for wa in a.split(' '):
            if wb == wa:
                found = True
                break
        if found:
            common += 1
        else:
            total += 1
    return common / total

# expects the following event structure:
# { 'sentences': [ a, b ] }
def lambda_handler(event, context):

    print(event)

    # check event structure
    if 'a' in event and 'b' in event:
        a = event['a']
        b = event['b']
        a = sentence_stem(a)
        b = sentence_stem(b)

        # return success
        return {
            'statusCode': 200,
            'body': str(compute(a, b))
        }
    else:
        return {
            'statusCode': 200,
            'body': 'NA'
        }

event = { 
    "a": "cheap electronic items", 
    "b": "discount electronics coupon"
}
print(lambda_handler(event, {}))
