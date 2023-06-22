# ai-chatbot
Implementation of  a fairly “vanilla” / standard LLM-powered chatbot using LangChain in a Python Lambda, which stores its history in a DynamoDB database.


## Project Description

This project involves the development of Python code that will run in an AWS Lambda function as part of pMD's application. The code will be invoked periodically in response to user chats or events within the application. The primary goal is to enable a chatbot to generate responses using LangChain's Language Model (LLM) AI, such as ChatGPT.

When the Python code is invoked, it will receive a prompt and access to a DynamoDB database that stores chat transcripts, including conversation history and summaries of recent chats for each user. With each invocation, the code will extract the ten most recent messages from the user's transcript using LangChain's DynamoDBChatMessageHistory object. It will also retrieve the summary of the user's recent chats from DynamoDB.

Using LangChain, the code will then leverage a specified LLM AI model (e.g., ChatGPT) to generate the next response for the chatbot. It will ensure that the DynamoDBChatMessageHistory object persists the new chats (user submissions and chatbot replies) into DynamoDB. Additionally, the code will utilize the ConversationSummaryBufferMemory object to update the summary of the user's recent interactions with the chatbot and store the updated summary in DynamoDB.

Finally, the AWS Lambda function will return the response generated by the chatbot.# PMD_chat
