# Task

For this assignment, you’ll build a chatbot app and write a 1500-word report.

# Assignment details

## Step 1: Read the scenario
A travel blogger has been commissioned by the (fictional) travel website Go Travel! to explore England and to post regular updates on their trip. In preparation for this blog series, the owners of the website have worked with a developer to create a Flask API framework prototype. This will integrate with their site and return weather data for each specific location on the blogger’s itinerary. They are in the process of testing the prototype, which uses an API to connect to OpenWeather Links to an external site. and then returns weather data based on the location entered into a user form.

**Itinerary**

  * Cumbria
  * Corfe Castle 
  * The Cotswolds 
  * Cambridge 
  * Bristol 
  * Oxford 
  * Norwich
  * Stonehenge 
  * Watergate Bay
  * Birmingham

However, during the testing process, they discover some limitations that they would like you to suggest solutions for. 

**Issues:**

* The current prototype can only return daily weather data.
* They have not budgeted for the additional cost of using the OpenWeather API if site traffic increases and calls to the API exceed the free 1,000 calls per day.
* The prototype can only return data for one location per query, accessed by the user entering data into the prototype form.

Ultimately, they would like to integrate a chatbot that can handle multiple queries. This will need to be able to access weather data for five days so the blogger can pre-plan activities, based on daily conditions. 

## Step 2: Build a chatbot

While building the chatbot, keep the following questions in mind:

* How can you apply the coding techniques you have learned during the last eight weeks?
* What conclusion can you draw from every step of the coding process and what do your results indicate?
* What blockers have you experienced and how do you rectify code that is not working?
*  Can you add some extra levels to your coding that will indicate you have grown in your Python skills?

Your tasks may not be limited to what is expected from you as laid out in the list. If you choose to use a different method than employed during Weeks 1-8, clearly state your reasoning.

### Recommended approach

Some actions you might pursue:

* Create a design for a chatbot that will meet the business requirements in the scenario. You should consider how you will justify your design decisions. 
* Design questions and responses for the chatbot, which will be accessed through a database.
* Elaborate on how integrating with multiple APIs, including weather and an additional service (e.g., news or events), enriches the chatbot's functionality and user experience, addressing the scenario's requirements comprehensively.
* Incorporate comprehensive error handling and input validation in your Python solution, ensuring the chatbot remains robust against unexpected inputs and API response failures.
* Conduct a test deployment in Flask, evaluating the chatbot's scalability and performance. Identify and document optimisations to address potential bottlenecks or scalability challenges.
* Your chatbot should demonstrate the effective use of Python libraries such as Chatterbot, Requests, JSON, HTML, SQL and Flask to create a functional chatbot that can send queries to, and receive data from, an external API and/or database. (Ultimately, the chatbot should not only answer queries but also engage users with dynamic follow-up questions, tailoring the conversation based on their responses for a more personalised interaction.)
* Finally, you will complete a brief reflection on your learning.

**Note:**

* At a minimum, your solution should demonstrate successful integration with an API and/or database and should provide at least one response. 
* You will demonstrate proficiency by using what you’ve learned to create inputs and outputs that demonstrate at least three questions and responses. 
* To excel, you will need to demonstrate the ability to add functionality beyond what is detailed in the brief; for example, advice based on weather conditions, or places to visit based on user queries.

## Step 3: Upload your program to GitHub

* Make sure it’s public.
* Create a README to give guidance to someone accessing your program.

## Step 4: Write a report

In your report, you should include the following:

* An analysis of the scenario, detailing how your chosen solution will address the requirements (200 words)
* Justification of the approach you used in creating, building, and deploying the chatbot (500 words)
* Details of the process you followed to test the chatbot. Write up the outcome of the testing as well as what lessons you learned, and what you would do differently in future. (500 words)
* Your reflection on challenges faced and the advantages of utilising test-driven processes when writing code. What challenges did you encounter, and how did you overcome them? (300 words)
* Include a link to the GitHub repository you created in Step 3.

**Tip:**

* You can include screenshots of code snippets and outputs from PyCharm or Python that might help you support your explanation and rationale.

# Assessment Criteria

## Analysis of the scenario and justifications for decisions made in the chatbot design. (30%)

|NP|P |C|D|HD|
|---|---|---|---|---|
| No attempts to justify or contextualise decisions. | An attempt has been made to justify decisions made. However, there are gaps in the descriptions included. | Some justification and context for decisions made. | The analysis provides a detailed rationale for the chatbot design decisions, clearly linking features and functionalities to the specific requirements of the scenario. | The analysis offers deep insights into the chatbot design, including a sophisticated rationale for all decisions made. It demonstrates how the design choices align with advanced business needs and user expectations, suggesting potential for scalability. |

## Use Python code appropriately to build a chatbot. (45%)

|NP|P |C|D|HD|
|---|---|---|---|---|
|No attempt made to create working code.| Limited attempt to complete the code, or response displays limited information about key elements of the Python script and understanding of Python programming.|The code is mostly complete, may lack commenting or logical flow but works on a basic level. Attempts made to address limitations.|The Python code for the chatbot is complete and demonstrates an efficient structure with comprehensive comments. The Python code for the chatbot is complete and demonstrates an efficient structure with comprehensive comments. It showcases good coding practices, with all key functionalities addressed, limitations thoroughly considered, and a number of positive and negative test cases included.|The Python code not only meets the requirements but also showcases exceptional coding practices, extending beyond the basic functionalities to include advanced features and a comprehensive test framework in place. The code structure is exemplary, with detailed comments that facilitate understanding and future enhancements.|

## Reflection of learning. ( 25%)

|NP|P |C|D|HD|
|---|---|---|---|---|
|No attempt to complete the written report, or report does not include reflection on development or lessons learned.|Little or no justification or critical evaluation of approach to the assignment. Thoughts not clearly organised.|Superficial justification  and evaluation of approach. Thoughts are unclear in some parts, and concepts are not communicated logically.|The reflection articulates a clear and coherent evaluation of the learning process, detailing the challenges faced, how they were overcome, and the key lessons learned. The writing is well-organised, indicating thoughtful engagement with the project.|The reflection demonstrates profound insights into the learning journey, offering a critical analysis of the project's development, including personal growth and professional development. It suggests actionable steps for future projects, reflecting a high degree of self-awareness and strategic thinking.|
