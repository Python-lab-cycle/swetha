print("print leap year between two given years")
print("enter start year")
startYear=int(input())
print("enter last year")
endYear=int(input())
print("list of leap year:")
for year in range(startYear, endYear):
 if((year%4==0)and(year%100!=0)or(year%400==0)):
  print(year)
