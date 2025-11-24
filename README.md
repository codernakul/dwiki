📚 **Interactive Wiki Encyclopedia**

A full-featured, Wikipedia-style web application built with Django.

📖 **About The Project**

This project is a dynamic encyclopedia application inspired by Wikipedia. It allows users to browse, search, create, and edit encyclopedia entries using a user-friendly interface.

The core engineering challenge was to build a system that seamlessly translates raw Markdown text into rendered HTML, ensuring that content creation is accessible while maintaining a polished frontend presentation.

✨ **Key Features**

- Markdown-to-HTML Conversion: Implemented a dynamic page rendering system that converts Markdown content (stored in backend files) into styled HTML on the fly.

- Create & Edit Functionality: Users can contribute new knowledge or update existing entries via a text-area interface pre-populated with current Markdown content.

- Robust Search Engine:

  - Direct Hit: Redirects immediately to the entry page if the query matches a title exactly.

  - Substring Matching: Returns a list of all entries containing the query string if no exact match is found.

- Random Entry Retrieval: A "Surprise Me" feature that redirects the user to a randomly selected encyclopedia entry.

- Error Handling: Custom error pages for non-existent entries (404 handling) to ensure a smooth user experience.

📖 **Demo**

![](https://github.com/codernakul/dwiki/blob/master/dwiki.gif)
