print('List_Comprehension'.center(75,'⭐'))

mult_lst = [[20,15,60,50],
          [40,20,36,98],
          [55,69,48,65]]

#creating list comprehension
lst_compre = [i for i in mult_lst ]
print('List Comprehension of a: {}'.format(lst_compre))
print('='*80)


#using conditional statement in list comprehensions:
lst_compre_even = [ j for i in mult_lst for j in i if j%2 ==0]
print('Even List compreshension using condtion: {}'.format(lst_compre_even))
print('='*80)

# nested list condition
lst_compre = [j for i in mult_lst for j in i]
print('Nested List Comprehension: {}'.format(lst_compre))
print('='*80)

#using funtion in list comprehension
def odd(n):
    if n%2==1:
        return True
    else:
        return False
lst_compre_odd = [ j for i in mult_lst for j in i if odd(j) == True]
print('List_comprehension of used odd function: {}'.format(lst_compre_odd))
print('='*80)
print('THE END'.center(75,'⭐'))