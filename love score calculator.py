def calculate_love_score():
    name1=input("whats your name?\n")
    name2=input("whats your companion's name?\n")
    combined_names=name1+name2
    lower_names=combined_names.lower()
    t=lower_names.count("t")
    r=lower_names.count("r")
    u=lower_names.count("u")
    e=lower_names.count("e")
    s1=t+r+u+e
    l=lower_names.count("l")
    o=lower_names.count("o")
    v=lower_names.count("v")
    s2=l+o+v+e
    love_score=str(s1)+str(s2)
    print(love_score)
calculate_love_score()
