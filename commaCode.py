def and_join(spam):
    if not isinstance(spam, list): raise ValueError('List expected')# this will run is a list is not passed
    if not spam: return None# is they is no list None will be returned
    if len(spam) == 1: return spam[0] # if the is only one item in the list that item will be returned

    temp = list(spam)# makes temp to be a list of spam
    temp[-1] = 'and ' + temp[-1] #the last item will be equal to the last and plus the last item
    return ','.join(temp)# joins the comma to temp


spam =['apples', 'bananas', 'tofu', 'cats']
who = [1, 2, 3, 4, 5]
print(and_join(spam))
#print(and_join(who))

def lst_to_str(lst):# this defines the function
    output = ''
    for i in lst[:-1]: #this will slice the list


        output += i + ', ' # this adds items to the output variable

    return output + 'and ' + lst[-1] # once output has been established and the last value of the list is added to the output

spam = ['apple', 'banana', 'egg']
who = [1, 2, 3, 4, 5]
print(lst_to_str(spam))
#print(lst_to_str(who))

# this method does not give the desired result
def cCode(list): # this defines the function cCode
    last = ' and ' + str(list[-1]) # here and concatenation the result it gives is and Martha
    return str(list[:-1])[1:-1] + last # what is return here is for str(list[:-1]) will give lisah has the slice which will look like this '['Lisah']' then [1:-1] comes in to remove....
    #....... the square brakets

list = ['Lisah', 'Martha']
print(cCode(list))
