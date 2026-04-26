# CS 340 Portfolio Reflection

##  How do you write programs that are maintainable, readable, and adaptable?

To ensure that the programs I write are easy to maintain, understand, and adapt to new situations, I develop them using modular code organization.

For example, for this project, the CRUD Python module separated the logic associated with accessing the MongoDB database from the logic associated with developing the user interface for the dashboard. As a result of separating these two areas of logic, I did not have to include MongoDB connection code in the dashboard.

The CRUD module handled all of the create, read, update, and delete operations related to access to the MongoDB database. Thus, the code used to display the user interface of the dashboard could remain focused solely on creating a user-friendly experience, rather than having to contain both database and user interface functionality.

An important benefit of programming in this manner is that once developed and tested; the CRUD module can be reused elsewhere within the application. Since I only wrote the database connection logic in one location, changing something in the database operation can now be done in just that one location. The reusable nature of the CRUD module allows me to reuse it for other potential future animal shelter dashboards, reporting tools, or applications that will need to connect to the same MongoDB database. It could potentially expand to include more advance search capabilities, updates and deletes.

##  How do you approach a problem as a computer scientist?

When I am addressing problems as a computer scientist I begin by learning as much as possible about what the client wants to accomplish. Then I break down the problem into smaller components. Using this method allowed me to focus on identifying dogs that might be good candidates for rescue training at Grazioso Salvare.

Once I identified what the client wanted to accomplish from the data and dashboard, I began to develop queries that met their needs. The client needed a way to find dogs that were suitable for rescue training based on certain criteria.

Thus far, most of the assigned projects have been relatively straightforward and could best be described as "completing a coding assignment." However, there was something different about this project. While still solving a problem, this project involved meeting specific requirements from a client. The requirement was not simply to complete an assignment but also to create a product that was functional, user friendly and tied to actual data.

Additionally, in order for the client to utilize the products they desired; I had to consider how the user would interact with the various elements.

In future database projects I will continue to follow this same general approach by first identifying the clients goals, analyzing the available data, creating queries that are helpful and allow for analysis, testing my database operations, and finally presenting the results in an understandable format via a user interface.

##  What do computer scientists do, and why does it matter?

Computer Science professionals design solutions for individuals to work with data, solve problems, and make better informed decisions. Solutions created by computer science professionals enable many organizations to collect and organize data automatically and efficiently using software systems.

This project has provided Grazioso Salvare with a functional dashboard to rapidly locate relevant animal shelter data for identification of dogs that may be good candidates for rescue training. Without a dashboard, the users would have to individually sift through vast amounts of data to locate suitable animals.

This individual effort would require significantly longer periods of time and could increase error rates. The rapid development of a dashboard utilizing MongoDB, a Python-based CRUD module for database interaction and visualization techniques for displaying data greatly aids the decision-making process for Grazioso Salvare.
