% Lecture 07 - HTTP and Web Applications
% None
% 1st March, 2017

Overview of This Lecture
------------------------

Examples?
•CUHK Website (http://www.cuhk.edu.hk/)
•Facebook Website (http://www.facebook.com/)
•HKO’s RSS Feed (http://rss.weather.gov.hk/)
•Instagram App
•Twitter REST API
•…

the above services make use of the HTTP protocol
•Let’s study more about HTTP first!

Layered Architecture

What are protocols?
•A set of rules that govern how communication parties interact with each other
•An agreement between the communicating entities
•Two devices need to agree on common protocols when they communicate

Some of the issues a protocol should cover
•The format of the addressing scheme
•How do we specify the start and end of a data stream
•How do we handle errors and data loss?
•How to handle problems in data transfer?

The ISO OSI (Open System Interconnection) 7-Layer Model
• A theoretical model of how a computer network should work
• It organises different functions of a network into 7 different layers
• It specifies the interfaces for communication between different
layers and different endpoints
1) It is a theoretical model
2) It is NOT a program or software
3) Practical networks may be implemented in different ways

The Hypertext Transfer Protocol (HTTP)

What is HTTP (Hypertext Transfer Protocol)?
• What happen between a request is made and a response is
received?

Tim Berners-Lee, credited as the inventor of the World Wide Web, created the original HTTP and HTML in 1990 at CERN
•For combining the Internet and hypertext

An application protocol for transferring hypertext and other file formats over the Internet
•Current widely used version: HTTP/1.1 (standardized in 1997)
•HTTP/2 specification was published as RFC 7540 in May 2015
•Client (e.g. Web browser) sends an HTTP request to a URL
•Server prepares and returns the requested resources

Request
An HTTP request has the following components
•URL - the unique identifier of the online resource
•Method/Verb – the action of the request (e.g. GET something?)
•HTTP Version – the version of the protocol you are using
•Headers – the metadata of the request
•Body – Data to be sent to the server

Response
An HTTP response has the following components
•Status Code – indicate whether the request is successful
•HTTP Version - the version of the protocol you are using
•Headers – metadata of the response
•Body – data of the resource requested

URL
Uniform Resource Locator (URL)
• A specific type of URI (Uniform resource identifier)
• It implies the means to access a resource
• Syntax of a URL:

Examples:
•CUHK Homepage http://www.cuhk.edu.hk/chinese/index.html
•YouTube Video https://www.youtube.com/watch?v=Q93o1yBr-Mc
•Apple Daily http://hkm.appledaily.com/list.php?category_guid=4104&category=daily
•Instagram API https://api.instagram.com/v1/users/self/feed?access_token=ACCESS-TOKEN

HTTP Request Methods
Indicate the desired action to be performed on the resource identified by the URL
•GET – retrieves data from the server
•HEAD – asks for a response same as GET, but without the body
•POST – asks the server to accept data enclosed in the request and apply it to the resource
•PUT – asks the server to store the data under the supplied URL
•Other methods: DELETE, TRACE, OPTIONS, CONNECT, PATCH

An example of GET: https://www.youtube.com/watch?v=Q93o1yBr-Mc
•Retrieve a YouTube video page providing the value of the parameter v
•It has no effect on the resource to be retrieved, it simply retrieves a copy of the resource “v=Q93olyBr-Mc” is the query string

Query String
•Each parameter and its value are specified by name=value
•Parameters are separated by ampersand “&”
•The maximum amount of information that can be passed to the server using the query string depends on the maximum length allowed for an URL (The limits of different browsers are different, usually at about 64K characters)
•NOT for passing sensitive data (e.g. password)

An example of POST:
https://twitter.com/login
• After filling in the user name and password
and clicking on the “Log in” button, the data
will be sent to Twitter’s server using the
“POST” method
• Usually used for submitting a form (e.g.
online forms, leaving comments, etc.)

Recall that HTTP is a text protocol (i.e. everything sent using HTTP are assumed to be characters) If you want to send files (binary data), you need to encode the binary data first before sending In an HTML form, set enctype=“multipart/form-data” (see next slide)

<form method=“post” enctype=“multipart/form-data”> <input type=“text” name=“name”> <input type=“file” name=“file”> <input type=“submit” value=“Send!”> </form>
Setting enctype=“multipart/form-data” tells the server that the data are split into multiple parts, one for each file, plus one for the textual data in the form body.
Ref: https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/Forms/Sending_and_retrieving_form_data

HTTP Headers
Headers contain metadata about the request/response, such as:
•Identity of the client
•Type of the content (e.g. plain text, HTML, CSS, image)
•Encoding of the content (e.g. ASCII, utf-8)
•Expiry date/time of the content
•Cookies
•…
For a list of HTTP request and response header fields, see: https://en.wikipedia.org/wiki/List_of_HTTP_header_fields

Inspecting HTTP Requests and Responses
Use the developer’s tools in Firefox or Chrome:

More on HTTP Headers
HTTP headers are sets of key-value pairs (field names and values)
Some of the request header “keys”:
• Accept: the preferred format of the resource
(e.g. text/html, application/json, application/xml)
• Accept-Language: the preferred language of the resource
(e.g. zh-TW, zh-CN, en-US)
• User-Agent: the type of browser or device
(e.g. indicate whether the client is on a PC or on a mobile)

More on HTTP Headers
Some of the response header “keys”:
• Content-Length: length of the content of the resource
• Content-Type: format of the resource
(e.g. text/html)
• Last-Modified: the time when the resource was last changed
• Server: The name of the Web server serving the resource
For a comprehensive list of header fields:
https://en.wikipedia.org/wiki/List_of_HTTP_header_fields

HTTP Status Code
HTTP Status code is included in a HTTP response to indicate the
outcome of an HTTP request
The different categories of HTTP status codes:
• 1XX: Informational
• 2XX: Successful
• 3XX: Redirection
• 4XX: Client-side error
• 5XX: Server-side error

HTTP Status Code
Examples of HTTP status codes
• 200: OK
Everything is OK, results should be in the response
• 301: Moved Permanently
The client should send request from the URL provided instead
• 403: Forbidden
The client is not authorised to access the resource
• 404: Not Found
The resource cannot be found
• 500: Internal Server Error

HTTPS
• HTTP over TLS,
HTTP over SSL or
HTTP Secure
• A protocol for
secure
communication
over the network
over the original
HTTP protocol

HTTPS
Will the following be visible to eavesdroppers when using HTTPS?
• Query strings in GET requests
• Parameters in POST requests
• File content in POST requests
• JSON content in POST requests
Why should we choose POST when sending sensitive data over
HTTP/HTTPS?

References
• Introduction to HTTP Basics
https://www3.ntu.edu.sg/home/ehchua/programming/webpr
ogramming/HTTP_Basics.html

Stateless-ness
HTTP is a stateless protocol
• The server does not retain information about clients between
requests
• Each request is considered independent
• No session information stored on the server-side
(See illustration on the next slide)



HTTP Servers

