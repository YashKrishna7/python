words=['apple','banana','apple','orange','banana','apple']
count={item:words.count(item) for item in list(words)}
print(count)