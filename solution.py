string = "The South Lake Union Streetcar is a streetcar route in Seattle, Washington, United States. Traveling 1.3 miles (2.1 km), it connects downtown to the South Lake Union neighborhood on Westlake Avenue, Terry Avenue, and Valley Street. It was the first modern Seattle Streetcar line, beginning service on December 12, 2007, two years after a separate heritage streetcar ceased operations. It was conceived as part of the redevelopment of South Lake Union into a technology hub, with lobbying and financial support from Paul Allen."
limit = 160

def util(string, limit, annotation_len):
    words = string.split(' ')
    output = []
    output.append('')
    idx = 0
    while idx < len(words):
        if output[-1] == '' :
            output[-1] += words[idx]
        elif len(output[-1] + ' ' + words[idx]) + annotation_len <= limit:
            output[-1] += ' ' + words[idx]
        else:
            output.append('')
            idx -= 1
        idx += 1
    return output

def addTags(output):
    length = len(output)
    for i in range(length):
        output[i] += f' ({i + 1}/{length})'
    return output

def function(string, limit):
    annotation_len = 6
    digit = 1
    while True:
        annotation_len += 1
        output = util(string, limit, annotation_len)
        # this if statement checks if the length of the output is on the same level of digits as the presumed length
        # e.g. we first assume that the total length is 1 digit, which means that we assume the output should be 1~9
        # messages long. If this is not satisfied, then we redo it by adding the presumed number of digits by one and
        # see if it fits.
        if digit * 10 > len(output):
            return addTags(output)

output = (function(string, limit))
for line in output:
    print(line)