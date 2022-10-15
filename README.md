# Recommendation System

Machine learning solves many problems but making product recommendations is a widely known application of machine learning. There are three main types of recommendation systems

### Plan:
```
Recommendation system
    |
    |
    |-----> Collaborative filtering
    |       |
    |       |------> User-User collaborative filtering : User-Item Collaborative Filtering : “Users who are similar to you also liked …”
    |       |
    |       |------>Item-Item collaborative filtering : “Users who liked this item also liked …”
    |
    |
    |-----> Content Based Filtering
    |
    |
    |------>Hybrid Recommendation Systems

```
### Collaborative Filtering

The collaborative filtering method is based on gathering and analysing data on user’s behaviour. This includes the user’s online activities and predicting what they will like based on the similarity with other users.

![alt text](https://miro.medium.com/max/828/1*SPE85ePd_aiJDO9RVbfbig.png)

For example, if user A likes Apple, Banana, and Mango while user B likes Apple, Banana, and Jackfruit, they have similar interests. So, it is highly likely that A would like Jackfruit and B would enjoy Mango. This is how collaborative filtering takes place.
#### Two kinds of collaborative filtering techniques used are:
- User-User collaborative filtering
- Item-Item collaborative filtering

One of the main advantages of this recommendation system is that it can recommend complex items precisely without understanding the object itself. There is no reliance on machine analysable content.

### Content-Based Filtering

Content-based filtering methods are based on the description of a product and a profile of the user’s preferred choices. In this recommendation system, products are described using keywords, and a user profile is built to express the kind of item this user likes.

![alt text](https://miro.medium.com/max/828/1*3YEZG1dEqvNz70h0uhP5Fg.png)

For instance, if a user likes to watch movies such as Iron Man, the recommender system recommends movies of the superhero genre or films describing Tony Stark.
The central assumption of content-based filtering is that you will also like a similar item if you like a particular item.

### Hybrid Recommendation Systems

In hybrid recommendation systems, products are recommended using both content-based and collaborative filtering simultaneously to suggest a broader range of products to customers. This recommendation system is up-and-coming and is said to provide more accurate recommendations than other recommender systems.
![alt text](https://miro.medium.com/max/828/1*jBBeSKBQg4H7VslNT34f4w.png)

Netflix is an excellent case in point of a hybrid recommendation system. It makes recommendations by juxtaposing users’ watching and searching habits and finding similar users on that platform. This way, Netflix uses collaborative filtering.
By recommending such shows/movies that share similar traits with those rated highly by the user, Netflix uses content-based filtering. They can also veto the common issues in recommendation systems, such as cold start and data insufficiency issues.


### Dataset: [Dataset link](https://www.kaggle.com/datasets/prajitdatta/movielens-100k-dataset)
