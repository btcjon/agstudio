Given a list of URLs saved in a text file, after we have reported the total number crawled, 
we want to extract and print the unique first-level subdirectories.

For example, if we have the following URLs:

https://microsoft.github.io/autogen/blog/2023/11/26/Agent-AutoBuild
https://microsoft.github.io/autogen/docs/reference/agentchat/user_proxy_agent
https://microsoft.github.io/autogen/docs/Getting-Started
https://microsoft.github.io/autogen/blog/tags/research
https://microsoft.github.io/autogen/

We want to report the unique directories gathered, which from our example above are:

/blog
/docs
/

our current incorrect print to user:

'Saved 73 URLs to tools/scrape/microsoft.github.io/urls.txt
The following subdirectories saved:
/autogen/'

still not getting correct result.  maybe it does not have access somehow to the urls?  maybe it should wait until they are printed to report, or maybe our logic is wrong, but what we are doing now is not working.
