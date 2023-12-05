**Product Mission**

For people who want to add several no specific destinations, the route design helper is an APP that can offer different choices (the highest-scoring route, the most time-saving route, the recently popular route …). Different from Google Maps which requires users to set specific destinations, this product allows users to input unspecified requests. For example, if the user wants to buy some drinks or water on his way home, this APP will offer one cheapest route(current location -> Target -> home), one fastest route(current location -> Dunkin -> home), and some other routes.

 

**User Stories**

As a student, I want to pick up some snacks on their way home. I am hungry so I prefer the shortest route.

A family goes out for dinner and plans to watch movies after dinner. They prefer to choose the highest-scoring Chinese restaurant or seafood restaurant. At the same time, they have to eat in one hour to avoid missing the start of the movie.

A man has to go to the BoA to cash a check, to one supermarket for food, to the florists to buy some roses, and back home to cook dinner. Since it is an anniversary, he wants high-quality roses. As for the other two destinations, he just wants to save time.

 

**Minimum Viable Product(MVP)**

A route design helper that can deal with one keyword requirement. After inputting all destinations, it will design the most time-saving route, the highest-scoring route, and so on. All destinations in one route are selected to fulfill one criterion.

However, this is still a huge project since you have to label countless address. Therefore, I break it into two smaller parts. The first part is getting the latitude and longitude of several places within one specific area by google map api. The second part is finding the k-nearest places(currently I set 3 weighting parameters: distance, cost and score) and returning corresponding nodes. With these two functions, the MVP can be realized once every place is labeled. 



**Demonstrate**

After exercising, I want to get some food and then I have to attend the class. I’d like to eat fried chicken. But the nearest KFC is still far away. Obviously, KFC is not a good choice.

![img](https://github.com/RussellOvO/EC601/edit/main/Project2/original.png)

With the route design helper, it will be different. After setting the destination, gym, fried chicken restaurant, and the classroom, the result can be McDonald’s since this is the cheapest route.

![img](https://github.com/RussellOvO/EC601/edit/main/Project2/cheapest.png)

 It also produces one route which contains BBQ chicken. That’s because BBQ Chicken is the highest-scoring restaurant in this area. ![img](https://github.com/RussellOvO/EC601/edit/main/Project2/best.png)

Besides, the university restaurant route which is neither the most delicious nor the cheapest is also one result since it is the most time-saving one.

![img](https://github.com/RussellOvO/EC601/edit/main/Project2/shortest.png)

