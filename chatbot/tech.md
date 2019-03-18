##Unit Testing

When developing the app unit testing was needed so that any potential problems that may arise could be detected early and dealt with. With this in mind we decided to unit test each part of the app as it was built.

The first testing we did was Unit testing on the app after the search component was developed. In order to test that the Open Street maps search was sufficient we used the component in a variety of locations to get different GPS coordinates and therefore different search results. This was to make sure that the backend code could work with all coordinates given.

![alt text](testing/O_connells.png) 

Fig 1.1

This Open Street Maps search was done on O’Connells street in town by us. The location was set to only 5km and the results are pretty lengthy.   

![alt text](testing/Skryne.png) 

Fig 1.2

This search  was done in the countryside of Skryne, Co. Meath with radius of 13km. As you can see in Fig 1.2 there is very little results in comparison to the city centre.


The next unit testing we did was based on the database to make sure that things were storing properly. The django admin page was a great for this as it allowed us to see all the entries for all the users provided we had admin access.

![alt text](testing/3.png)
Fig 2.1 
Fig 2.1 shows a result from querying the the search component of our app. Upon clicking the save search the search should save to the database. 

![alt text](testing/4.png)
Fig 2.2

This image shows the django admin page. I went into the database and found the result I had just saved with the app confirming that the save search works.


After the development of the chatbot, the chatbot was asked the top 10 frequently asked recycling queries found online. Our recycling chatbot responded appropriately when we asked the chatbot as testing.

The accounts side of the app was tested similarly to the other database models by checking the Django admin page after creating new instances of the model. We created new model instances for made up users to JohnDoe and MarySmith on our system via the signup page and checked the admin for the entries in the user database.

User testing


This questionnaire was done by fifteen users for our Beta testing stage. The users signed our consent forms and their data was made anonymous. When conducting testing we gave the test users our user manual and asked them to navigate the website and give feedback when they were done. Once all users were done their questionnaires, the results were recorded and reviewed by us. It was clear from the feedback that the users were in general happy with the app but there were a few people dissatisfied with the UI so after feedback we decided to change the layout of our EcoPal application user interface to make it more sleek and add a bit of color. 

This is the data collected from our questionnaire.

![alt text](testing/result1.png)
As you can see the overall experience of EcoPal was great/ good.

![alt text](testing/result2.png)
People found it mostly easy to navigate around  EcoPal with 26.7% saying it was basic.

![alt text](testing/result3.png)
As you can see the highest number of people found it easy to use our Recycling Search

![alt text](testing/result4.png)
Many people found it easy to use our chat bot but we did change the layout to make it easier for users to interact with.


![alt text](testing/result5.png)
The recycling search rarely gave back insufficient results.



![alt text](testing/result6.png)
The ChatBot rarely returned inappropriate answers.

![alt text](testing/result7.png)

Many people thought it was but there were a few who thought it wasn't.


Is there anything you could tell us to improve our app4 responses
Colors
no address listed, chatbot gave random answer
Colors hard on eyes
the results could be displayed better

##What we changed

These are the comments we received on how we can improve our app.
We took the report above and the suggested comments and we made some changes.
First we adjusted the UI, we changed the color scheme to a more basic neutral look as it looks sleeker and more approachable. We originally a lot of blues and green tones to compliment the usual colors used for recycling but changed them to neutral greys and light blues to avoid a high contrast.  

The address were originally not listed when the search feature came back with results only how far away, we changed this to include the address.
The chatbot returning a random answer is due to it not being able to find an appropriate one. We added a default response in for when this happens so the chatbot does not return random responses
On both the search results and the chatbot we improved on how we display our data.
The search results are displayed more spaced out and the result number bolded so it's easy to read through. The chatbot answer is now displayed above the textbox much like a texting app as people are more familiar with looking above where they have typed for a reply rather than below


