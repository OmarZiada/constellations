# constellations
A python project dedicated to merging the worlds of flag design and data visualization!

Have a look at this post: https://www.reddit.com/r/coolguides/comments/kyeej0/us_flag_but_each_star_is_scaled_proportionally_to/?utm_source=share&utm_medium=web2x&context=3.

This reddit post shows a U.S. flag with the unequally sized stars in unfamiliar positions.
But actually this flag is rather more of a graph. I had collected U.S. population data by state and had made the height and wide of each of the stars proportional to that data; arranged it in the shape of a U.S. map and posted it on reddit. It caught on with over 80k upvotes.

Someone even expanded on the concept to another flag: https://www.reddit.com/r/vexillology/comments/kys2y6/brazils_national_flag_with_each_star_being_scaled/.
I thought the flag was very cool and I appreciate the creator for showing the scope of this concept.

But some took issue to my approach, why did I make the height and width propotional to the population, instead of the area? You see, the area of an object increases at the square of it's length, so bigger states had an advantage. To counteract this fault in my design. I had went back to my code and adjust the lengths of the stars to be proportional to the square root of the population, thus make the area proportional to the population.

Here's the result: https://imgur.com/a/yT3bLWz.

Less impressive, but more just.

I then decided to branch out, not limiting the data set to the population: https://www.reddit.com/r/interestingasfuck/comments/l2tg21/us_flags_where_the_stars_are_proportional_in_area/.

In the code provided, you can enter custom data as instructed when running the script. I think this concept is very interesting and deserves mroe developement. Thing is, I'm no pro. I'm a sort of comfortable beginner when it comes to python and I don't have the skills to improve this project. That's why I'm providing to the public.

Here are some issues with my code:

- Stars can overlap
  - I can't figure out a padding algorithm for the stars
- Sizing of stars isn't automatic
  - Data set size varies. From average age to population, you need different scaling factors for your data. I haven't been able to find a way to automate that process
- No way of intiutively finding coordinates for stars.
  - I'm thinking you can find the actual geographical coordinates of the locations and feed them in the script. But I don't know if that's possible
  
  Thank you for you intrest in this project!
