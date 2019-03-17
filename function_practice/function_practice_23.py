def count(*strs):
    length = len(strs)
    for i in range(length):
        letter=0
        number=0
        space=0
        others=0
        for each in strs[i]:
            if each.isalpha()==True:
                letter+=1
            elif each.isdecimal()==True:
                number+=1
            elif each.isspace()==True:
                space+=1
            else:
                others+=1
        print('第',i+1,'个字符串里有',letter,'个英文字母',number,'个数字',space,'个空格',others,'个其他字符')
count('asgdv656  &^^%##$','zhgd&^%132  ','12&^&asd&^&  767')