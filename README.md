# Problem

Write a function that takes a big message and splits it into minimum number of smaller messages adhering to given limit. While splitting the function should not split a word into two messages. In the output messages please add tag ( x/y ). The total length (including the tag) should not exceed 160.

## Each chunk:

up to 160 characters long
no word should be split in the middle
each chunk has to have its order suffixed in the form of ' (k/n)', e.g. "this is the first chunk (1/2)", "this is the second chunk (2/2)"
if the text provided to the function is less than 160 characters, no ordering should be suffixed